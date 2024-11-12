a=str(input('Введите 1 строку '))#Ввод двух строк
b=str(input('Введите 2 строку '))
c=False
if(len(a)==len(b)):#проверка равенства длины строк
    for i in range(len(a)):#проверка на аннаграмму
        if(a[i] in b):
            c=True
        i+=1
if(c):                            #вывод
    print('Строчки аннаграмы')
if(c==False):
    print('Строки разные')
