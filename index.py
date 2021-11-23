from dataset import users, countries
from pprint import pprint


pprint(users)
# pprint(countries)

for user in users:
    if 'name' in user and 'password'.isdigit() in user:
        print(user.keys())

# users_wrong_passwords = [{'name': name['name'] for name in users if name['password'].isdigit()},
                        # {'mail': mail['mail'] for mail in users if mail['password'].isdigit()}]
# print(users_wrong_passwords)
