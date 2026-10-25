"""
EduManage - School Management System (Streamlit)

Run with:  streamlit run app.py
Uses the same School_data.json file (and schema) as the console version.
"""
from __future__ import annotations

import html
import json
import os
import re
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path

import altair as alt
import pandas as pd
import streamlit as st

# ----------------------------------------------------------------------------
# Config
# ----------------------------------------------------------------------------
DB_PATH = Path(__file__).parent / "School_data.json"
EMAIL_RE = re.compile(r"^[\w.+-]+@[\w-]+(\.[\w-]+)+$")
PASS_MARK = 40.0
ACCENT = "#6366F1"
GRADE_BANDS = [(90, "A+"), (80, "A"), (70, "B"),
               (60, "C"), (50, "D"), (40, "E"), (0, "F")]
GRADE_ORDER = [g for _, g in GRADE_BANDS]

st.set_page_config(
    page_title="EduManage | School Management",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------------------------
# Styling
# ----------------------------------------------------------------------------
st.markdown(
    """
<style>
#MainMenu, footer {visibility: hidden;}
header[data-testid="stHeader"] {background: transparent;}
.block-container {padding-top: 2rem; padding-bottom: 3rem; max-width: 1320px;}

/* Hero banner */
.hero {
    background: linear-gradient(120deg, #4F46E5 0%, #7C3AED 60%, #EC4899 130%);
    color: #fff; padding: 1.6rem 2rem; border-radius: 18px; margin-bottom: 1.4rem;
    box-shadow: 0 12px 30px -14px rgba(79, 70, 229, .7);
}
.hero .title {font-size: 1.9rem; font-weight: 700; line-height: 1.2; margin: 0;}
.hero .subtitle {margin: .3rem 0 0; opacity: .88; font-size: .98rem;}

/* KPI cards */
.kpi {
    border: 1px solid rgba(128,128,128,.22); background: rgba(128,128,128,.06);
    border-radius: 16px; padding: 1.1rem 1.3rem; position: relative; overflow: hidden;
    height: 100%;
}
.kpi::before {content: ""; position: absolute; left: 0; top: 0; bottom: 0; width: 4px; background: var(--accent, #6366F1);}
.kpi .label {font-size: .74rem; text-transform: uppercase; letter-spacing: .09em; opacity: .7; font-weight: 600;}
.kpi .value {font-size: 2.1rem; font-weight: 700; line-height: 1.25; margin-top: .15rem;}
.kpi .sub {font-size: .8rem; opacity: .65;}
.kpi .icon {position: absolute; right: 16px; top: 12px; font-size: 1.7rem;}

/* Profile card */
.profile {
    display: flex; gap: 1.2rem; align-items: center; padding: 1.2rem 1.4rem; margin-bottom: 1rem;
    border: 1px solid rgba(128,128,128,.22); background: rgba(128,128,128,.06); border-radius: 16px;
}
.avatar {
    width: 68px; height: 68px; min-width: 68px; border-radius: 50%; color: #fff; font-weight: 700; font-size: 1.5rem;
    background: linear-gradient(135deg, #6366F1, #EC4899); display: flex; align-items: center; justify-content: center;
}
.profile .name {font-size: 1.35rem; font-weight: 700; line-height: 1.2;}
.profile .meta {opacity: .72; font-size: .92rem; margin-top: .15rem;}

/* Badges */
.badge {display: inline-block; padding: .14rem .65rem; border-radius: 999px; font-size: .74rem; font-weight: 600; margin-right: .35rem;}
.badge.pass {background: rgba(16,185,129,.16); color: #10B981;}
.badge.fail {background: rgba(239,68,68,.16); color: #EF4444;}
.badge.muted {background: rgba(128,128,128,.18);}
.badge.info {background: rgba(99,102,241,.18); color: #818CF8;}

/* Empty state */
.empty {text-align: center; padding: 2.6rem 1rem; border: 2px dashed rgba(128,128,128,.3); border-radius: 16px; opacity: .88;}
.empty .big {font-size: 2.4rem;}

/* Section heading */
.section-title {font-size: 1.05rem; font-weight: 650; margin: .4rem 0 .6rem;}

/* Sidebar brand */
.brand {display: flex; align-items: center; gap: .6rem; margin: .2rem 0 1.2rem;}
.brand .logo {
    width: 40px; height: 40px; border-radius: 12px; display: flex; align-items: center; justify-content: center;
    background: linear-gradient(135deg, #6366F1, #8B5CF6); font-size: 1.3rem;
}
.brand .text {font-weight: 750; font-size: 1.15rem; line-height: 1.1;}
.brand .tag {font-size: .72rem; opacity: .6;}

/* Primary buttons / nav */
button[kind="primary"], button[data-testid="stBaseButton-primary"],
button[data-testid="stBaseButton-primaryFormSubmit"] {
    background: linear-gradient(120deg, #6366F1, #8B5CF6) !important; border: none !important; color: #fff !important;
}
button[kind="primary"]:hover, button[data-testid="stBaseButton-primary"]:hover,
button[data-testid="stBaseButton-primaryFormSubmit"]:hover {filter: brightness(1.08);}
section[data-testid="stSidebar"] button {text-align: left; justify-content: flex-start;}
div[data-testid="stForm"] {border-radius: 16px;}
</style>
""",
    unsafe_allow_html=True,
)


# ----------------------------------------------------------------------------
# Storage (same file + schema as the console app)
# ----------------------------------------------------------------------------
def load_data() -> dict:
    data = {"Students": [], "Teacher": []}
    if DB_PATH.exists():
        try:
            content = DB_PATH.read_text(encoding="utf-8").strip()
            if content:
                loaded = json.loads(content)
                if isinstance(loaded, dict):
                    data.update(loaded)
        except (json.JSONDecodeError, OSError) as exc:
            st.error(f"Could not read {DB_PATH.name}: {exc}")
    data.setdefault("Students", [])
    data.setdefault("Teacher", [])
    return data


def save_data(data: dict) -> None:
    tmp = DB_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, indent=4), encoding="utf-8")
    os.replace(tmp, DB_PATH)  # atomic: never leaves a half-written file


