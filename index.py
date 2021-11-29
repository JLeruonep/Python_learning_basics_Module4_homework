from dataset import users, countries
from pprint import pprint

# pprint(users)
#   Point 1

# Вариант c алгоритмом:
users_wrong_password = []

for user in users:
    if user['password'].isdigit():
        users_wrong_password.append({'name': user['name'], 'mail': user['mail']})

# # Генератор:
# # Формируем словарь по ключам имени и почты, если пароль пользователя состоит только из чисел
# users_wrong_password = [{'name': user['name'], 'mail': user['mail']} for user in users
#                         if user['password'].isdigit()]

#   Point 2

# Единственное - есть вопрос: правильно ли я достал 'cars'? На первый взгляд все работает,
# но если в списке будет больше двух словарей - тогда имя друга в выборку не попадет.
# Другого способа как подобраться к 'cars' в т.ч. с использованием метода get() я не придумал

# Вариант с алгоритмом:
# girls_drivers = []
# for user in users:
#     friends = user.get('friends', [])
#     for friend in friends:
#         if friend['sex'] == 'F' and friend.get('cars'):
#             girls_drivers.append(friend['name'])
# #
# girls_drivers.sort()
# print(girls_drivers)
# Генератор:
# Получаем значение 'name' из полученного массива значений 'friends'
# При условии, что 'friends' вообще есть в словаре, пол друга женский и друг владел машиной

girls_drivers = [friend['name'] for user in users for friend in user.get('friends', [])
                 if friend['sex'] == 'F' and friend.get('cars')]

#   Point 3

max_salary = {
    'occupation': 'none',
    'salary': 0
}
for user in users:
    if 'friends' in user:  # Проверяем, чтобы в списке лежал словарь с ключом 'friends'
        if user['friends'][0]['job']['salary'] > max_salary['salary']:
            max_salary = {'occupation': user['friends'][0]['job']['occupation'],
                          'salary': user['friends'][0]['job']['salary']}

#   Point 4

sum_salaries = {

}

for user in users:
    if 'friends' in user:
        friends_salaries = 0
        for friend in user['friends']:
            friends_salaries += friend['job']['salary']
        sum_salaries[user['name']] = friends_salaries
vip_user = max(sum_salaries, key=sum_salaries.get)

#   Point 5

friends_with_cars = 0
flights_count = 0

# Для каждого пользователя смотрим, чтобы у него были друзья, а у друзей - машины.
# Считаем количество друзей с машинами, считаем сколько было полетов у таких друзей
for user in users:
    if 'friends' in user and 'cars' in user['friends'][-1]:
        friends_with_cars += 1
        if 'flights' in user['friends'][-1]:
            flights_count += len(user['friends'][-1]['flights'])
avg_flights = round(flights_count / friends_with_cars, 5)

#   Point 6

for user in users:
    user_delete = False
    if 'friends' in user and 'flights' in user['friends'][-1]:
        for flight in user['friends'][-1]['flights']:
            for country in countries:
                if country in flight.values():
                    user_delete = True
    if user_delete is True:
        user.clear()
