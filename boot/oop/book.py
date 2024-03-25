class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        for item in self.books:
            if item.title == book.title and item.author == book.author:
                self.books.remove(item)

    def search_books(self, search_string):
        elem = search_string.lower()
        search_list = []
        for item in self.books:
            item_title = item.title.lower()
            item_author = item.author.lower()
            if elem in item_title.split() or elem in item_author.split():
                search_list.append(item)
        return search_list
