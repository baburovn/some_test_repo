#lst = [8, 11,-53,2,10,11]
lst = [3,2,6,-1]
len_lst = len(lst)


for i in range(len_lst-1):
    for j in range(i+1,len_lst):
        if lst[i] > lst[j]:
            lst[i] == lst[j]

print(lst)