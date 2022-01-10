import Ui
import GamePage
from PyQt5 import QtWidgets, QtCore, Qt
import sys
import CountDown
class StartPage:
    def __init__(self):
        self.ui = Ui.Ui()
        self.connectEvent()
    def connectEvent(self):
        self.ui.startBtn.clicked.connect(self.startGame)

    def startGame(self):
        self.ui.stackedWidget.setCurrentIndex(1)  
        self.gamePage = GamePage.GamePage(self.ui)
        self.countDown = CountDown.CountDown(self.ui)
        self.countDown.daemon = True
        self.countDown.start()

if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv)
    startPage = StartPage()
    sys.exit(app.exec_())                              

