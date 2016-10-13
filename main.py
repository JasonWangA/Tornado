#!/usr/bin/env python
# -*- coding:utf-8 -*-
#  Author: Jason Wang


import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html",list_info = [11,22,33])
        # self.write("Hello,Jason")
settings = {
    'static_path':'static',
    # 'static_url_prefix':  '/static/'
}
application = tornado.web.Application([
    (r"/index",MainHandler)
],**settings)



if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()