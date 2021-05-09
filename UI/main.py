
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

# IMPORT FUNCTIONS
from ui_functions import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Label.

        ## TOGGLE/BURGUER MENU
        ########################################################################
        # self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))
        # self.ui.Add()

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##



def displayFrame():
        ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = qimage2ndarray.array2qimage(frame)
        label.setPixmap(QPixmap.fromImage(image))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

    timer = QTimer()
    timer.timeout.connect(displayFrame)
    timer.start(60)

    label = QLabel('No Camera Feed')
    layout = QVBoxLayout()
    layout.addWidget(label)

    window = QWidget()
    window.setLayout(layout)
    window.show()
    window2 = MainWindow()
    sys.exit(app.exec_())


