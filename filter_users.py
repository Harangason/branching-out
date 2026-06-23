import json
import pathlib
import sys
import re
from os import name

import filter_by_mail as filter_mail


BASE_DIR = pathlib.Path(__file__).resolve().parent
USERS_FILE = BASE_DIR / "users.json"
USERS = json.load(USERS_FILE.open())



def load_users():
    if USERS_FILE.exists():
        USERS = json.load(USERS_FILE.open())
    else:
        print("Users file not found")
        sys.exit(1)
    return USERS

def save_users(users):
    json.dump(users, USERS_FILE.open("w"))
    users = load_users()
    return users

def user_input():
    name = []
    user_mail = input("Enter the user's email: ").strip().lower()
    local, domain = user_mail.split("@")
    parse_mail = re.split(r"[a-zA-Z0-9]+", local)
    print(f"{parse_mail[0]}@{parse_mail[1]}")
    sonderzeichen = re.findall(r"[a-zA-Z0-9]+", local)
    for i in range(len(sonderzeichen)):
        name.append(parse_mail[i])
    return name


def get_filter_by_email():
    filter_by_mail(user_input())
    filtered_users = filter_mail.filter_by_mail(USERS["users"])
    save_users(
        {
            "users": filtered_users,
        }
    )
    return filtered_users



def main():

    get_filter_by_email()

    return

if __name__ == "__main__":
    main()
