from sys import _xoptions
from PyQt5 import QtCore, QtWidgets

class Ui:
    def __init__(self):
        self.mainWindow = QtWidgets.QMainWindow()
        self.mainWindow.resize(800,800)
        self.mainWindow.setMaximumSize(800,800)
        self.mainWindow.setMinimumSize(800,800)


        self.centralWidget = QtWidgets.QWidget(self.mainWindow)
        self.centralWidget.setGeometry(0,0,800,800)



        self.character = QtWidgets.QLabel(self.centralWidget)
        self.character.setGeometry(375,375,50,50)
        self.character.setStyleSheet("background-color : red;")


        self.button = QtWidgets.QPushButton(self.centralWidget)
        self.button.setGeometry(100,100,100,100)






        self.mainWindow.show()