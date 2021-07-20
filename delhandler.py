import tornado.web
import json


class DelHandler(tornado.web.RequestHandler):
    def initialize(self, books):
        self.books = books
        
    def get(self):
        title = self.get_argument('title')
        result = self.books.del_book(title)
        if result:
            self.write("Deleted book title: {0} succsessfully".format(title))
            self.set_status(200)
        else:
            self.write("Book '{0}' not found".format(title))
            self.set_status(404)

    def delete(self, id):
        result = self.books.del_book_by_id(id)
        if result:
            self.write("Deleted book title: {0} succsessfully".format(id))
            self.set_status(200)
        else:
            self.write("Book '{0}' not found".format(id))
            self.set_status(404)
