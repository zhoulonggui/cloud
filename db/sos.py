import tornado.ioloop 
import tornado.web 
import json
import db

DB=db.db()
class hello(tornado.web.RequestHandler): 
    def get(self): 
        self.write('Hello,xiaorui.cc') 



class get_imagelist(tornado.web.RequestHandler):
    def get(self):
        entries = DB.listAllImage()
        if not entries:
            self.write("/no image")
        else:    
             self.write(json.dumps(entries, ensure_ascii=False))


application = tornado.web.Application([ 
    (r"/", hello), 
    (r"/get", get_imagelist),
])


if __name__ == "__main__": 
    application.listen(8888) 
    tornado.ioloop.IOLoop.instance().start() 
