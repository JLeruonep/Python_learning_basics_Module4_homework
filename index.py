from dataset import users, countries
from pprint import pprint

pprint(users)
# pprint(countries)

# Вариант:
# users_wrong_passwords = []
#
# for user in users:
#    if user['password'].isdigit():
#        users_wrong_passwords.append({'name': user['name'], 'mail': user['mail']})

users_wrong_passwords = [{'name': user['name'], 'mail': user['mail']} for user in users if user['password'].isdigit()]
girls_drivers = [user['friends']['sex'] for user in users]  # FIXME
pprint(girls_drivers)
# print(users_wrong_passwords)
# and user[1]['friends'][0]['cars']
# if user[1]['friends'][0]['sex'] == 'F'