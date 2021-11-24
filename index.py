from dataset import users, countries
from pprint import pprint


pprint(users)
# pprint(countries)

# Вариант c алгоритмом:
# users_wrong_passwords = []
#
# for user in users:
#    if user['password'].isdigit():
#        users_wrong_passwords.append({'name': user['name'], 'mail': user['mail']})

# Генератор:
# Формируем словарь по ключам имени и почты, если пароль пользователя состоит только из чисел
# users_wrong_passwords = [{'name': user['name'], 'mail': user['mail']} for user in users
#                          if user['password'].isdigit()]


# Вариант с алгоритмом:
# Единственное - есть вопрос: правильно ли я достал 'cars'? На первый взгляд все работает,
# но если в списке будет больше двух словарей - тогда имя друга в выборку не попадет.
# Другого способа как подобраться к 'cars' в т.ч. с использованием метода get() я не придумал #TODO Попробовать: "list".index("искомое")
# girls_drivers = []
# for friend in users:
#     if 'friends' in friend and friend['friends'][0]['sex'] == 'F' and 'cars' in friend['friends'][-1]:
#         girls_drivers.append(friend.get('friends')[0].get('name'))

# Генератор:
# Получаем значение 'name' из полученного массива значений 'friends'
# При условии, что 'friends' вообще есть в словаре, пол друга женский и друг владел машиной
# girls_drivers = [friend.get('friends')[0].get('name') for friend in users
#              if 'friends' in friend and friend['friends'][0]['sex'] == 'F' and 'cars' in friend['friends'][-1]]
#
# print(girls_drivers)
