# 2 завдання. Написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей.
import random

def get_numbers_ticket(min, max, quantity):
    population = list()
    your_num = list()
    if min >= 1 and max <= 1000:
         if min < max and max - min >= quantity:
            for i in range(min, max+1):
                population.append(i)
            your_num = random.sample(population, quantity)
            print(f'Ваші лотерейні числа:{sorted(your_num)}')
            return sorted(your_num)
         else:
              print(your_num )
              return your_num
           
    else: 
          print(your_num)
          return your_num
          
get_numbers_ticket(3, 50, 10)