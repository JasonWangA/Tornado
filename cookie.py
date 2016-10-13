#!/usr/bin/env python
# -*- coding:utf-8 -*-
#  Author: Jason Wang


import tornado.ioloop
import tornado.web

class BaseHandler(tornado.web.RequestHandler):

    def get_current_user(self):
        return self.get_secure_cookie("login_user")

class MainHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        login_user = self.current_user
        self.write(login_user)



class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.current_user

        self.render('login.html', **{'status': ''})

    def post(self, *args, **kwargs):

        username = self.get_argument('name')
        password = self.get_argument('pwd')
        if username == 'wupeiqi' and password == '123':
            self.set_secure_cookie('login_user', '武沛齐')
            self.redirect('/')
        else:
            self.render('login.html', **{'status': '用户名或密码错误'})

settings = {
    'template_path': 'template',
    'static_path': 'static',
    'static_url_prefix': '/static/',
    'cookie_secret': 'aiuasdhflashjdfoiuashdfiuh',
    'login_url': '/login'
}

application = tornado.web.Application([
    (r"/index", MainHandler),
    (r"/login", LoginHandler),
], **settings)


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()