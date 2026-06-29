<div align="center">

# 𝐑𝐀𝐈𝐍𝐁𝐎𝐖 𝐓𝐀𝐁𝐋𝐄

🟥 🟧 🟨 🟩 🟦 🟪

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

| File                   | Description                                                                                         |
| ---------------------- | --------------------------------------------------------------------------------------------------- |
| `hasher.py`            | Reads passwords, computes SHA-256 hashes, generates random salts, and exports the results to Excel. |
| `popularPasswords.txt` | Input dataset containing one password per line.                                                     |
| `hash_salt_demo.xlsx`  | Generated spreadsheet comparing unsalted and salted hashes.                                         |

---

# 📊 Example Output

Each password appears **three times**, once for each randomly generated salt.

| Password    | Clean SHA-256  | Salt   | Salted SHA-256 |
| ----------- | -------------- | ------ | -------------- |
| password123 | Same every run | Random | Different      |
| password123 | Same every run | Random | Different      |
| password123 | Same every run | Random | Different      |

---

## Without a Salt

Every identical password always produces the **exact same SHA-256 hash**.

```
password123
        │
        ▼
ef92b778...
```

Every user with the password `password123` would have the **same stored hash**.

Because the output is deterministic:

* ✅ Duplicate passwords are immediately visible.
* ✅ Attackers can use precomputed Rainbow Tables.
* ✅ Large password databases can be cracked much faster.

---

## With a Random Salt

A random salt is added before hashing.

```
password123 + 7A9F12...
        │
        ▼
6ef31c8b...

password123 + 91D4AB...
        │
        ▼
ef4c2b1a...

password123 + 52C7F9...
        │
        ▼
9db3eac5...
```

Although the password never changes, **every resulting hash is completely different**.

This means:

* Every stored password becomes unique.
* Duplicate passwords are hidden.
* Rainbow Tables become effectively useless.
* Attackers must brute-force each password individually.

---

# 🔒 Why Salting Matters

| Without Salt                                 | With Random Salt                          |
| -------------------------------------------- | ----------------------------------------- |
| Identical passwords produce identical hashes | Every password hash is unique             |
| Duplicate passwords are obvious              | Duplicate passwords are hidden            |
| Rainbow Tables work immediately              | Rainbow Tables become impractical         |
| Fast SHA-256 enables rapid guessing          | Each password must be attacked separately |

---

# ⚡ Modern Password Storage

Although this project uses **SHA-256** for educational purposes, modern applications **should not** store passwords using SHA-256 alone.

Instead, use password hashing algorithms specifically designed to resist brute-force attacks:

* ✅ Argon2id *(recommended)*
* ✅ bcrypt
* ✅ scrypt
* ✅ PBKDF2

These algorithms include:

* Random salts
* Configurable computational cost
* Memory hardness (Argon2id and scrypt)

Unlike SHA-256, they are intentionally slow, making password cracking dramatically more expensive.

---

# ⚙️ Installation

Install the required packages:

```bash
pip install pandas openpyxl
```

Clone the repository.

Place your password list inside:

```
popularPasswords.txt
```

Run the script:

```bash
python hasher.py
```

---

# 📄 Generated Spreadsheet

The Excel output contains the following columns.

| Column        | Description                           |
| ------------- | ------------------------------------- |
| `password`    | Original plaintext password           |
| `clean_hash`  | SHA-256 hash of the original password |
| `salt_id`     | Salt iteration (`Salt #1`–`Salt #3`)  |
| `salt_value`  | Random 32-character hexadecimal salt  |
| `salted_hash` | SHA-256 hash of `password + salt`     |

Each password generates **three rows**, making it easy to compare deterministic hashing with salted hashing.

---

# 🎯 Educational Purpose

This project is intended for:

* Cybersecurity students
* Secure software development courses
* Digital forensics classes
* Cryptography demonstrations
* Password security workshops
* Anyone learning why password salting is essential

It provides a practical demonstration of why modern systems use **unique salts** together with **slow password hashing algorithms** to securely store passwords.

---

<div align="center">

### ⭐ If this project helped you learn something, consider giving it a star!

Made for cybersecurity education and password security demonstrations.

</div>
