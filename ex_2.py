# 2 завдання. Написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей.
import random

def get_numbers_ticket(min, max, quantity):
    new_list = list()
    if min >= 1 and max <= 1000:
         if min < max and max - min > quantity:
            while quantity != 0:
                 n = random.randrange(min, max)
                 new_list.append(n)
                 quantity -= 1
            print(f'Ваші лотерейні числа:{new_list}')
            return new_list
         else:
              print(new_list)
              return new_list 
           
    else: 
          print(new_list)
          return new_list
          
get_numbers_ticket(1, 40, 3)
 