from functools import wraps
#ингредиент-декоратор
def pomidor(meat):
    def lavash(*args):
         print("Помидор")
         meat(*args)
         print("Помидор")
    return lavash

def one_more_d(ogurec):

     def shawerma(meat):
         def lavash(*args):
              print(ogurec)
              meat(*args)
              print(ogurec)
         return lavash
     return shawerma

@one_more_d(ogurec="Огурчик")
@pomidor
def myaso(ingredients):
     print(ingredients)




#nachinka2()



#s = input()
s = "5 6 3 6 -4 6 -1"

def one_more_decor(start):
     def decorator(func):
          def wrapper(*args):
               summa = func(*args)
               return summa + start
          return wrapper
     return decorator

@one_more_decor(start=5)
def str_to_int(s):
     int_sum = sum([int(i) for i in s.split()])
     return int_sum

print(str_to_int(s))