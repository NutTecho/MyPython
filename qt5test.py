import sys
from PyQt5.QtWidgets import QApplication , QWidget
from PyQt5 import uic

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('qt5demo.ui',self)
        self.setWindowTitle('Qt5Demotest')
        self.pushButton.clicked.connect(self.printdata)

    def printdata(self):
        a = int(self.lineEdit.text())
        b = int(self.lineEdit_2.text())
        self.lineEdit_3.setText(str(a+b))
        print(self.lineEdit_3.text())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = AppDemo()
    demo.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('closing window')
