import re



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


EMAIL_REGEX = re.compile(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')

def filter_by_mail(emails):
    return [email for email in emails if EMAIL_REGEX.match(email)]