# ----------------------------------------------------------------------------
# Domain layer
# ----------------------------------------------------------------------------
def letter(avg: float | None) -> str:
    if avg is None:
        return "-"
    for threshold, grade in GRADE_BANDS:
        if avg >= threshold:
            return grade
    return "F"


def student_avg(student: dict) -> float | None:
    grades = student.get("grades", {})
    return sum(grades.values()) / len(grades) if grades else None


class Person(ABC):
    collection = ""
    id_field = ""

    def __init__(self, data: dict):
        self.data = data

    @abstractmethod
    def get_role(self) -> str: ...

    @abstractmethod
    def register(self, **fields) -> tuple[bool, str]: ...

    @abstractmethod
    def show_details(self, key: str) -> dict | None: ...

    @staticmethod
    def validate_email(email: str) -> bool:
        return bool(EMAIL_RE.match(email or ""))

    def records(self) -> list:
        return self.data[self.collection]

    def find(self, key: str) -> dict | None:
        return next((r for r in self.records() if r.get(self.id_field) == key), None)

    def remove(self, key: str) -> bool:
        rec = self.find(key)
        if rec is None:
            return False
        self.records().remove(rec)
        save_data(self.data)
        return True

    def _check_common(self, name: str, email: str, ignore_key: str | None = None) -> str | None:
        if not name.strip():
            return "Name is required."
        if not self.validate_email(email.strip()):
            return "Please enter a valid email address."
        for r in self.records():
            if r.get(self.id_field) != ignore_key and r.get("email", "").lower() == email.strip().lower():
                return "That email is already registered."
        return None


class Student(Person):
    collection = "Students"
    id_field = "roll_no"

    def get_role(self) -> str:
        return "Student"

    def register(self, name: str, age: int, email: str, roll_no: str) -> tuple[bool, str]:
        roll_no = roll_no.strip()
        if not roll_no:
            return False, "Roll number is required."
        err = self._check_common(name, email)
        if err:
            return False, err
        if self.find(roll_no):
            return False, f"A student with roll number {roll_no} already exists."
        self.records().append({
            "name": name.strip(), "age": int(age), "email": email.strip(), "roll_no": roll_no,
            "grades": {}, "registered_on": datetime.now().strftime("%Y-%m-%d"),
        })
        save_data(self.data)
        return True, f"Student {name.strip()} registered successfully!"

    def update(self, roll_no: str, name: str, age: int, email: str) -> tuple[bool, str]:
        rec = self.find(roll_no)
        if rec is None:
            return False, "Student not found."
        err = self._check_common(name, email, ignore_key=roll_no)
        if err:
            return False, err
        rec.update({"name": name.strip(), "age": int(
            age), "email": email.strip()})
        save_data(self.data)
        return True, "Student details updated."

    def add_grade(self, roll_no: str, subject: str, marks: float) -> tuple[bool, str]:
        subject = subject.strip()
        if not subject:
            return False, "Subject is required."
        if not 0 <= marks <= 100:
            return False, "Marks must be between 0 and 100."
        rec = self.find(roll_no)
        if rec is None:
            return False, "Student not found."
        rec.setdefault("grades", {})[subject] = float(marks)
        save_data(self.data)
        return True, f"{subject}: {marks:g} saved for {rec['name']}."

    def remove_grade(self, roll_no: str, subject: str) -> bool:
        rec = self.find(roll_no)
        if rec and subject in rec.get("grades", {}):
            del rec["grades"][subject]
            save_data(self.data)
            return True
        return False

    def show_details(self, key: str) -> dict | None:
        rec = self.find(key)
        if rec is None:
            return None
        avg = student_avg(rec)
        return {**rec, "average": avg, "letter": letter(avg), "passed": avg is not None and avg >= PASS_MARK}


