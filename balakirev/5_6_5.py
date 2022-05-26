import sys

# считывание списка из входного потока
lst_in = [[1,0,0,0,0],
          [0,0,0,0,1],
          [0,0,1,0,0],
          [0,0,1,0,0],
          [1,0,0,0,1]]

#нарисуем матрицу для наглядности
# print(" ", end="   j=")
# for i in range(len(lst_in)):
#     print(i, end="  ")
#
# print()
# for i,v in enumerate(lst_in):
#     print("i=",i,v)
flag = "ДА"

#айдем позиции 1, сверим с рисунком
for i in range(len(lst_in)):
    for j in range(i + 1, len(lst_in)):
       if lst_in[i][j] != lst_in[j][i]:
           flag = "НЕТ"

print(flag)