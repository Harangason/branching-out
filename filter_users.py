import re

from load_users import load_users
import filter_by_mail as filter_mail

USERS = load_users()
VALID_FILTERS = ("name", "age", "email")


def filter_by_name(users, name):
    search_name = name.strip().lower()
    return [
        user
        for user in users
        if search_name in user.get("name", "").lower()
    ]


def filter_by_age(users, age):
    try:
        search_age = int(age)
    except ValueError:
        print("Invalid age: please enter a number")
        return None

    results = []
    for user in users:
        try:
            if int(user.get("age")) == search_age:
                results.append(user)
        except (TypeError, ValueError):
            continue

    return results


def get_email_parts(email):
    user_mail = email.strip().lower()

    if "@" not in user_mail:
        print('Invalid email address: missing "@" symbol')
        return None

    local, domain = user_mail.split("@", 1)
    parts = re.split(r"[.,_-]+", local)
    return [part for part in parts if part]


def filter_by_email(users, email):
    email_parts = get_email_parts(email)
    if email_parts is None:
        return None

    return filter_mail.filter_by_mail(users, email_parts)


def choose_filter():
    print("Choose a filter: name, age, email")
    filter_type = input("Filter by: ").strip().lower()

    if filter_type not in VALID_FILTERS:
        print("Invalid filter type")
        return None

    return filter_type


def filter_users(users):
    filter_type = choose_filter()
    if filter_type is None:
        return None

    search_value = input(f"Enter the user's {filter_type}: ").strip()
    if not search_value:
        print("Search value cannot be empty")
        return None

    if filter_type == "name":
        return filter_by_name(users, search_value)

    if filter_type == "age":
        return filter_by_age(users, search_value)

    return filter_by_email(users, search_value)


def main():
    filtered_users = filter_users(USERS["users"])
    if filtered_users is None:
        return
    name = filtered_users[0].get("name")
    age = filtered_users[0].get("age")
    email = filtered_users[0].get("email")

    print(f"Name: {name}, Age: {age}, EMAIL: {email}")


if __name__ == "__main__":
    main()
