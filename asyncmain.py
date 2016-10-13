#!/usr/bin/env python
# -*- coding:utf-8 -*-
#  Author: Jason Wang


import tornado.ioloop
import tornado.web
from tornado import httpclient
from tornado.web import asynchronous
from tornado import gen

# import tornado_data_uri.uimodules as md

class MainHandler(tornado.web.RequestHandler):
    @asynchronous
    @gen.coroutine
    def get(self):
        print('start get')
        http = httpclient.AsyncHTTPClient()
        http.fetch("http://127.0.0.1/post/",self.callback)
        self.write('end')

    def callback(self,response):
        print(response.body)


settings = {
    'template_path': 'template',
    'static_path': 'static',
    'static_url_prefix': '/static/',
    # 'ui_modules':md,
}

application = tornado.web.Application([
    (r"/index",MainHandler),
],**settings)


if __name__ == '__main__':
    application.listen(8001)
    tornado.ioloop.IOLoop.instance().start()



