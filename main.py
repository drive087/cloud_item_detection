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
from ui import Ui_MainWindow
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
import requests
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

model = Model()
endpoint = "http://ec2-18-138-255-177.ap-southeast-1.compute.amazonaws.com:8080/buyItem"

with open('./train.json') as f:
    train_json = json.load(f)

class Sleeper(QThread):
    def run(self, items):
        time.sleep(2)
        msg = make_message(items)
        msg.exec_()
        time.sleep(4)
        msg.hide()

def make_message(items):
        print(items)
        print(train_json['price'])
        total = 0
        cart = ""
        for item, idx in items.items():
            price = train_json['price'][item]*idx
            cart += "{} X {} \t {} {}\n".format(item, idx, price, 'Baht') 
            
            total += price 


        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Total")
        msg.setInformativeText(cart+'\n'+str(total)+' Baht')
        msg.setStandardButtons(QMessageBox.Ok)
        print('mask message')
        return msg

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        
        self.ui.setupUi(self)
        
        self.current_item = None

        self.counting = 0

        self.counting_label_debounce = True

        self.popup = Sleeper()

        self.buff_of_items = dict()

        bg = cv2.imread('./query_img/BG.jpg')
        self.bg = cv2.blur(bg,(10,10))
        self.diffThreshold = 40
        # self.popup.run()

        # with open('./test_local.json') as f:
        #     train_json = json.load(f)
        self.label_list = train_json['class_names']

        self.counting_label = defaultdict(lambda:0)
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        # self.checkLabelChange = False

        # self.ui.Label..connect(lambda: UIFunctions.setTextLabel(self, self.current_item))

        self.ui.Reset.clicked.connect(lambda: self.onResetList())

        self.ui.Purchase_2.clicked.connect(lambda: self.popup.run(self.counting_label))
        
        self.show()
        ## ==> END ##

    

    def onResetList(self):
        self.counting_label = defaultdict(lambda:0)
        self.changeCart()

    def displayFrame(self):
        ret, frame = cap.read()
        frame  = self.detection(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = qimage2ndarray.array2qimage(frame)
        label.setPixmap(QPixmap.fromImage(image))
        # cv2.imwrite('test.jpg', img_frame)
        # x_pred = Image.open('test.jpg')

        # y_pred = model.predict(x_pred)
        # if y_pred == self.current_item:
        #     self.counting = self.counting+1
        # else:
        #     self.counting = 0

        # self.current_item = y_pred
        self.changeLabel()

    def pad_img(self, img, pad_with):
        pad_value = max(img.shape[:-1])
        img_padded = np.pad(img,
                            ((0, (pad_value - img.shape[0])),  # pad bottom
                            (0, (pad_value - img.shape[1])),  # pad right
                            (0, 0)),  # don't pad channels
                            mode='constant',
                            constant_values=pad_with)

        return img_padded

    def detection(self, currentFrame):
        currentFrameBlur = cv2.blur(currentFrame,(10,10))
        previousFrame = self.bg
        frameDifference = cv2.absdiff(currentFrameBlur, previousFrame) > self.diffThreshold 
        frameDifference = frameDifference.astype(np.uint8) * 255 # convert to uin8

        

        kernel = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(20, 20))
        closing = cv2.morphologyEx(frameDifference, cv2.MORPH_CLOSE, kernel)
        closing = np.mean(closing, axis=2)
        closing = np.where(closing==0, 0, 255)
        closing = closing.astype(np.uint8)
        _, contours, _ = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        rbcContourImage = currentFrame.copy()
        for rcbContourIdx in range(len(contours)):
            color = (0, 0, 255)
            # Calculates the bounding rectangle of a contour
            x, y, w, h = cv2.boundingRect(contours[rcbContourIdx])
            posx = x//10
            posy = y//10

            if (posx, posy) not in self.buff_of_items: self.buff_of_items[(posx,posy)] = 0
            self.buff_of_items[(posx,posy)] += 1

            _size = w*h
            
            if _size < 18000 and _size > 3000:
#             and _size < 100000:
                cv2.drawContours(rbcContourImage, contours, rcbContourIdx, color, 2)
                if w>h:
                    _pad = w
                else:
                    _pad = h
                if self.buff_of_items[(posx,posy)] >= 6: color = (0, 255, 0)
                capture_img = currentFrame[y:y+h, x:x+w, :]
                img_pad = self.pad_img(capture_img, 0)
                cv2.rectangle(rbcContourImage,(x,y),(x+w,y+h),color,3)
                cv2.imwrite('test.jpg', img_pad)    
                
                x_pred = Image.open('test.jpg')
                y_pred = model.predict(x_pred)
                # print(y_pred)
                if self.buff_of_items[(posx,posy)] == 6:
                    if y_pred!='Unknown':
                        myobj = {'item': y_pred}
                        json_myobj = json.dumps(myobj)
                        res = requests.post(endpoint, data = json_myobj)
                        if res.status_code == 200:
                            print('Send {} success!!'.format(y_pred))


                cv2.putText(rbcContourImage, y_pred, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

        return rbcContourImage


    def changeLabel(self):
        self.ui.Label.setPlainText(self.current_item)
        if self.counting>=3:
            # self.ui.Label.set
            self.ui.Label.setStyleSheet("QPlainTextEdit {background-color: #00ff00;}")
            if self.counting_label_debounce:
                self.counting_label[self.current_item]+=1
                self.changeCart()
                self.counting_label_debounce = False
        else:

            self.ui.Label.setStyleSheet("QPlainTextEdit {background-color: #ff0000;}")
            self.counting_label_debounce = True

    def changeCart(self):
        cart = ""
        for item, idx in self.counting_label.items():
            price = train_json['price'][item]*idx
            cart += "{} X {} \t {} {}\n".format(item, idx, price, 'Baht') 

        self.ui.List.setPlainText(cart)
        

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

    # timer2 = QTimer()
    # timer2.timeout.connect(editLabel(window2))
    # timer2.start(60)
    
    sys.exit(app.exec_())
    # while True:
    #     window2.ui.Label.insertPlainText(current_item)