class Teacher(Person):
    collection = "Teacher"
    id_field = "emp_id"

    def get_role(self) -> str:
        return "Teacher"

    def register(self, name: str, age: int, email: str, emp_id: str, department: str = "") -> tuple[bool, str]:
        emp_id = emp_id.strip()
        if not emp_id:
            return False, "Employee ID is required."
        err = self._check_common(name, email)
        if err:
            return False, err
        if self.find(emp_id):
            return False, f"A teacher with employee ID {emp_id} already exists."
        self.records().append({
            "name": name.strip(), "age": int(age), "email": email.strip(), "emp_id": emp_id,
            "department": department.strip(), "registered_on": datetime.now().strftime("%Y-%m-%d"),
        })
        save_data(self.data)
        return True, f"Teacher {name.strip()} registered successfully!"

    def update(self, emp_id: str, name: str, age: int, email: str, department: str) -> tuple[bool, str]:
        rec = self.find(emp_id)
        if rec is None:
            return False, "Teacher not found."
        err = self._check_common(name, email, ignore_key=emp_id)
        if err:
            return False, err
        rec.update({"name": name.strip(), "age": int(age),
                   "email": email.strip(), "department": department.strip()})
        save_data(self.data)
        return True, "Teacher details updated."

    def show_details(self, key: str) -> dict | None:
        return self.find(key)


# ----------------------------------------------------------------------------
# DataFrame helpers
# ----------------------------------------------------------------------------
def students_df(data: dict) -> pd.DataFrame:
    cols = ["Roll No", "Name", "Age", "Email",
            "Subjects", "Average", "Grade", "Registered"]
    rows = []
    for s in data["Students"]:
        avg = student_avg(s)
        rows.append({
            "Roll No": s["roll_no"], "Name": s["name"], "Age": s["age"], "Email": s["email"],
            "Subjects": len(s.get("grades", {})),
            "Average": round(avg, 2) if avg is not None else None,
            "Grade": letter(avg), "Registered": s.get("registered_on", "-"),
        })
    return pd.DataFrame(rows, columns=cols)


def teachers_df(data: dict) -> pd.DataFrame:
    cols = ["Employee ID", "Name", "Age", "Email", "Department", "Registered"]
    rows = [{
        "Employee ID": t["emp_id"], "Name": t["name"], "Age": t["age"], "Email": t["email"],
        "Department": t.get("department") or "-", "Registered": t.get("registered_on", "-"),
    } for t in data["Teacher"]]
    return pd.DataFrame(rows, columns=cols)


def subject_stats(data: dict) -> pd.DataFrame:
    marks: dict[str, list[float]] = {}
    for s in data["Students"]:
        for subj, m in s.get("grades", {}).items():
            marks.setdefault(subj, []).append(m)
    rows = [{
        "Subject": subj, "Students": len(v), "Average": round(sum(v) / len(v), 2),
        "Highest": max(v), "Lowest": min(v), "Pass rate": round(100 * sum(m >= PASS_MARK for m in v) / len(v), 1),
    } for subj, v in sorted(marks.items())]
    return pd.DataFrame(rows, columns=["Subject", "Students", "Average", "Highest", "Lowest", "Pass rate"])


def gradebook_df(data: dict) -> pd.DataFrame:
    subjects = sorted({subj for s in data["Students"]
                      for subj in s.get("grades", {})})
    rows = []
    for s in data["Students"]:
        avg = student_avg(s)
        row = {"Roll No": s["roll_no"], "Name": s["name"]}
        for subj in subjects:
            row[subj] = s.get("grades", {}).get(subj)
        row["Average"] = round(avg, 2) if avg is not None else None
        row["Grade"] = letter(avg)
        rows.append(row)
    return pd.DataFrame(rows, columns=["Roll No", "Name", *subjects, "Average", "Grade"])


def csv_bytes(df: pd.DataFrame) -> bytes:
    return df.to_csv(index=False).encode("utf-8")


# ----------------------------------------------------------------------------
# UI helpers
# ----------------------------------------------------------------------------
def hero(title: str, subtitle: str) -> None:
    st.markdown(
        f'<div class="hero"><div class="title">{html.escape(title)}</div>'
        f'<div class="subtitle">{html.escape(subtitle)}</div></div>',
        unsafe_allow_html=True,
    )


def kpi(label: str, value: str, sub: str, icon: str, color: str = ACCENT) -> str:
    return (
        f'<div class="kpi" style="--accent:{color}"><div class="icon">{icon}</div>'
        f'<div class="label">{html.escape(label)}</div><div class="value">{html.escape(value)}</div>'
        f'<div class="sub">{html.escape(sub)}</div></div>'
    )


def empty_state(icon: str, title: str, text: str) -> None:
    st.markdown(
        f'<div class="empty"><div class="big">{icon}</div><h4>{html.escape(title)}</h4>'
        f'<div>{html.escape(text)}</div></div>',
        unsafe_allow_html=True,
    )


def section(title: str) -> None:
    st.markdown(
        f'<div class="section-title">{html.escape(title)}</div>', unsafe_allow_html=True)


