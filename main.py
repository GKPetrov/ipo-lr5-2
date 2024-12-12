string1 = input('Введите 1 строку ')#Ввод двух строк
string2 = input('Введите 2 строку ')
parametr = True
if(len(string1)==len(string2)):#проверка равенства длины строк
    for i in range(len(string2)):#проверка на аннаграмму
        if string1[i] == string2[len(string2)-i-1]:
            pass
        else:
            parametr=False
if(parametr):                            #вывод
    print('Строчки аннаграмы')
else:
    print('Строки разные')
