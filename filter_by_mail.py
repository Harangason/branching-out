import json
import sys
import re
from pathlib import Path

USERS_FILE = Path("users.json")

def load_users():
    if USERS_FILE.exists():
        with USERS_FILE.open("r") as f:
            return json.load(f)
    else:
        print("Users file not found")
        sys.exit(1)

def save_users(users):
    with USERS_FILE.open("w") as f:
        json.dump(users, f, indent=2)
    return users

EMAIL_REGEX = re.compile(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')

def filter_by_mail(users, name_parts):
    results = []

    for user in users:
        email = user["email"].lower()

        # Prüfe, ob ALLE Teile im Email-Local-Part vorkommen
        if all(part in email for part in name_parts):
            results.append(user)

    return results
