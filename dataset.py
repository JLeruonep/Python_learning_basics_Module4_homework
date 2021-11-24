import http.client
import json
from pprint import pprint

RANDOM_DATA = False  # Если True - данные каждый раз будут разными


conn = http.client.HTTPSConnection('pumpskill.ru')
conn.request('GET', f'/cases/api/python-basic/users-and-friends/{"?r=0" if not RANDOM_DATA else ""}')
response = conn.getresponse()
data = json.loads(response.read().decode('utf-8'))

users = data['users']
countries = data['countries']

us = [{'mail': 'ljubov_41@mail.ru',
  'name': 'Орест Ефстафьевич Зуев',
  'password': '7589652',
  'sex': 'M',
  'username': 'galkinaolimpiada'},
 {'friends': [{'job': {'occupation': 'Юрист', 'salary': 22131},
               'mail': 'miron00@mail.ru',
               'name': 'Евдокия Федоровна Харитонова',
               'sex': 'F'},
              {'cars': [{'Category': 'Pickup',
                         'Make': 'Dodge',
                         'Model': 'Ram 2500 Club Cab',
                         'Year': 1999}],
               'flights': [{'airport': 'Pierre-Elliott-Trudeau',
                            'city': 'Dorval',
                            'country': 'Canada'},
                           {'airport': 'Cheju International airport',
                            'city': 'Jeju-Si',
                            'country': 'South Korea'},
                           {'airport': 'New Incheon International airport',
                            'city': 'Incheon',
                            'country': 'South Korea'}],
               'job': {'occupation': 'Нарколог', 'salary': 11321},
               'mail': 'mefodigurev@hotmail.com',
               'name': 'Зыкова София Иосифовна',
               'sex': 'F'}],
  'mail': 'efimovsamson@mail.ru',
  'name': 'Королев Вадим Егорович',
  'password': '2r805T7',
  'sex': 'M',
  'username': 'zikovaevpraksija'},
 {'friends': [{'flights': [{'airport': 'Tokyo International airport',
                            'city': 'Tokyo',
                            'country': 'Japan'}],
               'job': {'occupation': 'Упаковщик', 'salary': 18743},
               'mail': 'xkalinina@hotmail.com',
               'name': 'Кира Борисовна Щербакова',
               'sex': 'F'}],
  'mail': 'leonid85@yandex.ru',
  'name': 'Быков Мина Еремеевич',
  'password': '75Gq7',
  'sex': 'M',
  'username': 'budimir1976'}]
