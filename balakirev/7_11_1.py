some_str = input()


def lst_sorted(get_list):

    def wrapper(some_str):
        lst = get_list(some_str)
        return sorted(lst)

    return wrapper


@lst_sorted
def get_list(some_str):
    str_lst = [int(i) for i in some_str.split()]
    return str_lst


lst = get_list(some_str)
print(*lst)
