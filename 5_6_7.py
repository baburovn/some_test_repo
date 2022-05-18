n= 6
lst =[]
for i in range(1,6):
    lst.append([1]*i)
for i in range(len(lst)):
    for j in range(0, i - 1):
        lst[i][j + 1] = lst[i - 1][j] + lst[i - 1][j + 1]

for r in lst:
    print(*r)

print(lst)