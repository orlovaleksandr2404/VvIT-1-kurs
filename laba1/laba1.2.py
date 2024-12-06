n1=input('введите число1:')
n2=input('введите число2:')
if n1.isdigit() and n2.isdigit():
    if int(n1)>int(n2):
        print("большее число =",n1)
    elif n1 == n2:
        print('числа равны')
    else:
        print('большее число =',n2)
else:
    print('ошибка')