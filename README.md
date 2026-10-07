# 🤖 AI / ML Learning Roadmap

A public learning journal — everything I study on my journey from Python basics to Machine Learning, documented one project at a time.

---

## 📁 Repository Structure

```
AI_ML_Learning_Roadmap/
├── 01_Python/                        ✅ Complete
│   ├── 01_Basics_Variables_Math/
│   ├── 02_Conditionals/
│   ├── 03_Functions/
│   ├── 04_Loops/
│   ├── 05_Strings/
│   ├── 06_Files/
│   ├── 07_Lists/
│   └── 08_Dictionaries_Tuples/
├── 02_Api_Projects/                  ✅ Complete
│   ├── 01_Weather/
│   │   ├── main.py
│   │   └── README.md
│   └── 02_mood_journal/
│       ├── mood_journal.py
│       └── README.md
├── 03_web_scraping/
├── 04_Numpy/                         🔄 On going
│   ├── phase-1.ipynb
│   ├── phase-2.ipynb
│   └── phase-3.ipynb
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🗺️ Roadmap

### ✅ Phase 1 — Python Fundamentals
> Variables, control flow, functions, loops, strings, file I/O, lists, dictionaries

📂 [Go to Python →](./01_Python/README.md)

| Folder | Topics |
|--------|--------|
| [01 — Basics, Variables & Math](./01_Python/01_Basics_Variables_Math/README.md) | Variables, arithmetic, input, f-strings |
| [02 — Conditionals](./01_Python/02_Conditionals/README.md) | `if/elif/else`, comparison operators, `random` |
| [03 — Functions](./01_Python/03_Functions/README.md) | `def`, return values, `__name__ == "__main__"` |
| [04 — Loops](./01_Python/04_Loops/README.md) | `for`, `while`, `break`, `continue` |
| [05 — Strings](./01_Python/05_Strings/README.md) | String methods, slicing, `string` module |
| [06 — Files](./01_Python/06_Files/README.md) | `open()`, read/write/append, `datetime` |
| [07 — Lists](./01_Python/07_Lists/README.md) | `.append()`, `.pop()`, `enumerate()`, `sum()` |
| [08 — Dictionaries & Tuples](./01_Python/08_Dictionaries_Tuples/README.md) | Nested dicts, `.items()`, `sorted()`, `max()` |

---

### ✅ Phase 2 — Python Applied (API Projects)
> Building real programs that talk to the internet using live APIs

📂 [Go to API Projects →](./02_Api_Projects/README.md)

| Folder | Topics |
|--------|--------|
| [01 — Weather App](./02_Api_Projects/01_Weather/README.md) | `requests`, Geocoding API, OpenWeatherMap, API keys, nested JSON |
| [02 — Mood Journal](./02_Api_Projects/02_mood_journal/README.md) | Advice Slip API, `json` file I/O, `datetime`, functions as dict values |

---

### 🔄 Phase 3 — Data Science Foundations
> Learning to work with data using the core data science libraries

📂 [Go to NumPy →](./04_Numpy/README.md)

| Folder | Topics |
|--------|--------|
| [NumPy](./04_Numpy/README.md) | Arrays, matrices, tensors, indexing, filtering, aggregations, real data analysis |
| Pandas | Data manipulation and analysis — *coming soon* |
| Matplotlib / Seaborn | Data visualisation — *coming soon* |

---

### 🔜 Phase 4 — Machine Learning
- [ ] Scikit-learn — Classification, regression, clustering
- [ ] Model evaluation and tuning
- [ ] Feature engineering

---

### 🔜 Phase 5 — Deep Learning
- [ ] Neural networks
- [ ] TensorFlow / PyTorch

---

## 🙌 Why This Repo?

Learning in public keeps me accountable and might help someone else on the same path. Every project here is something I built while studying — working through it myself, not copied.

Feel free to browse, fork, or open an issue if you spot a bug or have a suggestion!

---

## 💻 Requirements

- Python 3.6 or higher
- Phase 1 — standard library only, no installs needed
- Phase 2 — `pip install requests`
- Phase 3 — `pip install numpy jupyter`

```bash
# Verify Python version
python3 --version

# Run any Phase 1 script
python3 01_Python/01_Basics_Variables_Math/01_Calculator.py

# Run a Phase 2 project
python3 02_Api_Projects/01_Weather/main.py

# Open Phase 3 notebooks
jupyter notebook
```

---

## 👤 Author

**Aadarsh M**
- GitHub: [@AadarshM045](https://github.com/AadarshM045)
- Repository: [AI_ML_Learning_Roadmap](https://github.com/AadarshM045/AI_ML_Learning_Roadmap)

---

## 📄 License

This project is licensed under the terms in the [LICENSE](./LICENSE) file.