def initials(name: str) -> str:
    parts = name.split()
    if not parts:
        return "?"
    return (parts[0][0] + (parts[-1][0] if len(parts) > 1 else "")).upper()


def flash(message: str, icon: str = "✅") -> None:
    st.session_state["_flash"] = (message, icon)


def show_flash() -> None:
    if "_flash" in st.session_state:
        message, icon = st.session_state.pop("_flash")
        st.toast(message, icon=icon)


def form_key(name: str) -> str:
    return f"{name}_{st.session_state.get('form_n', 0)}"


def bump_form() -> None:
    st.session_state["form_n"] = st.session_state.get("form_n", 0) + 1


def goto(page: str) -> None:
    st.session_state["page"] = page


def bar_chart(df: pd.DataFrame, x: str, y: str, height: int = 280, color: str = ACCENT) -> alt.Chart:
    return (
        alt.Chart(df)
        .mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6, color=color)
        .encode(
            x=alt.X(f"{x}:N", sort=None, axis=alt.Axis(
                labelAngle=0, title=None)),
            y=alt.Y(f"{y}:Q", axis=alt.Axis(title=None)),
            tooltip=list(df.columns),
        )
        .properties(height=height)
    )


# ----------------------------------------------------------------------------
# Pages
# ----------------------------------------------------------------------------
def page_dashboard(data: dict) -> None:
    hero("Dashboard", f"School overview · {datetime.now():%A, %d %B %Y}")

    sdf = students_df(data)
    graded = sdf.dropna(subset=["Average"])
    class_avg = graded["Average"].mean() if not graded.empty else None
    pass_rate = 100 * (graded["Average"] >=
                       PASS_MARK).mean() if not graded.empty else None

    c1, c2, c3, c4 = st.columns(4)
    c1.markdown(kpi("Students", str(
        len(data["Students"])), "enrolled", "🎓", "#6366F1"), unsafe_allow_html=True)
    c2.markdown(kpi("Teachers", str(
        len(data["Teacher"])), "on staff", "👩‍🏫", "#EC4899"), unsafe_allow_html=True)
    c3.markdown(kpi("Class average", f"{class_avg:.1f}" if class_avg is not None else "-",
                    f"grade {letter(class_avg)}" if class_avg is not None else "no grades yet", "📈", "#10B981"),
                unsafe_allow_html=True)
    c4.markdown(kpi("Pass rate", f"{pass_rate:.0f}%" if pass_rate is not None else "-",
                    f"pass mark {PASS_MARK:g}", "✅", "#F59E0B"), unsafe_allow_html=True)
    st.write("")

    if not data["Students"] and not data["Teacher"]:
        empty_state("🏫", "Welcome to EduManage",
                    "Your school is empty. Register your first student or teacher to get started.")
        a, b, _ = st.columns([1, 1, 3])
        a.button("➕ Add a student", on_click=goto, args=(
            "Students",), type="primary", width="stretch")
        b.button("➕ Add a teacher", on_click=goto,
                 args=("Teachers",), width="stretch")
        return

    left, right = st.columns(2)
    with left:
        section("Grade distribution")
        if graded.empty:
            empty_state("📝", "No grades yet",
                        "Record some marks to see the distribution.")
        else:
            dist = graded["Grade"].value_counts().reindex(
                GRADE_ORDER, fill_value=0).reset_index()
            dist.columns = ["Grade", "Students"]
            st.altair_chart(bar_chart(dist, "Grade", "Students",
                            color="#8B5CF6"), width="stretch")
    with right:
        section("Average marks by subject")
        stats = subject_stats(data)
        if stats.empty:
            empty_state("📚", "No subjects yet",
                        "Subjects appear here once grades are recorded.")
        else:
            chart = bar_chart(stats[["Subject", "Average"]],
                              "Subject", "Average", color="#6366F1")
            st.altair_chart(chart.encode(y=alt.Y("Average:Q", scale=alt.Scale(domain=[0, 100]), axis=alt.Axis(title=None))),
                            width="stretch")

    left, right = st.columns(2)
    with left:
        section("🏆 Top performers")
        top = graded.sort_values("Average", ascending=False).head(5)[
            ["Roll No", "Name", "Average", "Grade"]]
        if top.empty:
            st.caption("No graded students yet.")
        else:
            st.dataframe(top, hide_index=True, width="stretch",
                         column_config={"Average": st.column_config.ProgressColumn("Average", min_value=0, max_value=100, format="%.1f")})
    with right:
        section("🆕 Recently registered students")
        recent = sdf.tail(
            5).iloc[::-1][["Roll No", "Name", "Email", "Registered"]]
        if recent.empty:
            st.caption("No students yet.")
        else:
            st.dataframe(recent, hide_index=True, width="stretch")


