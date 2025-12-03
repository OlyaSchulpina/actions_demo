class Book:
    def __init__(self, title, author, year, available):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__available = available

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__year

    def is_available(self):
        return self.__available > 0

    def get_available_count(self):
        return self.__available

    def mark_as_taken(self):
        if self.__available > 0:
            self.__available = self.__available - 1
            return True
        return False

    def mark_as_returned(self):
        self.__available = self.__available + 1

    def __str__(self):
        return (
            f"Книга: '{self.__title}', автор: {self.__author}, "
            f"год: {self.__year}, доступно: {self.__available}"
        )


class PrintedBook(Book):
    def __init__(self, title, author, year, pages, condition):
        super().__init__(title, author, year, 1)
        self.__pages = pages
        self.__condition = condition

    def get_pages(self):
        return self.__pages

    def get_condition(self):
        return self.__condition

    def repair(self):
        if self.__condition == "плохая":
            self.__condition = "хорошая"

    def __str__(self):
        return (
            "Печатная книга: "
            f"'{self.get_title()}', автор: {self.get_author()}, "
            f"год: {self.get_year()}, страниц: {self.__pages}, "
            f"состояние: {self.__condition}"
        )


class EBook(Book):
    def __init__(self, title, author, year, file_size, format_):
        super().__init__(title, author, year, 999)
        self.__file_size = file_size
        self.__format = format_

    def download(self):
        return f"Книга '{self.get_title()}' загружена"

    def __str__(self):
        return (
            "Электронная книга: "
            f"'{self.get_title()}', автор: {self.get_author()}, "
            f"год: {self.get_year()}, размер: {self.__file_size}MB, "
            f"формат: {self.__format}"
        )


class User:
    def __init__(self, name):
        self.__name = name
        self.__borrowed_books = []

    def get_name(self):
        return self.__name

    def borrow(self, book):
        if book.mark_as_taken():
            self.__borrowed_books.append(book)
            return f"Книга '{book.get_title()}' взята"
        return f"Книга '{book.get_title()}' недоступна"

    def return_book(self, book):
        if book in self.__borrowed_books:
            book.mark_as_returned()
            self.__borrowed_books.remove(book)
            return f"Книга '{book.get_title()}' возвращена"
        return f"У пользователя нет книги '{book.get_title()}'"

    def show_books(self):
        if not self.__borrowed_books:
            print(f"У пользователя {self.__name} нет книг")
        else:
            print(f"Книги пользователя {self.__name}:")
            for book in self.__borrowed_books:
                print(f"  - {book.get_title()}")

    def get_borrowed_books(self):
        return self.__borrowed_books


class Librarian(User):
    def __init__(self, name):
        super().__init
