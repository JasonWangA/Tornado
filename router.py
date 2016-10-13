#!/usr/bin/env python
# -*- coding:utf-8 -*-
#  Author: Jason Wang


import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class StoryHandler(tornado.web.RequestHandler):
    def get(self, story_id):
        self.write("You requested the story " + story_id)

class BuyHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("buy.wupeiqi.com/index")

application = tornado.web.Application([
    (r"/index", MainHandler),
    (r"/story/([0-9]+)", StoryHandler),
])

application.add_handlers('buy.wupeiqi.com$', [
    (r'/index',BuyHandler),
])

if __name__ == "__main__":
    application.listen(8002)
    tornado.ioloop.IOLoop.instance().start()
