t = ["– Скажи-ка, дядя, ведь не даром",
    "Я Python выучил с каналом",
    "Балакирев что раздавал?",
    "Ведь были ж заданья боевые,",
    "Да, говорят, еще какие!",
    "Недаром помнит вся Россия",
    "Как мы рубили их тогда!"
    ]



#kk = [t[x].split() for x in range(len(t)) ]
zz = [[x for x in row if len(x) > 3 ] for row in [t[x].split() for x in range(len(t)) ]]
print(zz)

