class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        return f'Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}'
Book1 = Book('Стихи',"Пушкин",1829)
Book2 = Book(input('введите название'),input('введите автора'),int(input('введите год')))
print(Book1.get_info())