import cv2
import os
import numpy as np
import argparse
from keras import backend as K
from keras.models import load_model
import licence_plate
import send_text

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 


def resize2SquareKeepingAspectRation(img, size, interpolation):
    h, w = img.shape[:2]
    c = None if len(img.shape) < 3 else img.shape[2]
    if h == w: return cv2.resize(img, (size, size), interpolation)
    if h > w: dif = h
    else:     dif = w
    x_pos = int((dif - w)/2.)
    y_pos = int((dif - h)/2.)
    if c is None:
        mask = np.zeros((dif, dif), dtype=img.dtype)
        mask[y_pos:y_pos+h, x_pos:x_pos+w] = img[:h, :w]
    else:
        mask = np.zeros((dif, dif, c), dtype=img.dtype)
        mask[y_pos:y_pos+h, x_pos:x_pos+w, :] = img[:h, :w, :]
    return cv2.resize(mask, (size, size), interpolation)


def helmet_detection():
    os.chdir(r"E:\ProjectCollege\Images")
    execution_path = os.getcwd()
    print(execution_path)
    image = cv2.imread(r"E:\ProjectCollege\Images\Frames\frame7.jpg", cv2.IMREAD_UNCHANGED)
    print("original dimensions:", image.shape)
    resized = resize2SquareKeepingAspectRation(image, 300, cv2.INTER_AREA)
    cv2.imwrite("frame9_resized.jpg", resized)
    img = cv2.imread(r"E:\ProjectCollege\Images\frame9_resized.jpg")
    img1 = np.expand_dims(resized, axis=0)
    classifier = load_model('helmet_detection.h5')
    predictedClass = classifier.predict_classes(img1)
    print('The predicted class for the input image is: ', predictedClass)
    if predictedClass == 0 :
        print("Helmet is not Present")
        path = r'E:\ProjectCollege\Images'
        try:
            #cv2.imshow('capture',image)
            cv2.imwrite(r'E:\ProjectCollege\Images\Framess\framecapv.jpg',image)
        except Exception as e:
            print(e)
        licence_plate.licence_plate_recognition()
        #send_text.send_text()
    else :
        print("Helmet is Present")
       