def page_students(data: dict) -> None:
    svc = Student(data)
    hero("Students", "Register, search and manage student records")
    tab_dir, tab_reg, tab_prof = st.tabs(
        ["📋 Directory", "➕ Register", "👤 Profile"])

    with tab_dir:
        df = students_df(data)
        if df.empty:
            empty_state("🎓", "No students yet",
                        "Use the Register tab to add your first student.")
        else:
            c1, c2, c3 = st.columns([3, 2, 1.2])
            query = c1.text_input(
                "Search", placeholder="Search by name, roll number or email…", label_visibility="collapsed")
            sort_by = c2.selectbox("Sort by", [
                                   "Name", "Roll No", "Average", "Age", "Registered"], label_visibility="collapsed")
            c3.download_button("⬇ Export CSV", csv_bytes(
                df), "students.csv", "text/csv", width="stretch")
            if query:
                mask = df[["Name", "Roll No", "Email"]].apply(lambda col: col.astype(
                    str).str.contains(query, case=False, na=False)).any(axis=1)
                df = df[mask]
            df = df.sort_values(sort_by, ascending=sort_by !=
                                "Average", na_position="last")
            st.caption(f"{len(df)} student(s)")
            st.dataframe(df, hide_index=True, width="stretch", column_config={
                "Average": st.column_config.ProgressColumn("Average", min_value=0, max_value=100, format="%.1f"),
            })

    with tab_reg:
        _, mid, _ = st.columns([1, 3, 1])
        with mid:
            with st.form(form_key("stu_reg")):
                st.markdown("##### New student")
                a, b = st.columns(2)
                name = a.text_input(
                    "Full name *", placeholder="e.g. Aarav Sharma", key=form_key("stu_name"))
                roll = b.text_input(
                    "Roll number *", placeholder="e.g. 2026-014", key=form_key("stu_roll"))
                age = a.number_input(
                    "Age *", min_value=3, max_value=100, value=14, step=1, key=form_key("stu_age"))
                email = b.text_input(
                    "Email *", placeholder="name@example.com", key=form_key("stu_email"))
                submitted = st.form_submit_button(
                    "Register student", type="primary", width="stretch")
            if submitted:
                ok, msg = svc.register(
                    name=name, age=age, email=email, roll_no=roll)
                if ok:
                    flash(msg)
                    bump_form()
                    st.rerun()
                else:
                    st.error(msg)

    with tab_prof:
        if not data["Students"]:
            empty_state("👤", "No profiles yet",
                        "Register a student to see their profile here.")
            return
        rolls = [s["roll_no"] for s in data["Students"]]
        roll = st.selectbox("Select student", rolls,
                            format_func=lambda r: f"{svc.find(r)['name']} · {r}")
        info = svc.show_details(roll)
        badge = ('<span class="badge pass">PASSING</span>' if info["passed"]
                 else '<span class="badge fail">BELOW PASS MARK</span>') if info["average"] is not None \
            else '<span class="badge muted">NO GRADES</span>'
        st.markdown(
            f'<div class="profile"><div class="avatar">{html.escape(initials(info["name"]))}</div><div>'
            f'<div class="name">{html.escape(info["name"])}</div>'
            f'<div class="meta">Roll {html.escape(info["roll_no"])} · Age {info["age"]} · {html.escape(info["email"])}</div>'
            f'<div style="margin-top:.5rem">{badge}</div></div></div>',
            unsafe_allow_html=True,
        )
        m1, m2, m3 = st.columns(3)
        m1.metric("Average marks",
                  f"{info['average']:.2f}" if info["average"] is not None else "-")
        m2.metric("Overall grade", info["letter"])
        m3.metric("Subjects", len(info["grades"]))

        if info["grades"]:
            gdf = pd.DataFrame([{"Subject": k, "Marks": v, "Grade": letter(v),
                                 "Status": "Pass" if v >= PASS_MARK else "Fail"} for k, v in info["grades"].items()])
            g1, g2 = st.columns([1, 1])
            g1.dataframe(gdf, hide_index=True, width="stretch", column_config={
                "Marks": st.column_config.ProgressColumn("Marks", min_value=0, max_value=100, format="%.1f")})
            g2.altair_chart(bar_chart(gdf[["Subject", "Marks"]], "Subject", "Marks", height=220).encode(
                y=alt.Y("Marks:Q", scale=alt.Scale(domain=[0, 100]), axis=alt.Axis(title=None))), width="stretch")
        else:
            st.info("No grades recorded yet. Add some from the Grades page.")

        with st.expander("✏️ Edit details"):
            with st.form(f"edit_stu_{roll}"):
                a, b = st.columns(2)
                n = a.text_input("Full name", info["name"], key=f"es_n_{roll}")
                ag = b.number_input("Age", 3, 100, int(
                    info["age"]), key=f"es_a_{roll}")
                em = a.text_input("Email", info["email"], key=f"es_e_{roll}")
                b.text_input("Roll number (cannot be changed)",
                             roll, disabled=True, key=f"es_r_{roll}")
                if st.form_submit_button("Save changes", type="primary"):
                    ok, msg = svc.update(roll, n, ag, em)
                    if ok:
                        flash(msg)
                        st.rerun()
                    else:
                        st.error(msg)
        with st.expander("🗑️ Danger zone"):
            confirm = st.checkbox(
                "I understand this permanently deletes the student and all their grades.", key=f"cd_{roll}")
            if st.button("Delete student", disabled=not confirm, key=f"del_stu_{roll}"):
                svc.remove(roll)
                flash(f"Student {info['name']} deleted.", "🗑️")
                st.rerun()


