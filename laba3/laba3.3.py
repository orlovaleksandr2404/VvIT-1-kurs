def text(filename,type):
    try:
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
            return 'Неверный тип чтения'
    except FileNotFoundError:
        return f'ошибка {filename} не найден'
print(text(input('введите название файла:'),int(input('введите тип(1 или 2):'))))