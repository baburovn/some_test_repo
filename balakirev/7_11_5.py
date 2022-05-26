# str1 = input()
# str2 = input()
str1 = "house river tree car"
str2 = "дом река дерево машина"
import ast
# str1 = str1.split()
#
# str2 = str2.split()



def deco_merge(str_merge):

     def wrapper(*args, **kwargs):
         print(dict(zip(str_merge(str1,str2)[0],str_merge(str1,str2)[1])))
         #return ({str_merge(str1,str2)[i]:str_merge(str1,str2)[i+1] for i in range(0,8,3)})

     return wrapper

@deco_merge
def str_merge(str1,str2):
    str1 = str1.split()
    str2 = str2.split()
    return [str1] + [str2]

d = str_merge(str1,str2)
#print(d)