def page_teachers(data: dict) -> None:
    svc = Teacher(data)
    hero("Teachers", "Manage your teaching staff")
    tab_dir, tab_reg, tab_prof = st.tabs(
        ["📋 Directory", "➕ Register", "👤 Profile"])

    with tab_dir:
        df = teachers_df(data)
        if df.empty:
            empty_state("👩‍🏫", "No teachers yet",
                        "Use the Register tab to add your first teacher.")
        else:
            c1, c2 = st.columns([4, 1.2])
            query = c1.text_input("Search", placeholder="Search by name, employee ID, department or email…",
                                  label_visibility="collapsed", key="t_search")
            c2.download_button("⬇ Export CSV", csv_bytes(
                df), "teachers.csv", "text/csv", width="stretch")
            if query:
                mask = df[["Name", "Employee ID", "Department", "Email"]].apply(
                    lambda col: col.astype(str).str.contains(query, case=False, na=False)).any(axis=1)
                df = df[mask]
            st.caption(f"{len(df)} teacher(s)")
            st.dataframe(df, hide_index=True, width="stretch")

    with tab_reg:
        _, mid, _ = st.columns([1, 3, 1])
        with mid:
            with st.form(form_key("t_reg")):
                st.markdown("##### New teacher")
                a, b = st.columns(2)
                name = a.text_input(
                    "Full name *", placeholder="e.g. Sunita Koirala", key=form_key("t_name"))
                emp = b.text_input(
                    "Employee ID *", placeholder="e.g. EMP-102", key=form_key("t_emp"))
                age = a.number_input(
                    "Age *", min_value=18, max_value=80, value=30, step=1, key=form_key("t_age"))
                email = b.text_input(
                    "Email *", placeholder="name@school.edu", key=form_key("t_email"))
                dept = a.text_input(
                    "Department (optional)", placeholder="e.g. Science", key=form_key("t_dept"))
                submitted = st.form_submit_button(
                    "Register teacher", type="primary", width="stretch")
            if submitted:
                ok, msg = svc.register(
                    name=name, age=age, email=email, emp_id=emp, department=dept)
                if ok:
                    flash(msg)
                    bump_form()
                    st.rerun()
                else:
                    st.error(msg)

    with tab_prof:
        if not data["Teacher"]:
            empty_state("👤", "No profiles yet",
                        "Register a teacher to see their profile here.")
            return
        ids = [t["emp_id"] for t in data["Teacher"]]
        emp = st.selectbox("Select teacher", ids,
                           format_func=lambda i: f"{svc.find(i)['name']} · {i}")
        info = svc.show_details(emp)
        dept = info.get("department") or ""
        dept_badge = f'<span class="badge info">{html.escape(dept)}</span>' if dept else '<span class="badge muted">NO DEPARTMENT</span>'
        st.markdown(
            f'<div class="profile"><div class="avatar">{html.escape(initials(info["name"]))}</div><div>'
            f'<div class="name">{html.escape(info["name"])}</div>'
            f'<div class="meta">ID {html.escape(info["emp_id"])} · Age {info["age"]} · {html.escape(info["email"])}</div>'
            f'<div style="margin-top:.5rem">{dept_badge}</div></div></div>',
            unsafe_allow_html=True,
        )
        with st.expander("✏️ Edit details"):
            with st.form(f"edit_t_{emp}"):
                a, b = st.columns(2)
                n = a.text_input("Full name", info["name"], key=f"et_n_{emp}")
                ag = b.number_input("Age", 18, 80, min(
                    max(int(info["age"]), 18), 80), key=f"et_a_{emp}")
                em = a.text_input("Email", info["email"], key=f"et_e_{emp}")
                dp = b.text_input("Department", dept, key=f"et_d_{emp}")
                if st.form_submit_button("Save changes", type="primary"):
                    ok, msg = svc.update(emp, n, ag, em, dp)
                    if ok:
                        flash(msg)
                        st.rerun()
                    else:
                        st.error(msg)
        with st.expander("🗑️ Danger zone"):
            confirm = st.checkbox(
                "I understand this permanently deletes the teacher record.", key=f"ctd_{emp}")
            if st.button("Delete teacher", disabled=not confirm, key=f"del_t_{emp}"):
                svc.remove(emp)
                flash(f"Teacher {info['name']} deleted.", "🗑️")
                st.rerun()


NEW_SUBJECT = "➕ New subject…"


def marks_key(roll: str, subject: str, current: float | None) -> str:
    # The key must not change while a brand-new subject name is being typed, otherwise the marks reset to 0.
    return f"g_marks_{roll}_{subject}" if current is not None else f"g_marks_{roll}_new"


