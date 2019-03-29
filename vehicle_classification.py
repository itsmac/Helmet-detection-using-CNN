from imageai.Detection import ObjectDetection
import os
import cv2
import argparse
import numpy as np

def directory_path():
    os.chdir(r"E:\ProjectCollege")
    execution_path = os.getcwd()
    return execution_path

def vehicle_classifier():
    execution_path = directory_path()
    vidcap = cv2.VideoCapture('input_p_1.mp4')
    count = 0
    e = 1
    c = 0
    f = 1
    success = True
    fps = int(vidcap.get(cv2.CAP_PROP_FPS))
    print("frames per second:", fps)
    print("Reading the frames ")
    try :
        while success:
            success,imag = vidcap.read()
            path = r'E:\ProjectCollege\Images\Frames'
            if count%(0.2*fps) == 0 :
                c = c + 1
                cv2.imwrite(os.path.join(path,'frame%d.jpg'%c),imag)
            count+=1
        print("total no of key frames:", c)
        detector = ObjectDetection()
        detector.setModelTypeAsRetinaNet()
        detector.setModelPath( os.path.join(execution_path , "resnet.h5"))
        detector.loadModel()
        custom = detector.CustomObjects(motorcycle = True)
        while c!=0:
            imgfile = cv2.imread(r"E:\ProjectCollege\Images\Frames\frame%d.jpg"%f)
            path = r"E:\ProjectCollege\Images\Frames"
            detections = detector.detectCustomObjectsFromImage(custom_objects = custom, input_image= os.path.join(path, "frame%d.jpg"%f))
            print("objects in frame%d"%f)
            for eachObject in detections:
                print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
                if eachObject["name"] == "motorcycle" :
                    path = r"E:\ProjectCollege\Images"
                    cv2.imwrite(os.path.join(path ,'capturedframe%d.jpg'%e),imgfile)
                    e = e + 1
            f = f + 1
            c = c - 1
                
    except Exception as e:
            print(str(e))
    
