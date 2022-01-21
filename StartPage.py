from email.errors import NonPrintableDefect
from argon2 import PasswordHasher
from sqlalchemy import false, true
import Ui
import GamePage
from PyQt5 import QtWidgets, QtCore, Qt, QtGui
import Config
import sys

# 시간 끝나면 다음 동작 구현
# 폰트 깨짐 문제
class StartPage:
    def __init__(self):
        self.ui = Ui.Ui()
        self.levelClicked = False
        self.level = None
        self.alert = None
        self.messege = None

        self.connectEvent()
        
    def connectEvent(self):
        self.ui.startBtn.clicked.connect(self.startGame)
        for index in range(0,len(self.ui.levelBtn)):
            self.ui.levelBtn[index].mousePressEvent = lambda event, num = index : self.selectLevel(event,num)

    def selectLevel(self,event,num):
        self.level = self.ui.levelBtnText[num]
        for index in range(0,len(self.ui.levelBtn)):
            if index == num:
                self.ui.levelBtn[index].setStyleSheet(
                "background-color : black;"
                "border : 2px solid black;"
                "color : white;"
                )
            else:
                self.ui.levelBtn[index].setStyleSheet(
                "background-color : none;"
                "border : 2px solid black;"
                "color : black;"
                )
        self.levelClicked = True

    def startGame(self):
        if self.levelClicked == False:
            self.getConfig = Config.Config()
            self.getConfig.dialog()
            self.getConfig.messege.setText("Select Level")
            self.getConfig.alert.show()
        else:
            self.ui.stackedWidget.setCurrentIndex(1)  
            self.gamePage = GamePage.GamePage(self.ui,self.level)

if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv)
    startPagdsaddae = StartPage()
    sys.exit(app.exec_())                              