def save_grade_cb() -> None:
    """Button callback. Reads the *current* widget values from session state (callback args would be
    stale if the user typed a subject and clicked in one go), and can safely reset widget state."""
    ss = st.session_state
    data = load_data()
    roll = ss.get("g_student")
    choice = ss.get("g_subject")
    subject = str(ss.get("g_new_subject", "") if choice ==
                  NEW_SUBJECT else choice or "").strip()
    student = Student(data).find(roll)
    current = student.get("grades", {}).get(subject) if student else None
    key = marks_key(roll, subject, current)
    marks = ss.get(key, ss.get(f"g_marks_{roll}_new", 0.0))
    ok, msg = Student(data).add_grade(roll, subject, float(marks))
    if ok:
        flash(msg)
        # jump to the subject we just saved
        st.session_state["g_subject"] = subject.strip()
        st.session_state.pop("g_new_subject", None)
    else:
        st.session_state["_grade_error"] = msg


def page_grades(data: dict) -> None:
    svc = Student(data)
    hero("Grades", "Record marks and review the class gradebook")
    tab_rec, tab_book = st.tabs(["✍️ Record grade", "📒 Gradebook"])

    with tab_rec:
        if not data["Students"]:
            empty_state("🎓", "No students yet",
                        "Register students first, then record their grades here.")
        else:
            rolls = [s["roll_no"] for s in data["Students"]]
            left, right = st.columns([1, 1.15], gap="large")
            with left:
                st.markdown("##### Add or update a mark")
                roll = st.selectbox(
                    "Student", rolls, format_func=lambda r: f"{svc.find(r)['name']} · {r}", key="g_student")
                student = svc.find(roll)
                existing = sorted(
                    {subj for s in data["Students"] for subj in s.get("grades", {})})
                NEW = NEW_SUBJECT
                options = [*existing, NEW]
                if st.session_state.get("g_subject") not in options:
                    # e.g. last grade of that subject was removed
                    st.session_state.pop("g_subject", None)
                choice = st.selectbox("Subject", options, key="g_subject")
                subject = st.text_input("New subject name", placeholder="e.g. Mathematics",
                                        key="g_new_subject") if choice == NEW else choice
                subject = subject.strip()
                current = student.get("grades", {}).get(subject)
                st.number_input("Marks (0–100)", 0.0, 100.0, float(current) if current is not None else 0.0, 0.5,
                                key=marks_key(roll, subject, current))
                if current is not None:
                    st.caption(
                        f"Existing mark of **{current:g}** will be replaced.")
                st.button("Save grade", type="primary",
                          width="stretch", on_click=save_grade_cb)
                if err := st.session_state.pop("_grade_error", None):
                    st.error(err)
            with right:
                st.markdown(f"##### {student['name']}'s grades")
                grades = student.get("grades", {})
                if not grades:
                    st.caption("No grades recorded yet.")
                for subj, m in grades.items():
                    c1, c2, c3, c4 = st.columns([3, 1.2, 1, 0.8])
                    c1.markdown(f"**{subj}**")
                    c2.markdown(f"{m:g}")
                    c3.markdown(
                        f'<span class="badge {"pass" if m >= PASS_MARK else "fail"}">{letter(m)}</span>', unsafe_allow_html=True)
                    if c4.button("🗑️", key=f"rm_{roll}_{subj}", help=f"Remove {subj}"):
                        svc.remove_grade(roll, subj)
                        flash(f"Removed {subj} for {student['name']}.", "🗑️")
                        st.rerun()
                avg = student_avg(student)
                if avg is not None:
                    st.divider()
                    st.metric(
                        "Average", f"{avg:.2f}", f"Grade {letter(avg)}", delta_color="off")

    with tab_book:
        gdf = gradebook_df(data)
        if gdf.empty:
            empty_state("📒", "Gradebook is empty",
                        "Records will appear here once students are registered.")
        else:
            st.download_button("⬇ Export gradebook CSV", csv_bytes(
                gdf), "gradebook.csv", "text/csv")
            st.dataframe(gdf, hide_index=True, width="stretch", column_config={
                "Average": st.column_config.ProgressColumn("Average", min_value=0, max_value=100, format="%.1f")})


