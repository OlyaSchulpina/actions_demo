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
            self.__available -= 1
            return True
        return False

    def mark_as_returned(self):
        self.__available += 1

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
    def __init__(self, title, author, year, file_size, file_format):
        super().__init__(title, author, year, 999)
        self.__file_size = file_size
        self.__format = file_format

    def get_file_size(self):
        return self.__file_size

    def get_format(self):
        return self.__format

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
        return list(self.__borrowed_books)


class Librarian(User):
    def __init__(self, name):
        super().__init__(name)

    def add_book(self, library, book):
        return library.add_book(book)

    def remove_book(self, library, book):
        return library.remove_book(book)

    def register_user(self, library, user):
        return library.add_user(user)


class Library:
    def __init__(self):
        self.__books = []
        self.__users = []

    def add_book(self, book):
        self.__books.append(book)
        return f"Книга '{book.get_title()}' добавлена в библиотеку"

    def remove_book(self, book):
        if book in self.__books:
            self.__books.remove(book)
            return f"Книга '{book.get_title()}' удалена из библиотеки"
        return "Книга не найдена в библиотеке"

    def add_user(self, user):
        self.__users.append(user)
        return (
            f"Пользователь {user.get_name()} "
            "зарегистрирован в библиотеке"
        )

    def find_book(self, title):
        for book in self.__books:
            if book.get_title().lower() == title.lower():
                return book
        return None

    def find_user(self, name):
        for user in self.__users:
            if user.get_name().lower() == name.lower():
                return user
        return None

    def show_all_books(self):
        print("Все книги в библиотеке:")
        for book in self.__books:
            print(f"  - {book}")

    def show_available_books(self):
        print("Доступные книги:")
        available_found = False
        for book in self.__books:
            if book.is_available():
                print(f"  - {book}")
                available_found = True
        if not available_found:
            print("  Нет доступных книг")

    def lend_book(self, title, user_name):
        book = self.find_book(title)
        user = self.find_user(user_name)

        if not book:
            return f"Книга '{title}' не найдена в библиотеке"
        if not user:
            return f"Пользователь '{user_name}' не зарегистрирован"

        return user.borrow(book)

    def return_book(self, title, user_name):
        book = self.find_book(title)
        user = self.find_user(user_name)

        if not book:
            return f"Книга '{title}' не найдена в библиотеке"
        if not user:
            return f"Пользователь '{user_name}' не зарегистрирован"

        return user.return_book(book)

    # Add methods for testing purposes
    def get_books_count(self):
        return len(self.__books)

    def get_users_count(self):
        return len(self.__users)

    def get_books(self):
        return list(self.__books)