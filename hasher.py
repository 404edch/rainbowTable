import hashlib
import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
passwords_file = os.path.join(script_dir, 'popularPasswords.txt')
output_file = os.path.join(script_dir, 'hash_salt_demo.xlsx')

data = []

with open(passwords_file, 'r', encoding='utf-8-sig') as f:
    for line in f:
        password = line.strip()
        if not password:
            continue

        clean_hash = hashlib.sha256(password.encode()).hexdigest()

        for i in range(3):
            salt = os.urandom(16).hex()
            salted_hash = hashlib.sha256((password + salt).encode()).hexdigest()
            data.append({
                'password': password,
                'clean_hash': clean_hash,
                'salt_id': f"Salt #{i+1}",
                'salt_value': salt,
                'salted_hash': salted_hash
            })

df = pd.DataFrame(data)
df.to_excel(output_file, index=False, sheet_name='Demo')
print(f"Done! {len(df)} rows saved to hash_salt_demo.xlsx")