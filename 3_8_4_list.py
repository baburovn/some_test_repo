

def my_decorator(get_sq):

    def wrapper(*args,**kwargs):
        print("i am inside foo")
        get_sq(*args,**kwargs)


    return wrapper


@my_decorator
def get_sq(width, height):
    print(width * height)

get_sq(5,5)