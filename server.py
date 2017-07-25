#!/usr/bin/python
# import tornado
# from tornado.ioloop import IOLoop
# from tornado.wsgi import WSGIContainer
# from tornado.httpserver import HTTPServer
# from tornado.web import FallbackHandler, RequestHandler, Application

# class MainHandler(RequestHandler):
#   def get(self):
#     self.write("Powered by Tornado")

# tr = WSGIContainer(backend_app)

# application = Application([
#     (r"/tornado", MainHandler),
#     (r".*", FallbackHandler, dict(fallback=tr)),
#     ], cookie_secret="SECRET_DE_FOU_2349882034823")

# if __name__ == "__main__":
#   server = HTTPServer(application)
#   server.bind(80)
#   server.start(0)
#   IOLoop.current().start()

import tornado
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from app import app

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(5000)
IOLoop.instance().start()
