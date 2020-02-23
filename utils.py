#!/usr/bin/python

import os
import json
import time
import requests
from conf import config


def create_json(ports):
    total = {}
    for i, port in enumerate(ports):
        unit = {}
        unit.update(pid=-1)
        unit.update(status=0)
        unit.update(modelPath=config.INIT_MODELPATH)
        total[str(port)] = unit
    with open("conf/config.json", "w") as f:
        json.dump(total, f, sort_keys=True, indent=4)
    return total

def modelId2path(ids):
    return config.INIT_MODELPATH.replace("600",str(ids))


def start_app():
    data = read_json()
    print(data)
    for key in data:
        print(key, data[key]["modelPath"])
        cmd = ("nohup python slaver.py" + " "
               + key + " "
               + str(data[key]["modelPath"]) + " "
               + config.INIT_LABELS + " &")
        print("start...", cmd)
        os.system(cmd)


def stop_port(port):
    data = read_json()
    pids = data[str(port)]["pid"]
    if pids>0:
        status = os.system("kill -9 " + str(pids))
        time.sleep(0.1)
        if status == 0:
            set_port(port=port, pids=-1, status=0)


def stop_all():
    data = read_json()
    for key in data:
        pids = data[key]["pid"]
        if pids > 0:
            status = os.system("kill -9 " + str(pids))
            if status == 0:
                set_port(port=key, pids=-1, status=0)


def read_json():
    with open("conf/config.json", "r") as f:
        res = json.load(f)
    return res


def set_port(port, pids=None, status=None, modelPath=None):
    port = str(port)
    data = read_json()
    if pids is not None:
        data[port]["pid"] = pids
    if status is not None:
        data[port]["status"] = status
    if modelPath is not None:
        data[port]["modelPath"] = modelPath
    with open("conf/config.json", "w") as f:
        json.dump(data, f, sort_keys=True, indent=4)
    return data

def modelID_to_labels(modelID):
    if int(modelID) == 600:
        return "1,2,3,4,5,6,7,8,9,10,11,12,13,14"
    if int(modelID) == 400:
        return "1,2,3,4,5"


def check_port_is_modelId(port,modelID):
    data = read_json()
    new_model_path = config.INIT_MODELPATH.replace("600",str(modelID))
    if data[str(port)]["modelPath"] == new_model_path:
        return True
    else:
        return False

def shift_port_to_modelId(port,modelID):
    data = read_json()
    stop_port(port)
    new_model_path = config.INIT_MODELPATH.replace("600",str(modelID))
    new_model_labels = modelID_to_labels(modelID)
    cmd = ("nohup python slaver.py" + " " 
            + str(port) + " " 
            + new_model_path +" " 
            + new_model_labels + " &")
    print("cmding:",cmd)
    os.system(cmd)

def predict(port,path):
    url = "http://localhost:"+str(port) +"/yolo?path="+path
    res = requests.get(url)
    return res.text

if __name__ == '__main__':
    print("testing...")
    
