import re
import filter_by_mail as filter_mail

USERS = load_users()   # <--- FEHLTE!

def user_input() -> list:
    user_name = []
    user_mail = input("Enter the user's email: ").strip().lower()

    if "@" not in user_mail:
        print('Invalid email address: missing "@" symbol')
        return None

    local, domain = user_mail.split("@", 1)

    # Deine Regex war falsch: sie entfernt ALLE Buchstaben/Zahlen
    # Du willst aber an Sonderzeichen splitten
    parts = re.split(r"[.,_-]", local)

    # Debug-Ausgabe
    print(f"{parts}")

    return parts


def filter_by_mail(user_name) -> list:
    return filter_mail.filter_by_mail(USERS["users"], user_name)


def main():
    names = user_input()
    if names is None:
        return
    print(filter_by_mail(names))


if __name__ == "__main__":
    main()
