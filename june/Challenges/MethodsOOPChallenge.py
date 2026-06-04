# Stores a list of books
# add_book(title) — adds a book
# __len__ — returns number of books
# __contains__ — checks if a book is in the library
# __str__ — prints "Library: 3 books"
# __getitem__ — lets you access books by index
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, title):
        self.books.append({ "title": title})
    def __len__(self):
        return len(self.books)
    def __contains__(self, title):
        return any(i["title"] == title for i in self.books)
    def __str__(self):
        total = len(self.books)
        return f"Library: {total} books"
    def __getitem__(self, index):
        return self.books[index]

lib = Library()
lib.add_book("Python Crash Course")
lib.add_book("Clean Code")
lib.add_book("The Pragmatic Programmer")

print(len(lib))                         # 3
print("Clean Code" in lib)              # True
print("Harry Potter" in lib)            # False
print(lib[0])                           # Python Crash Course
print(lib)                              # Library: 3 books