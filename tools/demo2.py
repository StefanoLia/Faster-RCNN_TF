from __future__ import absolute_import, division, print_function

import os

import tensorflow as tf
from tensorflow import keras

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os, sys, cv2

if __name__ == '__main__':

    IMG_SHAPE = (1224, 1624, 3)

    base_model = tf.keras.applications.MobileNetV2(input_shape=IMG_SHAPE,
                                                   include_top=False,
                                                   weights='imagenet')

    base_model.trainable = False

    capture = cv2.VideoCapture('videos/s08-d14-cam-002.avi')
    # Check if camera opened successfully
    if not capture.isOpened():
        print("Error opening video stream or file")
    size = (
        int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    )
    codec = cv2.VideoWriter_fourcc(*'DIVX')
    output = cv2.VideoWriter('videos/videofile_masked_2.avi', codec, 60.0, size)

    i = 0
    while capture.isOpened():
        i = i + 1
        ret, frame = capture.read()
        print(frame.shape)

    capture.release()
    output.release()
    cv2.destroyAllWindows()