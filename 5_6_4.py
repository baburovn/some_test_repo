n = 17
dic = {}
count = 0
for i in range(2, n):
    for j in range(2,n):
        #print("i=",i,"j=",j)
        if i % j == 0 and i != j:
            count += 1

        if count == 1:
            dic.update({i:count})
            count = 0

for i in range(2,17) :
    if i not in dic.keys():
        print(i, end=" ")