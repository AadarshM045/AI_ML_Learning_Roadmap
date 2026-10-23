# 04 — NumPy

> First step into data science — learning to work with arrays, matrices, and numerical operations the fast way.

---

## 📂 Notebooks

| File | Topics |
|------|--------|
| [`phase-1.ipynb`](./phase-1.ipynb) | Array creation, vectors, matrices, tensors, array properties, reshaping |
| [`phase-2.ipynb`](./phase-2.ipynb) | Indexing, slicing, filtering, fancy indexing, `np.where()`, combining & deleting arrays |
| [`phase-3.ipynb`](./phase-3.ipynb) | Real business analysis — Zomato sales data, aggregations, dot product, vectorized operations |

---

## 🧠 What You'll Learn

### Phase 1 — Array Basics
- `np.zeros()`, `np.ones()`, `np.full()` — creating arrays filled with a value
- `np.random.random()` — random arrays
- `np.arange(start, stop, step)` — sequences like Python's `range()` but as arrays
- Vectors (1D), Matrices (2D), Tensors (3D) — and how to create each
- Array properties — `.shape`, `.ndim`, `.dtype`, `.size`
- `.reshape()` — change dimensions without changing data
- `.flatten()` vs `.ravel()` — both flatten to 1D, but `ravel()` returns a view, `flatten()` returns a copy
- `.T` — transpose (flip rows and columns)

### Phase 2 — Indexing & Manipulation
- 1D slicing — `arr[1:3]`, `arr[1:7:2]` (with steps)
- 2D indexing — `arr[row, col]`, `arr[1]` (whole row), `arr[:, 2]` (whole column)
- `np.sort()` — sorting arrays
- Boolean filtering — `arr[arr % 2 == 0]` — filter directly with a condition
- Mask filtering — same result, but condition stored in a variable first
- Fancy indexing — `arr[[2, 4, 7]]` — pick elements by index list
- `np.where(condition)` — returns indices where condition is True
- `np.where(condition, x, y)` — like an if/else applied to every element
- `np.concatenate()` — joining arrays
- `np.vstack()` / `np.hstack()` — add rows or columns to a 2D array
- `np.delete()` — remove elements by index
- Shape compatibility check — `np.shape(a) == np.shape(b)`

### Phase 3 — Real Data Analysis
- `np.sum(axis=0)` — sum down columns (per year)
- `np.sum(axis=1)` — sum across rows (per restaurant)
- `np.min()`, `np.max()`, `np.mean()` with `axis=` — aggregations on real data
- `np.cumsum()` — running total
- `np.dot()` — dot product of two vectors
- `np.vectorize()` — apply any Python function to every element of an array
- Array arithmetic — `/12` on a whole 2D array gives monthly averages instantly

---

## 💡 Key Concepts in Practice

```python
import numpy as np

# ── Creating arrays ───────────────────────────────────
zeros  = np.zeros((3, 4))        # 3 rows, 4 cols of 0.0
ones   = np.ones((3, 4))         # 3 rows, 4 cols of 1.0
full   = np.full((3, 4), 5)      # 3 rows, 4 cols of 5
random = np.random.random((3,4)) # values between 0 and 1
seq    = np.arange(0, 11, 3)     # [0, 3, 6, 9]

# ── Shapes ────────────────────────────────────────────
vector = np.array([3, 5, 7])                          # 1D
matrix = np.array([[3, 5, 6], [6, 3, 6]])             # 2D
tensor = np.array([[[3,4],[5,6]], [[6,7],[7,3]]])     # 3D

# ── Properties ───────────────────────────────────────
arr.shape   # (2, 2)
arr.ndim    # 2
arr.dtype   # int64
arr.size    # 4

# ── Reshape & Transpose ──────────────────────────────
arr.reshape(3, 2)   # change shape — total elements must stay the same
arr.flatten()       # always a copy
arr.ravel()         # view (faster, shares memory with original)
arr.T               # transpose — rows become columns

# ── Slicing ───────────────────────────────────────────
arr[1:3]            # elements at index 1 and 2
arr[1:7:2]          # every 2nd element from index 1 to 6
arr_2d[2, 1]        # row 2, column 1
arr_2d[1]           # entire row 1
arr_2d[:, 2]        # entire column 2

# ── Filtering ─────────────────────────────────────────
even = arr[arr % 2 == 0]              # direct boolean filter
mask = arr % 2 == 0                   # same, stored as mask
even = arr[mask]

# ── np.where ─────────────────────────────────────────
np.where(arr > 5)                     # returns indices where True
np.where(arr > 6, arr * 10, arr * 5) # if/else on every element

# ── Combining & removing ──────────────────────────────
np.concatenate((arr1, arr2))          # join 1D arrays
np.vstack((matrix, new_row))          # add a row
np.hstack((matrix, new_col))         # add a column
np.delete(arr, 5)                     # remove element at index 5

# ── Aggregations with axis ────────────────────────────
np.sum(data, axis=0)    # sum each column
np.sum(data, axis=1)    # sum each row
np.mean(data[:, 1:], axis=1)   # mean of columns 1+ per row
monthly = sales_data[:, 1:] / 12     # divide every value — no loop needed

# ── Dot product & vectorize ───────────────────────────
np.dot(v1, v2)                        # sum of element-wise products
np.vectorize(str.upper)(names_array)  # apply Python function to whole array
```

---

## 🖥️ Sample Output — Phase 3 (Zomato Analysis)

```
======= Zomato Sales Analysis =======
Data Shape: (5, 5)

Per Year Sale:  [     15  810000  945000 1085000 1240000]
Restro Sale:    [800001 610002 990003 900004 780005]

Min Sales per Restaurant: [150000 120000 200000 180000 160000]
Max Sales per Year:       [200000 230000 260000 300000]
Avg Sales per Restaurant: [200000. 152500. 247500. 225000. 195000.]

Monthly Average:
 [[12500.  15000.  18333.  20833.]
  [10000.  11666.  13333.  15833.]
  [16666.  19166.  21666.  25000.]
  [15000.  17500.  20000.  22500.]
  [13333.  15416.  17083.  19166.]]
```

---

## ▶️ How to Run

```bash
# Install dependencies
pip install numpy jupyter

# Open notebooks
jupyter notebook
```

Or open directly in VS Code with the Jupyter extension.

---

*Part of the [AI/ML Learning Roadmap](../README.md)*
