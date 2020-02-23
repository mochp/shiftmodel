from yolo3 import yolo
import time
import sys

if __name__ == '__main__':
    start = time.time()
    model1 = yolo.YOLO(model_path=sys.argv[1],labels=sys.argv[2]) 
    A, B = model1.detect_image("2.png")
    print("cost time: ",time.time()-start)


