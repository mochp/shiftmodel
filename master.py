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


# config = utils.create_json(config.PORTS)
# utils.start_app()


modelId = 600
path = "2.png"


port = choices(config.PORTS)[0]
print(port)
check = utils.check_port_is_modelId(port,modelId)
if not check:
    print("shifting...")
    utils.shift_port_to_modelId(port,modelId)


while True:
    data = utils.read_json()
    if data[str(port)]["status"]==1:
        print("predicting...")
        break
    time.sleep(1)
    print("wating...")
res = utils.predict(port,path)
print("ok",res)

# if config.port["modelId"] != model_id:
#     os.cmd("kill -9 pid")
#     os.cmd("python slaver.py 8888 400.h5 1,2,3,4,5")
# res = utils.Request(picture_path)
# respon = {"res":res}
# print(data[str(port)]["modelPath"])

# class FileUploadHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.set_header('Access-Control-Allow-Origin', '*')
#         self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
#         modelId = self.get_query_argument('modelId', 'None') 
#         picture_path = self.get_query_argument('path', 'None') 

#         port = choices(config.ports)
#         if config.port["modelId"] != modelId:
#             os.cmd("kill -9 pid")
#             os.cmd("python slaver.py 8888 400.h5 1,2,3,4,5")
#         res = utils.Request(picture_path)
#         respon = {"res":res}

#         self.set_header('Content-Type', 'application/json; charset=UTF-8')
#         self.write(json.dumps(respon))
#         self.finish()

# app = tornado.web.Application([
#     (r'/master', FileUploadHandler),
# ])

# if __name__ == '__main__':
#     app.listen(8888)
#     tornado.ioloop.IOLoop.instance().start()
