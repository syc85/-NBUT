"""
This code is used to adjust some key parameters related to
red ball and yellow stick detection in golf task.
NBUT SYC HK YZN
"""

import cv2
import numpy as np
from visualTask import *
from naoqi import ALProxy
import vision_definitions as vd

if __name__ == "__main__":
    IP = "169.254.143.164"
    # for ball detection
    #detector = BallDetect(IP, resolution=vd.kVGA)
    #detector.sliderHSV(client="test3")

    # for stick detection
    detector = StickDetect(IP)
    detector.slider(client = "test2")
