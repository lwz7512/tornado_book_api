import tornado.web
import json


class AddHandler(tornado.web.RequestHandler):
    def initialize(self, books):
        self.books = books
        
    def get(self):
        title = self.get_argument('title')
        author = self.get_argument('author')
        result = self.books.add_book(title, author)
        self.set_status(200)
        self.write(result)
        self.finish()

    def post(self):
        print('>>> got book:')
        if self.request.body is not None:
            parameters = json.loads(self.request.body)
            print(parameters)
            self.books.add_book(parameters['title'], parameters['author'])
        self.set_status(200)
        self.write(self.books.json_list())
        self.finish()