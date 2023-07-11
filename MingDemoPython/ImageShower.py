import cv2 as cv
#never ever do this 
# from cv2 import *

from time import sleep

class ImageShower:
    
    def __init__(self, path):
        self.path = path

    def showImage(self):
        self.img = cv.imread(self.path)
        
        cv.imshow("In Reparatur:", self.img)
        cv.waitKey(5000)