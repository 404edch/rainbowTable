![Alt Text](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzY4d3pkeXA1eDJpcnB2b3Rod2k0azF2OXBhNWI3dWhuMXRpZ3V6cCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ZJlesIV8TnabS/giphy.gif)
# 🔐 Password Hashing & Salting Demo

Demonstrates SHA-256 hashing with and without salting applied to a list of common passwords, exporting the results to a structured Excel table for side-by-side comparison.

---

## 📁 Files

| File | Description |
|---|---|
| `hasher.py` | Reads passwords from the `.txt` file, computes a clean SHA-256 hash and 3 unique salted hashes per password, and exports everything to Excel |
| `popularPasswords.txt` | Input — one password per line, used as the dataset |
| `hash_salt_demo.xlsx` | Output — generated on run, contains the full comparison table |

---

## 📊 Output Table

Each password produces 3 rows (one per salt).

| Column | Content |
|---|---|
| `password` | Original plaintext password |
| `clean_hash` | SHA-256 of the raw password — **identical** across all 3 rows for the same password |
| `salt_id` | Salt iteration label (Salt #1, #2, #3) |
| `salt_value` | Randomly generated 32-char hex salt for this row |
| `salted_hash` | SHA-256 of `password + salt` — **unique** every row, even for identical passwords |

---

## ⚙️ Setup

```bash
pip install pandas openpyxl
```

Place `hasher.py` and `popularPasswords.txt` in the same folder, then:

```bash
python hasher.py
```

`hash_salt_demo.xlsx` will be created in the same folder.
