# Program to check usernames
current_users = ['flor', 'gabriel', 'malaquias', 'admin']
new_users = ['flor', 'Gabriel', 'ivone', 'paty']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"This username {new_user} is not available.")
    else:
        print(f"Ok, this username {new_user} is available.")