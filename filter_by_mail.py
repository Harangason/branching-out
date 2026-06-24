import re

EMAIL_REGEX = re.compile(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')

def filter_by_mail(emails):
    return [email for email in emails if EMAIL_REGEX.match(email)]