string1 = input('Введите 1 строку ')#Ввод двух строк
string2 = input('Введите 2 строку ')
parametr = False
if(len(string1)==len(string2)):#проверка равенства длины строк
        for i in string1:#проверка на аннаграмму
            if i in string2:
                parametr=True
if(parametr):                            #вывод
    print('Строчки аннаграмы')
else:
    print('Строки разные')
