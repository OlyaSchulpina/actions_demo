class Book:
    def __init__(self,title, author, year,available):
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
        return self.__available

    def mark_as_taken(self):
        self.__available = self.__available - 1

    def mark_as_returned(self):
        self.__available = self.__available + 1

    def __str__(self):
        return "Book class"

class PrintedBook(Book):
    def __init__(self, pages, condition):
        self.__pages = pages
        self.__condition = condition
    def repair(self):
        if self.__condition == "плохая":
            self.__condition = "хорошая"


class EBook(Book):
    def __init__(self,file_size,format):
        self.__file_size = file_size
        self.__format = format
    def download(self,book):
        return f"Книга {book.get_title()} загружена"


class User:
    def __init__(self,name):
        self.__name = name
        self.__borrowed_books = []

    def borrow(self,book):
        book.mark_as_taken()
        self.__borrowed_books.append(book)
        return f" Книга '{book.get_title()}' взята"

    def return_book(self,book):
        book.mark_as_returned()
        self.__borrowed_books.remove(book)
        return f" Книга '{book.get_title()}' возвращена"

    def show_books(self):
        print(self.__borrowed_books)

    def get_borrowed__books(self):
        return self.__borrowed_books

class Librarian(User):
    def add_book(self,library,book):
        self.__books.append(book)
    def remove_book(self,library,book):
        self.__books.remove(book)
    def register_user(self, library, user):
        self.__users.append(user)

class Library:
    def __int__(self):
        self.__books = []
        self.__users = []

    def add_book(self,book):
        self.__books.append(book)

    def remove_book(self,book):
        self.__books.remove(book)

    def add_user(self,user):
        self.__users.append(user)

    def find_book(self,title):
        return title in self.__books

    def show_all_books(self):
        return self.__books

    def show_available_books(self):
        for b in self.__books:
            if self.is_available()>0:
                return b

    def lend_book(self,title,user):
        book = find_book(title)
        user.borrow(book)

    def return_book(self,title,user):
        book = find_book(title)
        user.return_book(book)

if __name__ == '__main__':
    lib = Library()

    # --- создаём книги ---
    b1 = PrintedBook("Война и мир", "Толстой", 1869, 1225, "хорошая")
    b2 = EBook("Мастер и Маргарита", "Булгаков", 1966, 5, "epub")
    b3 = PrintedBook("Преступление и наказание", "Достоевский", 1866, 480, "плохая")

    # --- создаём пользователей ---
    user1 = User("Анна")
    librarian = Librarian("Мария")

    # --- библиотекарь добавляет книги ---
    librarian.add_book(lib, b1)
    librarian.add_book(lib, b2)
    librarian.add_book(lib, b3)

    # --- библиотекарь регистрирует пользователя ---
    librarian.register_user(lib, user1)

    # --- пользователь берёт книгу ---
    lib.lend_book("Война и мир", "Анна")

    # --- пользователь смотрит свои книги ---
    user1.show_books()

    # --- возвращает книгу ---
    lib.return_book("Война и мир", "Анна")

    # --- электронная книга ---
    b2.download()

    # --- ремонт книги ---
    b3.repair()
    print(b3)
