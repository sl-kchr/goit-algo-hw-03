
# 1 завдання. Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.
from datetime import datetime

def get_days_from_today(date):
    now = datetime.now()

    try:
         new_date = datetime.strptime(date, '%Y-%m-%d')
         difference = now.date() - new_date.date()
         print(difference.days)
         return difference.days


    except ValueError:
        print('Нажаль ці данні неможливо оборобти.', '\n''Введіть двту в правильному форматі "РРРР-ММ-ДД"')
get_days_from_today('2020-10-08')


