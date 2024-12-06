def describe_person(name,age=30):
    if age == '' :
        return 'Имя: ' + name + ', возраст: 30'
    else:
        return 'Имя: ' + name + ', возраст: ' + str(age)
uname = input('введите имя:')
uage = input('введите возраст:')
print(describe_person(uname,uage))
