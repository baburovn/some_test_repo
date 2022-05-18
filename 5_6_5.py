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
    for j in range(len(lst_in)):
        if i < len(lst_in)-1 and lst_in[i][j] == 1 and lst_in[i+1][j] == 1:
            #print("i=",i,"j=", j,"DA")
            flag ="НЕТ"
            break
        if j < len(lst_in)-1 and lst_in[i][j] == 1 and lst_in[i][j+1] == 1:
            #print("i=",i,"j=", j,"DA")
            flag = "НЕТ"
            break

        if j < len(lst_in)-1 and i < len(lst_in)-1 and lst_in[i][j] == 1 and lst_in[i+1][j+1] == 1:
            #print("i=",i,"j=", j,"DA")
            flag = "НЕТ"
            break


print(flag if flag == "НЕТ" else "ДА")
