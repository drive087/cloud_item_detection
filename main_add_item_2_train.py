# ################################################################################
# ##
# ## BY: WANDERSON M.PIMENTA
# ## PROJECT MADE WITH: Qt Designer and PySide2
# ## V: 1.0.0
# ##
# ################################################################################

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
# (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import *
# (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from ui_add_item import Ui_Add_Item_MainWindow
# from ui_add_item import Ui_MainWindow
import cv2
import qimage2ndarray

from model import Model
from PIL import Image
# IMPORT FUNCTIONS
from ui_functions import *
from collections import defaultdict
import time
import json
import threading
import numpy as np

import os

class Sleeper(QThread):
    def run(self):
        time.sleep(2)
        msg = make_message()
        msg.exec_()
        time.sleep(4)
        msg.hide()

def make_message():

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Warning!!")
        msg.setInformativeText('Please fill in blank.')
        msg.setStandardButtons(QMessageBox.Ok)
        print('mask message')
        return msg


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Add_Item_MainWindow()

        bg = cv2.imread('./query_img/BG.jpg')
        self.bg = cv2.blur(bg,(10,10))

        self.diffThreshold = 30

        self.ui.setupUi(self)

        self.onReset()

        self.ui.Capture.clicked.connect(lambda: self.onCapture())

        self.ui.Reset.clicked.connect(lambda: self.onReset())

        self.ui.Save.clicked.connect(lambda: self.onSave())

        self.ui.BG.clicked.connect(lambda: self.capture_BG())
        
        self.prepare_item = None

        self.item_name = None

        self.popup = Sleeper()

        self.show()
        ## ==> END ##

    def capture_BG(self):
        ret, frame = cap.read()
        img_frame = frame
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imwrite('./query_img/BG.jpg', frame)
        print('Capture BG success!!')

    def onReset(self):
        path = './query_img/buffer/'
        for item in os.listdir(path):
            os.remove(os.path.join(path, item))

    def displayFrame(self):
        ret, frame = cap.read()
        buff = self.detection(frame)
        if len(buff)==2:
            frame, self.prepare_item = self.detection(frame)
        else:
            frame = self.detection(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = qimage2ndarray.array2qimage(frame)
        label.setPixmap(QPixmap.fromImage(image))

    def detection(self, currentFrame):
        currentFrameBlur = cv2.blur(currentFrame,(10,10))
        previousFrame = self.bg
        frameDifference = cv2.absdiff(currentFrameBlur, previousFrame) > self.diffThreshold 
        frameDifference = frameDifference.astype(np.uint8) * 255 # convert to uin8

        

        kernel = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(10, 10))
        closing = cv2.morphologyEx(frameDifference, cv2.MORPH_CLOSE, kernel)
        closing = np.mean(frameDifference, axis=2)
        closing = np.where(closing==0, 0, 255)
        closing = closing.astype(np.uint8)
        _, contours, _ = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        rbcContourImage = currentFrame.copy()
        img2 = np.zeros_like(rbcContourImage)
        img2[:,:,0] = closing
        img2[:,:,1] = closing
        img2[:,:,2] = closing
        if len(contours)>=1:
            c = max(contours, key = cv2.contourArea)
            x,y,w,h = cv2.boundingRect(c)
            # if w > h:
            #     _pad = w
            # else:_pad = h

            cv2.rectangle(rbcContourImage,(x,y),(x+w,y+h), (0, 0, 255),3)
            return rbcContourImage, currentFrame[y:y+h, x:x+w, :]
        return rbcContourImage

    def pad_img(self, img, pad_with):
        pad_value = max(img.shape[:-1])
        img_padded = np.pad(img,
                            ((0, (pad_value - img.shape[0])),  # pad bottom
                            (0, (pad_value - img.shape[1])),  # pad right
                            (0, 0)),  # don't pad channels
                            mode='constant',
                            constant_values=pad_with)

        return img_padded

    def onCapture(self):
        img = self.prepare_item
        h, w = img.shape[:2]
        # if h > w:
        #     dif_pad = h-w
        #     img_pad = np.pad(a, (0, 3), 'constant', constant_values=(4, 6))

        img_pad = self.pad_img(img, 0)

        path = './dataset/train/'
        _class = self.ui.class_name.toPlainText()
        if _class not in os.listdir(path):os.mkdir(path+_class)
        number = len(os.listdir(path+_class))
        print(number)
        # target_path = os.path.join(path,self.item_name)
        cv2.imwrite(path + '{}/{}{}.jpg'.format(_class, _class, number), img_pad)

        self.ui.Amount.setPlainText(str(number+1)+'/4')

    def onSave(self):
        class_name = self.ui.class_name.toPlainText()
        if len(class_name.strip()) == 0:
            self.popup.run()
        else:
            print(self.ui.class_name.toPlainText())
        

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    current_item = "BG"

    cap = cv2.VideoCapture(3)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 240)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)


    label = QLabel('No Camera Feed')
    layout = QVBoxLayout()
    layout.addWidget(label)

    window = QWidget()
    window.setLayout(layout)
    window.show()
    window2 = MainWindow()
    
    timer = QTimer()
    timer.timeout.connect(window2.displayFrame)
    timer.start(60)

    
    sys.exit(app.exec_())

