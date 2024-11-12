a=str(input('Введите 1 строку '))
b=str(input('Введите 2 строку '))
c=False
if(len(a)==len(b)):
    for i in range(len(a)):
        if(a[i] in b):
            c=True
        i+=1
if(c):
    print('Строчки аннаграмы')
if(c==False):
    print('Строки разные')
