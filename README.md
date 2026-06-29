<div align="center">

# $${\Huge{\textsf{{\color[rgb]{1,0,0}R}{\color[rgb]{1,0.45,0}A}{\color[rgb]{0.85,0.65,0}I}{\color[rgb]{0,0.7,0}N}{\color[rgb]{0,0.75,0.75}B}{\color[rgb]{0,0.35,1}O}{\color[rgb]{0.45,0,1}W}{\color[rgb]{0.8,0,0.8}~}{\color[rgb]{1,0,0}T}{\color[rgb]{1,0.45,0}A}{\color[rgb]{0.85,0.65,0}B}{\color[rgb]{0,0.7,0}L}{\color[rgb]{0,0.75,0.75}E}}}}$$

<p align="center">
  <img
    src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzY4d3pkeXA1eDJpcnB2b3Rod2k0azF2OXBhNWI3dWhuMXRpZ3V6cCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ZJlesIV8TnabS/giphy.gif"
    width="700"
    alt="Rainbow Table Animation">
</p>

### 🔐 Demonstrating why passwords should **never** be stored as plain SHA-256 hashes.

</div>

---

# 🌈 Rainbow Table Demo

This project demonstrates how password hashing works, why **unsalted hashes are vulnerable to Rainbow Table attacks**, and how **random salts** make precomputed attacks impractical.

Using a dataset of common passwords, the script generates:

* A standard SHA-256 hash for each password
* Three unique salted SHA-256 hashes per password
* An Excel spreadsheet comparing both approaches side by side

The generated spreadsheet makes it easy to visualize how salting completely changes the resulting hash, even when the original password is identical.

---

# 📁 Project Structure

| File                   | Description                                                                                        |
| ---------------------- | -------------------------------------------------------------------------------------------------- |
| `hasher.py`            | Reads passwords, computes SHA-256 hashes, generates random salts, and exports the results to Excel |
| `popularPasswords.txt` | Input dataset containing one password per line                                                     |
| `hash_salt_demo.xlsx`  | Generated output containing the comparison table                                                   |

---

# 📊 Example Output

Each password appears **three times**, once for each randomly generated salt.

| Password    | Clean SHA-256  | Salt   | Salted SHA-256 |
| ----------- | -------------- | ------ | -------------- |
| password123 | Same every run | Random | Different      |
| password123 | Same every run | Random | Different      |
| password123 | Same every run | Random | Different      |

This demonstrates two important properties:

✅ **Without a salt**

* Every identical password always produces the exact same SHA-256 hash.
* Attackers can search massive precomputed Rainbow Tables to recover passwords almost instantly.

❌ Example

```
password123
↓
ef92b778...
```

Every user using **password123** would have exactly the same stored hash.

---

✅ **With a random salt**

```
password123 + 7A9F12...
↓
6ef31c8b...

password123 + 91D4AB...
↓
ef4c2b1a...

password123 + 52C7F9...
↓
9db3eac5...
```

Even though the password never changed, every resulting hash is completely different.

This makes Rainbow Tables effectively useless because an attacker would need to generate a brand-new table for every unique salt.

---

# 🔒 Why Salting Matters

Without salting:

* Identical passwords have identical hashes
* Rainbow Tables work immediately
* Large password databases can be cracked efficiently

With salting:

* Every stored password becomes unique
* Duplicate passwords are hidden
* Rainbow Tables become computationally infeasible
* Attackers must brute-force each password individually

---

# ⚡ Modern Password Storage

While this project uses **SHA-256** for educational purposes, modern applications **should not** store passwords using SHA-256 alone.

Instead, use dedicated password hashing algorithms designed to be intentionally slow:

* Argon2id *(recommended)*
* bcrypt
* scrypt
* PBKDF2

These algorithms combine:

* Random salts
* Configurable computational cost
* Memory hardness (Argon2 and scrypt)

Together they dramatically increase the cost of password cracking compared to fast cryptographic hashes like SHA-256.

---

# ⚙️ Installation

```bash
pip install pandas openpyxl
```

Clone the repository and place your password list in:

```
popularPasswords.txt
```

Run:

```bash
python hasher.py
```

---

# 📄 Generated Spreadsheet

The output Excel file contains the following columns:

| Column        | Description                          |
| ------------- | ------------------------------------ |
| `password`    | Original plaintext password          |
| `clean_hash`  | SHA-256 of the original password     |
| `salt_id`     | Salt iteration (Salt #1–3)           |
| `salt_value`  | Random 32-character hexadecimal salt |
| `salted_hash` | SHA-256 of `password + salt`         |

Each password produces three rows, allowing direct comparison between deterministic hashing and salted hashing.

---

# 🎯 Educational Purpose

This project is intended for:

* Cybersecurity students
* Digital forensics courses
* Secure software development classes
* Password security demonstrations
* Cryptography fundamentals

It provides a practical demonstration of why password salting is essential and why modern password hashing algorithms remain the industry standard.
