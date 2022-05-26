t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

s = 'Декораторы - это круто!'



def upper_dec(chars):
     def decorator(foo):
          def wrapper(*args,**kwargs):
               print("i worked:\n")
               chr_s = foo(*args,**kwargs)
               for i in chr_s:
                    if i in chars:
                         chr_s = chr_s.replace(i,"-").replace("---","-").replace("--","-")
               return chr_s
          return wrapper
     return decorator



@upper_dec(chars=" !?")
def cyr_to_lat(s):
     s = s.lower()
     s_new = ""
     for i in s:
          if i in t.keys():
               s_new += t[i]
          else: s_new += i
     return s_new

print(cyr_to_lat(s))