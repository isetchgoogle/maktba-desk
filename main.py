import sys
import os
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget

from PyQt5.QtWidgets import QApplication, QMainWindow
from PySide2 import *
from qt_material import *

class MainWindow(QMainWindow):
    def __init__(self):
        super (MainWindow, self).__init__()
        loadUi("interface.ui" , self)
        apply_stylesheet(app, theme='dark_cyan.xml')
       # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")

