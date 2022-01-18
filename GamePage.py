from PyQt5 import QtWidgets, QtCore, Qt
import Character
import Obstacle
import CountDown


class GamePage:
    def __init__(self,ui,level):
        self.ui = ui
        self.level = level
        self.setLevel()
        self.char = Character.Character(self.ui)
        self.connectEvent()


    def countDown(self):
        self.runCountDown = CountDown.CountDown(self.ui)
        self.runCountDown.daemon = True
        self.runCountDown.start()

    def connectEvent(self):
        self.ui.gameStartBtn.clicked.connect(self.startGame)

    def startGame(self):
        self.ui.gameStartBtn.hide()
        self.countDown()
        self.ui.showLife()
        self.showObstacle = Obstacle.Obstacle(self.ui,self.level)  

        

    def setLevel(self):
        if self.level == self.ui.levelBtnText[0]:
            self.level = 1
        elif self.level == self.ui.levelBtnText[1]:
            self.level = 2
        elif self.level == self.ui.levelBtnText[2]:
            self.level = 3
