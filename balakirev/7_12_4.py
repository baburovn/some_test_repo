from functools import wraps
s = "1 2 3 4 5"


def decorator(func):
     @wraps(func)
     def wrapper(*args,**kwargs):
          sum_lst = sum(func(*args,**kwargs))
          return sum_lst
     return wrapper

@decorator
def get_list(s):
     '''Функция для формирования списка целых значений'''
     return [int(i) for i in s.split()]

