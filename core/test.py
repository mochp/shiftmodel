from yolo3 import yolo
import time


# model2 = yolo.YOLO(model_path='2019-9-28.h5',
#                    labels="1,2,3,4,5,6,7,8,9,0,11,12,13,14")
start = time.time()

model1 = yolo.YOLO(model_path='754.h5',
                   labels="1,2,3,4,5")

start = time.time()
A, B = model1.detect_image("2.png")
print(time.time()-start)

start = time.time()
A, B = model2.detect_image("2.png")
print(time.time()-start)