def page_analytics(data: dict) -> None:
    hero("Analytics", "Performance insights across students and subjects")
    sdf = students_df(data)
    graded = sdf.dropna(subset=["Average"])
    if graded.empty:
        empty_state("📊", "Nothing to analyse yet",
                    "Record some grades and insights will appear here.")
        return

    tab_lead, tab_subj, tab_risk = st.tabs(
        ["🏆 Leaderboard", "📚 Subjects", "⚠️ Needs attention"])

    with tab_lead:
        lb = graded.sort_values(
            "Average", ascending=False).reset_index(drop=True)
        medals = ["🥇", "🥈", "🥉"]
        lb.insert(0, "Rank", [medals[i] if i < 3 else str(i + 1)
                  for i in range(len(lb))])
        st.dataframe(lb[["Rank", "Roll No", "Name", "Subjects", "Average", "Grade"]], hide_index=True, width="stretch",
                     column_config={"Average": st.column_config.ProgressColumn("Average", min_value=0, max_value=100, format="%.1f")})

    with tab_subj:
        stats = subject_stats(data)
        c1, c2 = st.columns([1.2, 1])
        c1.dataframe(stats, hide_index=True, width="stretch", column_config={
            "Average": st.column_config.ProgressColumn("Average", min_value=0, max_value=100, format="%.1f"),
            "Pass rate": st.column_config.NumberColumn("Pass rate", format="%.0f%%")})
        with c2:
            section("Distribution of all marks")
            all_marks = pd.DataFrame(
                {"Marks": [m for s in data["Students"] for m in s.get("grades", {}).values()]})
            hist = (alt.Chart(all_marks).mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6, color="#8B5CF6")
                    .encode(x=alt.X("Marks:Q", bin=alt.Bin(step=10), axis=alt.Axis(title=None)),
                            y=alt.Y("count():Q", axis=alt.Axis(title=None))).properties(height=240))
            st.altair_chart(hist, width="stretch")

    with tab_risk:
        rows = []
        for s in data["Students"]:
            failing = {k: v for k, v in s.get(
                "grades", {}).items() if v < PASS_MARK}
            if failing:
                rows.append({"Roll No": s["roll_no"], "Name": s["name"], "Email": s["email"],
                             "Failing subjects": ", ".join(f"{k} ({v:g})" for k, v in failing.items()), "Count": len(failing)})
        if rows:
            st.warning(
                f"{len(rows)} student(s) are below the pass mark ({PASS_MARK:g}) in at least one subject.")
            st.dataframe(pd.DataFrame(rows).sort_values(
                "Count", ascending=False), hide_index=True, width="stretch")
        else:
            st.success(
                "Everyone is at or above the pass mark in every subject. 🎉")


def page_data(data: dict) -> None:
    hero("Data & Backup", "Export your records or restore from a backup")
    c1, c2 = st.columns(2, gap="large")
    with c1:
        st.markdown("##### Download backup")
        st.caption(
            "A complete copy of all students, teachers and grades as JSON.")
        stamp = datetime.now().strftime("%Y%m%d_%H%M")
        st.download_button("⬇ Download School_data.json", json.dumps(data, indent=4).encode("utf-8"),
                           f"School_data_{stamp}.json", "application/json", type="primary")
        st.markdown("##### Export tables")
        e1, e2, e3 = st.columns(3)
        e1.download_button("Students CSV", csv_bytes(students_df(
            data)), "students.csv", "text/csv", width="stretch")
        e2.download_button("Teachers CSV", csv_bytes(teachers_df(
            data)), "teachers.csv", "text/csv", width="stretch")
        e3.download_button("Gradebook CSV", csv_bytes(gradebook_df(
            data)), "gradebook.csv", "text/csv", width="stretch")
    with c2:
        st.markdown("##### Restore from backup")
        st.caption(
            "Replaces ALL current data with the contents of the uploaded file.")
        up = st.file_uploader("Backup file", type="json",
                              label_visibility="collapsed")
        if up is not None:
            try:
                restored = json.loads(up.getvalue().decode("utf-8"))
                valid = isinstance(restored, dict) and isinstance(restored.get(
                    "Students"), list) and isinstance(restored.get("Teacher"), list)
            except (json.JSONDecodeError, UnicodeDecodeError):
                valid = False
            if not valid:
                st.error("That doesn't look like a valid School_data.json backup.")
            else:
                st.info(
                    f"Backup contains {len(restored['Students'])} students and {len(restored['Teacher'])} teachers.")
                ok = st.checkbox(
                    "I understand this replaces all current data.")
                if st.button("Restore backup", disabled=not ok, type="primary"):
                    save_data(restored)
                    flash("Backup restored.", "♻️")
                    st.rerun()


# ----------------------------------------------------------------------------
# App shell
# ----------------------------------------------------------------------------
PAGES = {
    "Dashboard": ("📊", page_dashboard),
    "Students": ("🎓", page_students),
    "Teachers": ("👩‍🏫", page_teachers),
    "Grades": ("📝", page_grades),
    "Analytics": ("📈", page_analytics),
    "Data & Backup": ("💾", page_data),
}


def main() -> None:
    st.session_state.setdefault("page", "Dashboard")
    data = load_data()

    with st.sidebar:
        st.markdown('<div class="brand"><div class="logo">🎓</div><div><div class="text">EduManage</div>'
                    '<div class="tag">School Management System</div></div></div>', unsafe_allow_html=True)
        for name, (icon, _) in PAGES.items():
            st.button(f"{icon}  {name}", key=f"nav_{name}", width="stretch", on_click=goto, args=(name,),
                      type="primary" if st.session_state["page"] == name else "secondary")
        st.divider()
        st.caption(
            f"👥 {len(data['Students'])} students · 👩‍🏫 {len(data['Teacher'])} teachers")
        st.caption(f"Pass mark: {PASS_MARK:g}  ·  v2.0")

    show_flash()
    PAGES[st.session_state["page"]][1](data)


main()
