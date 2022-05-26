lst = list(map(int, input().split()))
if lst[0] != lst[-1]:
    lst.append(True)
else: lst.append(False)

print(*lst)
