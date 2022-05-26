a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]]

lst =[[a[i], int(a[i+1])] for i in range(0,len(a)-1,2)]

print(lst)
