import json
from pathlib import Path
import sys

USERS_FILE = Path("users.json")

def load_users():
    if USERS_FILE.exists():
        with USERS_FILE.open("r") as f:
            return json.load(f)
    else:
        print("Users file not found")
        sys.exit(1)
