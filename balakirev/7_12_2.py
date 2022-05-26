from functools import wraps
s = "Декораторы - это классно!"


def params(tag):
     def to_tag(tagged):
         @wraps(tagged)
         def wrapper(*args,**kwargs):
             in_tag = f"<{tag}>{tagged(*args,**kwargs)}</{tag}>"
             return in_tag

         return wrapper
     return to_tag

@params(tag="div")
def str_to_lower(s):
     return s.lower()

print(str_to_lower(s))
print(f"Имя функции: {str_to_lower.__name__}")