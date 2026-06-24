def filter_by_mail(users, name_parts):
    results = []

    for user in users:
        email = user["email"].lower()

        # Prüfe, ob ALLE Teile im Email-Local-Part vorkommen
        if all(part in email for part in name_parts):
            results.append(user)
    return results