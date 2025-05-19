class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")

book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

book1.display_info()
book2.display_info()

print(f"Total books: {Book.total_books}")
