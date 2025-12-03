import unittest


class TestBook(unittest.TestCase):
    def test_book_creation(self):
        book = Book("Title", "Author", 2023, 3)
        self.assertEqual(book.get_title(), "Title")
        self.assertEqual(book.get_available_count(), 3)

    def test_mark_as_taken(self):
        book = Book("Title", "Author", 2023, 2)
        self.assertTrue(book.mark_as_taken())
        self.assertEqual(book.get_available_count(), 1)

    def test_mark_as_returned(self):
        book = Book("Title", "Author", 2023, 0)
        book.mark_as_returned()
        self.assertEqual(book.get_available_count(), 1)


class TestPrintedBook(unittest.TestCase):
    def test_printed_book_creation(self):
        pb = PrintedBook("Title", "Author", 2023, 300, "хорошая")
        self.assertEqual(pb.get_pages(), 300)
        self.assertEqual(pb.get_condition(), "хорошая")

    def test_repair(self):
        pb = PrintedBook("Title", "Author", 2023, 300, "плохая")
        pb.repair()
        self.assertEqual(pb.get_condition(), "хорошая")


class TestEBook(unittest.TestCase):
    def test_ebook_creation(self):
        eb = EBook("Title", "Author", 2023, 5.5, "PDF")
        self.assertEqual(eb.get_format(), "PDF")
        self.assertEqual(eb.get_available_count(), 999)

    def test_download(self):
        eb = EBook("Title", "Author", 2023, 5.5, "PDF")
        self.assertIn("загружена", eb.download())


class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User("John")
        self.assertEqual(user.get_name(), "John")

    def test_borrow_and_return(self):
        user = User("John")
        book = Book("Title", "Author", 2023, 1)

        result = user.borrow(book)
        self.assertIn("взята", result)

        result = user.return_book(book)
        self.assertIn("возвращена", result)


class TestLibrary(unittest.TestCase):
    def test_add_and_find_book(self):
        library = Library()
        book = Book("Title", "Author", 2023, 1)

        library.add_book(book)
        found = library.find_book("Title")
        self.assertEqual(found.get_title(), "Title")

    def test_lend_and_return_book(self):
        library = Library()
        book = Book("Title", "Author", 2023, 1)
        user = User("John")

        library.add_book(book)
        library.add_user(user)

        result = library.lend_book("Title", "John")
        self.assertIn("взята", result)

        result = library.return_book("Title", "John")
        self.assertIn("возвращена", result)


if __name__ == "__main__":
    unittest.main()