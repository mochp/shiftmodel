# coding=utf-8

import os
import time
import json
import yaml
import tornado.web
import tornado.ioloop
import utils
from random import choices
from conf import config

class FileUploadHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        modelId = self.get_query_argument('modelId', 'None') 
        # picture_path = self.get_query_argument('path', 'jpg') 
        picture_path = "2.png"
        assert int(modelId)>0
        # assert picture_path is not "jpg"

        port = choices(config.PORTS)[0]
        check = utils.check_port_is_modelId(port,modelId)
        utils.waiting_port_success_or_ready(port)
        if check:
            res = utils.predict(port,picture_path)
            utils.setting_port_success(port)
        else:
            print("shifting...")
            utils.shift_port_to_modelId(port,modelId)   
            utils.waiting_port_ready(port)
            res = utils.predict(port,picture_path)
            utils.setting_port_success(port)
            
        respon = {"res":res}

        self.set_header('Content-Type', 'application/json; charset=UTF-8')
        self.write(json.dumps(respon))
        self.finish()

app = tornado.web.Application([
    (r'/master', FileUploadHandler),
])

if __name__ == '__main__':
    app.listen(8888)   
    # server = tornado.httpserver.HTTPServer(app)
    # server.bind(8888)
    # server.start(0)  # 禁用多线程
    tornado.ioloop.IOLoop.instance().start()
