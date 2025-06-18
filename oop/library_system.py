class Book:
    def __init__(self, title:str, author:str):
        self.title = title
        self.author = author
class EBook(Book):
    def __init__(self, file_size:int,title, author):
        self.file_size = file_size
        super().__init__(title, author)
class PrintBook(Book):
    def __init__(self, title, author,page_count:int):
        self.page_count =page_count
        super().__init__(title, author)
class Library:
    def __init__(self):
    
        self.books =[]
    def add_book(self,book):
        self.book = book
        self.books.append(book)
    def remove_book(self, title: str):
        """Removes a book by title."""
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Removed '{title}' from {self.name}.")
                return
        print(f"Book '{title}' not found.")
    
    def list_books(self):
        """Prints all books (works for all subclasses due to polymorphism)."""
        print(f"\nBooks in {self.books}:")
        for book in self.books:
            print(f"- {book}")  # Calls __str__ of each book type
        print()
