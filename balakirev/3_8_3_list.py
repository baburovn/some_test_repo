str_lst = "+7(xxx)xxx-xx-xx"
lst = [i for i in str_lst if i not in ("+","-")]
lst[0] = "8"
print("".join(lst))