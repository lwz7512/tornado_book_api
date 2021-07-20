import tornado.web
import json

# http://localhost:8888/v1/updatebook?id=1&title=test&author=lwz7512&description=mybook

class UpdateHandler(tornado.web.RequestHandler):
    def initialize(self, books):
        self.books = books
        
    def get(self):
        id = self.get_argument('id')
        title = self.get_argument('title')
        author = self.get_argument('author')
        description = self.get_argument('description')
        result = self.books.update_book_by(id, title, author, description)
        if result:
            self.write("Update book title: {0} succsessfully".format(title))
            self.set_status(200)
        else:
            self.write("Book '{0}' not found".format(title))
            self.set_status(404)

    def put(self, id):
      if self.request.body is not None:
            parameters = json.loads(self.request.body)
            self.books.update_book_by(
              id,
              parameters['title'],
              parameters['author'],
              parameters['description']
            )
      self.set_status(200)
      self.write(self.books.json_list())
      self.finish()