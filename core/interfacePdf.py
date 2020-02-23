# coding=utf-8


import tornado.ioloop
import tornado.web
import os
import json
from main import mypdf


def getString(file_metas):
    upload_path = os.path.join(os.path.dirname(__file__), 'loadpdf')
    filename = file_metas['filename']
    print(len(filename))
    file_path = os.path.join(upload_path, filename)
    print(file_path)
    with open(file_path, 'wb') as up:
        up.write(file_metas['body'])
    respon = mypdf(file_path)
    return respon


class FileUploadHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

        file_metas=self.request.files.get("image0", None)[0]   
        try:
            result = getString(file_metas)
            respon = {
                    "status": 1,
                    "result": result
                    }
        except:
            respon = {
                    "status": 0,
                    "result": []
                    }

        self.set_header('Content-Type', 'application/json; charset=UTF-8')
        self.write(json.dumps(respon))
        self.finish()


app = tornado.web.Application([
    (r'/pdf4', FileUploadHandler),
])

if __name__ == '__main__':
    app.listen(8007)
    tornado.ioloop.IOLoop.instance().start()
