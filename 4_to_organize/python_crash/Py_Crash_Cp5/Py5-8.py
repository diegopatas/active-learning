# Program Hello admin
users = ['glau', 'flor', 'ste', 'thiago', 'admin']
for i in users:
    if i == 'admin':
        print(f"Hello {i.title()}, would you like to see a status report?")
    else:
        print(f"Hello {i.title()}, thank you for logging in again!")
users = ['admin']

if users:
    print("Ok, we still have some users!")
else:
    print("We ran out of users!")