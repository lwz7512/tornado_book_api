import json


class Book:

    def __init__(self):
        self.books = []
        self.id = 0  # current book id, initially 0

    # get new book id
    def generate_id(self):
        self.id += 1
        return self.id

    def add_book(self, title, author, description=''):
        new_book = {}
        new_book["ID"] = self.generate_id()
        new_book["Title"] = title
        new_book["Author"] = author
        new_book["Description"] = description

        self.books.append(new_book)
        print("Book: {0}".format(new_book))
        return json.dumps(new_book)

    def del_book_by_id(self, id):
        book_index = -1
        for idx, book in enumerate(self.books):
            if book["ID"] == int(id): # conver to number
                book_index = idx
        if book_index == -1:
            return False
        else:
            del self.books[book_index]  # delete the element
            return True

    def update_book_by(self, id, title, author, description):
        found = False
        for book in self.books:
            if book["ID"] == int(id): # conver to number
                book["Title"] = title or book["Title"]
                book["Author"] = author or book["Author"]
                book["Description"] = description or book["Description"]
                found = True
                print(">>> book {0} updated!".format(id))
        return found

    def del_book(self, title):
        found = False
        for idx, book in enumerate(self.books):
            if book["Title"] == title:
                found = True
                del self.books[idx]
        print("books: {0}".format(json.dumps(self.books)))
        return found

    def get_all_books(self):
        return self.books

    def json_list(self):
        return json.dumps(self.books)
