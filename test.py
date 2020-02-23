# from yolo3.yolo import YOLO
import time
import os
from multiprocessing import Pool
from conf import config
import requests


def infer(port):
    url = "http://localhost:8888/master?modelId="+str(port)
    res = requests.get(url)
    return res.text


start = time.time()
p = Pool(64)   # 创建4个进程
for i in range(100):
    p.apply_async(infer, args=(400,))
print('Waiting for all subprocesses done...')
p.close()
p.join()

print(time.time()-start)

