import sys
import random
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("make_color.ui")[0]

class Window(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.label.setText("Let's see some colors!")
        self.label_2.setText("You can choice color with drop box.")

        self.comboBox.addItem('red')
        self.comboBox.addItem('yello')
        self.comboBox.addItem('green')
        self.comboBox.addItem('blue')
        self.comboBox.addItem('purple')
        self.comboBox.currentIndexChanged.connect(self.changeBackgroundColor)

        self.lineEdit.setPlaceholderText("여기에 입력하세요")

    def changeBackgroundColor(self, index):
        color_name = ''
        if index==0:
            r, g, b = 255, 1, 1
            color_name='You picked red!'
        elif index==1:
            r, g, b = 255, 255, 10
            color_name='You picked yello!'
        elif index==2:
            r, g, b = 3, 220, 25
            color_name='You picked green!'
        elif index==3:
            r, g, b = 10, 11, 250
            color_name='You picked blue!'
        else:
            r, g, b = 120, 15, 140
            color_name='You picked purple!'
        self.lineEdit.setStyleSheet(f"background-color: rgb({r}, {g}, {b});")
        self.lineEdit.setText(color_name)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Window()
    myWindow.show()
    app.exec_()