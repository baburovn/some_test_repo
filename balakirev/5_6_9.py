n = 4
lst =[[0 if i!=j else 1 for i in range(n)] for j in range(n)]
for i in range(len(lst)):
    print(*lst[i])
