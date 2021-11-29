import sys
import os
from PyQt5.uic import loadUi
import controller 
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget,QTableWidgetItem ,QPushButton
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
        self.creat_CRUD.clicked.connect(self.creat)
        
        self.crud()
        self.table(self.emprunte_table,self.emprunteButtonTable,"self.emprunteBtn","réstoré")
        self.table(self.reserve_table,self.reserveButtonTable,"self.reserveBtn","emprunté")    
###########################################################################################################################
    def table(self,table,btnFunction,btnName,btnText):
        table.setColumnWidth(0,100)
        table.setColumnWidth(1,150)
        table.setColumnWidth(2,100)
        table.setColumnWidth(3,100)
        table.setColumnWidth(4,100)
#firestore_data
        books=controller.getU()
        row=0
        table.setRowCount(len(books))
        for book in books:
            table.setItem(row, 0, QTableWidgetItem(book["Livre"]))
            table.setItem(row, 1, QTableWidgetItem(str(book["Référence"])))
            table.setItem(row, 2, QTableWidgetItem(book["Etudiant"]))
            table.setItem(row, 3, QTableWidgetItem(book["CIN"]))
            table.setItem(row, 4, QTableWidgetItem(str(book["Date"])))
            btnName = QPushButton(btnText)
            btnName.clicked.connect(btnFunction)
            table.setCellWidget(row, 5,btnName)
            row=row+1        
 
###########################################################################################################################
    def crud(self):
        self.CRUD_table.setColumnWidth(0,100)
        self.CRUD_table.setColumnWidth(1,150)
        self.CRUD_table.setColumnWidth(2,100)
        self.CRUD_table.setColumnWidth(3,100)
        self.CRUD_table.setColumnWidth(4,100)
        self.CRUD_table.setColumnWidth(5,100)

        books=controller.getU()
        row=0
        self.CRUD_table.setRowCount(len(books))
        for book in books:
            self.CRUD_table.setItem(row, 0, QTableWidgetItem(book["CIN"]))
            self.CRUD_table.setItem(row, 1, QTableWidgetItem(str(book["Date"]))) 
            self.CRUD_table.setItem(row, 2, QTableWidgetItem(book["Etudiant"]))
            self.CRUD_table.setItem(row, 3, QTableWidgetItem(book["Livre"]))
            self.CRUD_table.setItem(row, 4, QTableWidgetItem(str(book["Référence"])))
           
            row=row+1        

###########################################################################################################################
    def emprunteButtonTable(self):
        button = self.sender()
        index = self.emprunte_table.indexAt(button.pos())
        if index.isValid():
            print(index.row(), index.column())
    
###########################################################################################################################
    def reserveButtonTable(self):
        button = self.sender()
        index = self.reserve_table.indexAt(button.pos())
        if index.isValid():
            print(index.row(), index.column())  
###########################################################################################################################
    def creat(self):
        controller.addBookFireStore()
        self.crud()
###########################################################################################################################
    def menu(self):
        if self.left_menu_frame.minimumWidth()==60:
            self.left_menu_frame.setMinimumSize(200,200)
        else:
            self.left_menu_frame.setMinimumSize(60,0)

###########################################################################################################################
app = QApplication(sys.argv)
window = MainWindow()
window.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
        

