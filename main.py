import sys
import os
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget,QTableWidgetItem ,QPushButton
from PySide2 import *
from qt_material import *

class MainWindow(QMainWindow):
    def __init__(self):
        super (MainWindow, self).__init__()
        loadUi("interface.ui" , self)
        apply_stylesheet(app, theme='light_black.xml')
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
    
    def menu(self):
        if self.left_menu_frame.minimumWidth()==60:
            self.left_menu_frame.setMinimumSize(200,200)
        else:
            self.left_menu_frame.setMinimumSize(60,0)


    def crud(self):
        self.CRUD_table.setColumnWidth(0,100)
        self.CRUD_table.setColumnWidth(1,150)
        self.CRUD_table.setColumnWidth(2,100)
        self.CRUD_table.setColumnWidth(3,100)
        self.CRUD_table.setColumnWidth(4,100)

        #local_data
        books=[{"Livre":"ddn","Référence":45,"Etudiant":"ddd York","CIN":"123456","Date":"fff"}, {"Livre":"gg", "Référence":40,"Etudiant":"ggg","CIN":"123458","Date":"Lodon"},
                {"Livre":"fgdss","Référence":30,"Etudiant":"fdssq","CIN":"123457","Date":"dedde"}]
        row=0
        self.CRUD_table.setRowCount(len(books))
        for book in books:
            self.CRUD_table.setItem(row, 0, QTableWidgetItem(book["Livre"]))
            self.CRUD_table.setItem(row, 1, QTableWidgetItem(str(book["Référence"])))
            self.CRUD_table.setItem(row, 2, QTableWidgetItem(book["Etudiant"]))
            self.CRUD_table.setItem(row, 3, QTableWidgetItem(book["CIN"]))
            self.CRUD_table.setItem(row, 4, QTableWidgetItem(book["Date"]))
            row=row+1 

    def emprunt(self):
        self.emprunte_table.setColumnWidth(0,100)
        self.emprunte_table.setColumnWidth(1,150)
        self.emprunte_table.setColumnWidth(2,100)
        self.emprunte_table.setColumnWidth(3,100)
        self.emprunte_table.setColumnWidth(4,100)
        
        #local_data
        books=[{"Livre":"John","Référence":45,"Etudiant":"New York","CIN":"123456","Date":"Londn"}, {"Livre":"Mark", "Référence":40,"Etudiant":"LA","CIN":"123458","Date":"Lodon"},
                {"Livre":"George","Référence":30,"Etudiant":"London","CIN":"123457","Date":"Lodon"}]
        row=0
        self.emprunte_table.setRowCount(len(books))
        for book in books:
            self.emprunte_table.setItem(row, 0, QTableWidgetItem(book["Livre"]))
            self.emprunte_table.setItem(row, 1, QTableWidgetItem(str(book["Référence"])))
            self.emprunte_table.setItem(row, 2, QTableWidgetItem(book["Etudiant"]))
            self.emprunte_table.setItem(row, 3, QTableWidgetItem(book["CIN"]))
            self.emprunte_table.setItem(row, 4, QTableWidgetItem(book["Date"]))
            self.emprunteBtn = QPushButton('restoré')
            self.emprunteBtn.clicked.connect(self.emprunteButtonTable)
            
            self.emprunte_table.setCellWidget(row, 5,self.emprunteBtn)

            row=row+1        

    def emprunteButtonTable(self):
        button = self.sender()
        index = self.emprunte_table.indexAt(button.pos())
        if index.isValid():
            print(index.row(), index.column())
 
    

    def resrve(self):
        self.reserve_table.setColumnWidth(0,100)
        self.reserve_table.setColumnWidth(1,150)
        self.reserve_table.setColumnWidth(2,100)
        self.reserve_table.setColumnWidth(3,100)
        self.reserve_table.setColumnWidth(4,100)
        self.reserve_table.setColumnWidth(5,100)

        #local_data
        books=[{"Livre":"Jdddohn","Référence":45,"Etudiant":"Nddddew York","CIN":"123456","Date":"Londzzzn"}, {"Livre":"Mazzzrk", "Référence":40,"Etudiant":"LzzzA","CIN":"123458","Date":"Lodon"},
                {"Livre":"Gedddorge","Référence":30,"Etudiant":"Loddddndon","CIN":"123457","Date":"Lzzzodon"}]
        row=0
        self.reserve_table.setRowCount(len(books))
        for book in books:
            self.reserve_table.setItem(row, 0, QTableWidgetItem(book["Livre"]))
            self.reserve_table.setItem(row, 1, QTableWidgetItem(str(book["Référence"])))
            self.reserve_table.setItem(row, 2, QTableWidgetItem(book["Etudiant"]))
            self.reserve_table.setItem(row, 3, QTableWidgetItem(book["CIN"]))
            self.reserve_table.setItem(row, 4, QTableWidgetItem(book["Date"]))
            
#BUTTON each row that calls reserveButtonTable function

            self.reserveBtn = QPushButton('emprunté')
            self.reserveBtn.clicked.connect(self.reserveButtonTable)
            self.reserve_table.setCellWidget(row, 5,self.reserveBtn)

            row=row+1        

    def reserveButtonTable(self):
        button = self.sender()
        index = self.reserve_table.indexAt(button.pos())
        if index.isValid():
            print(index.row(), index.column())




app = QApplication(sys.argv)
window = MainWindow()
window.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
        

