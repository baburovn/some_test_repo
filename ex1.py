import os
print(os.getcwd())
file = open('text_file.txt')
counter = 0
for i in file.readlines():
    counter +=1
    print(f"Строка №{counter} {i}", end="")