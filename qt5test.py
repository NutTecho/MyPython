import sys
from PyQt5.QtWidgets import QApplication , QWidget ,QMessageBox
from PyQt5 import uic,QtWidgets
from datetime import datetime
import pandas as pd
import pyodbc

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('qt5demo.ui',self)
        self.setWindowTitle('Qt5Demotest')
        self.pushButton.clicked.connect(self.printdata)
        self.comboBox.addItem('c')
        self.pushButton_2.clicked.connect(self.getcombo)
        self.dateTimeEdit.dateTime = datetime.now
        self.tableWidget.setColumnWidth(0,50)
        self.tableWidget.setColumnWidth(1,100)
        self.tableWidget.setColumnWidth(2,50)
        self.tableWidget.setColumnWidth(3,100)
        self.getdb()
        self.Slider1.valueChanged['int'].connect(self.scrolllb.setNum)
        self.Slider1.valueChanged['int'].connect(self.countdata)

    def printdata(self):
        a = int(self.lineEdit.text())
        b = int(self.lineEdit_2.text())
        self.lineEdit_3.setText(str(a+b))
        print(self.lineEdit_3.text())
        msg = QMessageBox()
        msg.setWindowTitle("test message")
        msg.setText("this is main")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ignore|QMessageBox.Ok)
        msg.setInformativeText("informative text, yal")
        msg.setDetailedText("test detail")

        msg.buttonClicked.connect(self.popup_button)
        
        x = msg.exec_()

    def popup_button(self,i):
        print(i.text())

    def getcombo(self):
        data = self.comboBox.currentText()
        index = self.comboBox.findText(data)
        print(index)
        print(data)
    
    def getdb(self):
        con_string = """Driver={SQL Server};
                Server=127.0.0.1;
                Database = test;
                UID = client1;
                PWD = nutert0405;
                """
        sql = """ SELECT * FROM test.dbo.xx	"""
        try:
            with pyodbc.connect(con_string) as con:
                c1 = con.cursor()
                c1.execute(sql)
                self.tableWidget.setRowCount(8)
                for i,row in enumerate(c1):
                    self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(row[1]))
                    self.tableWidget.setItem(i,2,QtWidgets.QTableWidgetItem(str(row[3])))
                    self.tableWidget.setItem(i,3,QtWidgets.QTableWidgetItem(row[4]))


        except Exception as e:
            print('Error -> {}'.format(e))

    def countdata(self,value):
        print(value)

       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = AppDemo()
    demo.show()


    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('closing window')

    



    
        
