a = input('напишите текст для добавления в файл')
with open('user_input.txt','a',encoding='utf-8') as file:
    file.write('\n'+a)
print('____добавлено____')
with open('user_input.txt', encoding='utf-8') as file:
    content = file.read()
    print(content)