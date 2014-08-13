#!/usr/bin/env python
# -*- coding: utf8 -*-
# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


import os.path
import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import sys
sys.path.append('..')
from db import db
import json

from tornado.options import define, options
DB=db.db()
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/",get_imagelist),
            (r"/Get/image", get_image),
            (r"/Get/imagelist", get_imagelist),
            (r"/Post/image", change_image),
            (r"/Put/image", create_iamge),
            (r"/Delete/image",delete_iamge ),
        ]
        tornado.web.Application.__init__(self,handlers)

class get_imagelist(tornado.web.RequestHandler):
    def get(self):
        entries = DB.listAllImage()
        if not entries:
            self.redirect("/no image")
        else:    
             self.write(json.dumps(entries, ensure_ascii=False))


class get_image(tornado.web.RequestHandler):
    def get(self, image_id):                                          
        entry = DB.selectByXXX('name',image_id)
        if not entry: raise tornado.web.HTTPError(404)
        else:
            self.write(json.dumps(entry, ensure_ascii=False))


class change_image(tornado.web.RequestHandler):
    def put(self,image_id,choice,value):
        entry = DB.updateByXXX(choice,image_id,value)
        self.write(entry)


class create_iamge(tornado.web.RequestHandler):
    def put(self,name,system,size,version,description):
            li={'name' : name ,'system' : system ,'size' : size ,'version' : version ,'description': description}
            entry = DB.addNewImage(li)
            self.write(json.dumps(li), ensure_ascii=False)
        

class delete_iamge(tornado.web.RequestHandler):
    def put(self,image_id):
        if DB.deleteOneImage(image_id):
            self.write(image_id)
        else:
            self.write(image_id)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
