lst_in = ['django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya', 'marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya']
lst = []
for i, value in enumerate(lst_in):
    while value.count("  "):
        value = value.replace("  "," ")

    lst_in[i] = value

    while value.count(" "):
        value = value.replace(" ","-")
    lst_in[i] = value

    print(lst_in[i])

#print(*lst_in end="\n")