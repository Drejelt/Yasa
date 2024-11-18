class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}
        self.authors = {}

    def new_book(self, name: str, year: int, author):
        if author.name not in self.authors:
            self.authors[author.name] = author
        book = Book(name, year, author)
        self.books[name] = book
        author.books[name] = book
        return book

    def group_by_author(self, author):
        if isinstance(author, Author):
            author_name = author.name
        elif isinstance(author, str):
            author_name = author
        else:
            raise ValueError("Автор должен быть объектом Author или строкой с именем.")

        return [str(book) for book in self.books.values() if book.author.name == author_name]

    def group_by_year(self, year: int):
        return [str(book) for book in self.books.values() if book.year == year]

    def __str__(self):
        return f"Библиотека '{self.name}' содержит {len(self.books)} книг и {len(self.authors)} авторов."


class Book:
    total_books = 0

    def __init__(self, name: str, year: int, author):
        self.name = name
        self.year = year
        if not isinstance(author, Author):
            raise ValueError("Автор должен быть экземпляром класса Author.")
        self.author = author
        Book.total_books += 1

    def __str__(self):
        return f"'{self.name}' авторства {self.author.name} ({self.year})"


class Author:
    def __init__(self, name: str, country: str, birthday: str):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = {}

    def __str__(self):
        return f"{self.name} ({self.country}, родился {self.birthday})"


library = Library("Всякая шизофрения") #Имя библиотеки, указал для примера.
#Авторы, можно указать любых если следовать синтаксису.
author1 = Author("Десмонд Джон Моррис", "Великобритания", "1928-01-24")
author2 = Author("Джордж Оруэлл", "Великобритания", "1903-06-25")

book1 = library.new_book("Голая обезьяна", 1967, author1)
book2 = library.new_book("1984", 1949, author2)
book3 = library.new_book("Биология искусства: исследование художественного поведения человекообразных обезьян и его связи с человеческим искусством", 1967, author1) #По факту год выпуска книги 1964, но я для проверки сортировки указал 1967
print(library)
print(author1)
print(author2)
print(library.group_by_author(author1))
print(library.group_by_author("Десмонд Джон Моррис"))
print(library.group_by_year(1967))
