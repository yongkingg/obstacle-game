from sys import _xoptions
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui:
    def __init__(self):
        self.character_x = 375
        self.character_y = 500

        font = QtGui.QFont()
        font.setFamily("궁서")
        
        self.mainWindow = QtWidgets.QMainWindow()
        self.mainWindow.resize(800,800)
        self.mainWindow.setMaximumSize(800,800)
        self.mainWindow.setMinimumSize(800,800)
        self.mainWindow.setWindowTitle("Game")

        self.stackedWidget = QtWidgets.QStackedWidget(self.mainWindow)
        self.stackedWidget.setGeometry(0,0,800,800)

        # Start Page
        self.startPage = QtWidgets.QWidget()
        self.startPage.setMinimumSize(QtCore.QSize(800, 800))
        self.startPage.setMaximumSize(QtCore.QSize(800, 800))
        self.stackedWidget.addWidget(self.startPage)

        self.findidpw_font = QtGui.QFont()
        self.findidpw_font.setFamily("HY울릉도B")
        self.findidpw_font.setPointSize(30)
        self.findidpw_font.setPixelSize(30)

        self.startBtn = QtWidgets.QPushButton(self.startPage)
        self.startBtn.setGeometry(175,650,450,100)
        self.startBtn.setText("Join")
        font.setPointSize(40)
        font.setPixelSize(40)
        self.startBtn.setFont(font)
        
        self.startMessage = QtWidgets.QLabel(self.startPage)
        self.startMessage.setGeometry(100,200,600,100)
        self.startMessage.setText("Choose Level")
        font.setPointSize(40)
        font.setPixelSize(40)
        self.startMessage.setFont(font)
        self.startMessage.setAlignment(QtCore.Qt.AlignCenter)

        self.levelBtn = []
        self.levelBtnText = ["EASY","NORAML","HARD"]
        for index in range(0,3):
            tmpBtn = QtWidgets.QPushButton(self.startPage)
            xPos = 175 + 155*index
            tmpBtn.setGeometry(xPos,450,125,100)
            # tmpBtn.setStyleSheet("border : 2px solid black;")
            tmpBtn.setText(self.levelBtnText[index])
            font.setPointSize(25)
            font.setPixelSize(25)
            tmpBtn.setFont(font)
            
            self.levelBtn.append(tmpBtn)

        
        # Game Page
        self.gamePage = QtWidgets.QWidget()
        self.gamePage.setMinimumSize(QtCore.QSize(800, 800))
        self.gamePage.setMaximumSize(QtCore.QSize(800, 800))
        self.stackedWidget.addWidget(self.gamePage)

        self.character = QtWidgets.QLabel(self.gamePage)
        self.character.setGeometry(self.character_x,self.character_y,50,50)
        self.character.setStyleSheet("background-color : red;")

        self.timeArea = QtWidgets.QLabel(self.gamePage)
        self.timeArea.setGeometry(5,0,100,50)
        self.timeArea.setStyleSheet("border : 2px solid black;")
        self.timeArea.setFont(font)
        self.timeArea.setAlignment(QtCore.Qt.AlignCenter)

        self.gameStartBtn = QtWidgets.QPushButton(self.gamePage)
        self.gameStartBtn.setGeometry(600,5,190,50)
        self.gameStartBtn.setStyleSheet("border : 2px solid black;")
        self.gameStartBtn.setText("Game Start")
        self.gameStartBtn.setFont(font)
        

        # self.testObject = QtWidgets.QLabel(self.gamePage)
        # self.testObject.setGeometry(375,375,50,50)
        # self.testObject.setStyleSheet(
        #     "background-color : 2px solid black;"
        #     "border : 2px solid black;"
        #     )



        self.stackedWidget.setCurrentIndex(0)  
        self.mainWindow.show()