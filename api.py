import signal
import tornado.ioloop
import tornado.web
from book import Book
from addhandler import AddHandler
from delhandler import DelHandler
from gethandler import GetHandler
from updateHandler import UpdateHandler

books = Book()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Book Microservice v1")

def make_app():
    return tornado.web.Application([
        (r"/v1", MainHandler),
        (r"/v1/addbook", AddHandler, dict(books = books)),
        (r"/v1/delbook/([A-Za-z0-9]+)", DelHandler, dict(books = books)),
        (r"/v1/getbooks", GetHandler, dict(books = books)),
        (r"/v1/updatebook/([A-Za-z0-9]+)", UpdateHandler, dict(books = books)),
    ])

async def shutdown():
    tornado.ioloop.IOLoop.current().stop()
    print('<<< server stopped!')

def exit_handler(sig, frame):
    print('>>> to stop server...')
    tornado.ioloop.IOLoop.instance().add_callback_from_signal(shutdown)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print('>>> starting server...')
    signal.signal(signal.SIGTERM, exit_handler)
    signal.signal(signal.SIGINT,  exit_handler)
    tornado.ioloop.IOLoop.current().start()
