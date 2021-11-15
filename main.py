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
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #self.centralwidget.setGraphicsEffect(self.shadow)
        self.setWindowTitle("fuck")
        self.crud_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.CRUD_page))
        self.emprunte_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.emprunte_page))
        self.reserve_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.reserve_page))
        self.menu_btn.clicked.connect(self.menu)
        self.crud()
        self.emprunt()
        self.resrve()
    
    
    def crud(self):
        self.CRUD_table.setColumnWidth(0,100)
        self.CRUD_table.setColumnWidth(1,150)
        self.CRUD_table.setColumnWidth(2,100)
        self.CRUD_table.setColumnWidth(3,100)
        self.CRUD_table.setColumnWidth(4,100)



    
    
    def emprunt(self):
        self.emprunte_table.setColumnWidth(0,100)
        self.emprunte_table.setColumnWidth(1,150)
        self.emprunte_table.setColumnWidth(2,100)
        self.emprunte_table.setColumnWidth(3,100)
        self.emprunte_table.setColumnWidth(4,100)
        
    
    def resrve(self):
        self.reserve_table.setColumnWidth(0,100)
        self.reserve_table.setColumnWidth(1,150)
        self.reserve_table.setColumnWidth(2,100)
        self.reserve_table.setColumnWidth(3,100)
        self.reserve_table.setColumnWidth(4,100)




    def menu(self):
        if self.left_menu_frame.minimumWidth()==60:
            self.left_menu_frame.setMinimumSize(200,200)
        else:
            self.left_menu_frame.setMinimumSize(60,0)






app = QApplication(sys.argv)
window = MainWindow()
window.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
        

