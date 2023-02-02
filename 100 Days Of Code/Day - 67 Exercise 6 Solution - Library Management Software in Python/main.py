class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBooks(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def showInfo(self):
        print(f"The library has {self.noBooks} books")
        print(f"The books are ")
        for book in self.books:
            print(book)

l1 = Library()
l1.addBooks("Harry Potter 1")
l1.addBooks("Harry Potter 1")
l1.addBooks("Harry Potter 1")
l1.showInfo()