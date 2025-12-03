import pytest
from your_library_module import (Book, PrintedBook, EBook, User, Librarian, Library)

class TestBook:
    def test_book_init(self):
        book = Book("Test Book", "Test Author", 2020, 5)
        assert book.get_title() == "Test Book"
        assert book.get_author() == "Test Author"
        assert book.get_year() == 2020
        assert book.get_available_count() == 5
        assert book.is_available() is True [file:1]

    def test_book_mark_as_taken_success(self):
        book = Book("Test Book", "Test Author", 2020, 1)
        result = book.mark_as_taken()
        assert result is True
        assert book.get_available_count() == 0
        assert book.is_available() is False [file:1]

    def test_book_mark_as_taken_fail(self):
        book = Book("Test Book", "Test Author", 2020, 0)
        result = book.mark_as_taken()
        assert result is False
        assert book.get_available_count() == 0 [file:1]

    def test_book_mark_as_returned(self):
        book = Book("Test Book", "Test Author", 2020, 0)
        book.mark_as_returned()
        assert book.get_available_count() == 1
        assert book.is_available() is True [file:1]

class TestPrintedBook:
    def test_printed_book_init(self):
        book = PrintedBook("War and Peace", "Tolstoy", 1869, 1225, "хорошая")
        assert book.get_title() == "War and Peace"
        assert book.get_pages() == 1225
        assert book.get_condition() == "хорошая"
        assert book.get_available_count() == 1 [file:1]

    def test_printed_book_repair(self):
        book = PrintedBook("Crime", "Dostoevsky", 1866, 480, "плохая")
        book.repair()
        assert book.get_condition() == "хорошая" [file:1]

class TestEBook:
    def test_ebook_init(self):
        book = EBook("Master", "Bulgakov", 1966, 5, "epub")
        assert book.get_title() == "Master"
        assert book.get_file_size() == 5  # assuming getter exists or access via reflection
        assert book.get_format() == "epub"
        assert book.get_available_count() == 999 [file:1]

    def test_ebook_download(self):
        book = EBook("Master", "Bulgakov", 1966, 5, "epub")
        result = book.download()
        assert result == "Книга 'Master' загружена" [file:1]

class TestUser:
    def test_user_borrow_success(self):
        book = PrintedBook("Test Book", "Author", 2020, 100, "хорошая")
        user = User("Test User")
        result = user.borrow(book)
        assert "взята" in result
        assert len(user.get_borrowed_books()) == 1 [file:1]

    def test_user_borrow_fail(self):
        book = PrintedBook("Test Book", "Author", 2020, 100, "хорошая")
        user = User("Test User")
        user.borrow(book)  # borrow first
        result = user.borrow(book)  # try again
        assert "недоступна" in result [file:1]

    def test_user_return_book(self):
        book = PrintedBook("Test Book", "Author", 2020, 100, "хорошая")
        user = User("Test User")
        user.borrow(book)
        result = user.return_book(book)
        assert "возвращена" in result
        assert len(user.get_borrowed_books()) == 0 [file:1]

    def test_user_return_not_borrowed(self):
        book = PrintedBook("Test Book", "Author", 2020, 100, "хорошая")
        user = User("Test User")
        result = user.return_book(book)
        assert "нет книги" in result [file:1]

class TestLibrary:
    def setup_method(self):
        self.lib = Library()
        self.b1 = PrintedBook("Война и мир", "Толстой", 1869, 1225, "хорошая")
        self.b2 = EBook("Мастер и Маргарита", "Булгаков", 1966, 5, "epub")
        self.user1 = User("Анна")

    def test_add_book(self):
        result = self.lib.add_book(self.b1)
        assert "добавлена" in result
        assert len(self.lib._Library__books) == 1  # note: private access for testing [file:1]

    def test_remove_book(self):
        self.lib.add_book(self.b1)
        result = self.lib.remove_book(self.b1)
        assert "удалена" in result
        assert len(self.lib._Library__books) == 0 [file:1]

    def test_find_book(self):
        self.lib.add_book(self.b1)
        found = self.lib.find_book("Война и мир")
        assert found is not None
        assert found.get_title() == "Война и мир" [file:1]

    def test_lend_book_success(self):
        librarian = Librarian("Мария")
        librarian.add_book(self.lib, self.b1)
        librarian.register_user(self.lib, self.user1)
        result = self.lib.lend_book("Война и мир", "Анна")
        assert "взята" in result [file:1]

    def test_lend_book_not_found(self):
        result = self.lib.lend_book("Nonexistent", "Анна")
        assert "не найдена" in result [file:1]

    def test_return_book_success(self):
        librarian = Librarian("Мария")
        librarian.add_book(self.lib, self.b1)
        librarian.register_user(self.lib, self.user1)
        self.lib.lend_book("Война и мир", "Анна")
        result = self.lib.return_book("Война и мир", "Анна")
        assert "возвращена" in result [file:1]

class TestLibrarian:
    def test_librarian_add_book(self):
        lib = Library()
        book = PrintedBook("Test", "Author", 2020, 100, "хорошая")
        librarian = Librarian("Test Librarian")
        result = librarian.add_book(lib, book)
        assert "добавлена" in result [file:1]

    def test_librarian_register_user(self):
        lib = Library()
        user = User("Test User")
        librarian = Librarian("Test Librarian")
        result = librarian.register_user(lib, user)
        assert "зарегистрирован" in result [file:1]
