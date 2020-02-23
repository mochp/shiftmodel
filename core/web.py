# coding=utf-8

import os
import json
import yaml
import tornado.web
import tornado.ioloop
from yolo3.yolo import YOLO
model = YOLO()

with open('./port.yml','rb') as file_config:
    config = yaml.load(file_config)


class FileUploadHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        modelId = self.get_query_argument('modelId', 'None') 
        if int(config["server1"]["modelId"]) == int(modelId):
            _,B = model.detect_image("/home/nlp/lmy/pdf8-web/01.jpg")
        else:
            model = YOLO()
            _,B = model.detect_image("/home/nlp/lmy/pdf8-web/01.jpg")
        respon = {"obj":str(B)}
        self.set_header('Content-Type', 'application/json; charset=UTF-8')
        self.write(json.dumps(respon))
        self.finish()

app = tornado.web.Application([
    (r'/redfile', FileUploadHandler),
])

if __name__ == '__main__':
    app.listen(8007)
    tornado.ioloop.IOLoop.instance().start()
