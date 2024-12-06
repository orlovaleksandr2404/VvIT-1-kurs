def text(filename,type):
    if type == 1: #весь файл
        with open(filename,encoding='utf-8') as file:
            content = file.read()
            return content
    elif type == 2:
        lines = [] #построчное
        with open(filename,encoding='utf-8') as file:
            for line in file:
                lines.append(line)
        return lines
    else:
        return 'введен неверный тип'
print(text('example.txt',int(input('введите тип(1 или 2):'))))
