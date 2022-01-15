from PyQt5 import QtWidgets, QtCore, Qt
import Character
import Obstacle
import CountDown

class GamePage:
    def __init__(self,ui):
        self.ui = ui
        self.char = Character.Character(self.ui)
        self.countDown()
        self.connectEvent()


    def countDown(self):
        self.runCountDown = CountDown.CountDown(self.ui)
        self.runCountDown.daemon = True
        self.runCountDown.start()

    def connectEvent(self):
        self.ui.gameStartBtn.clicked.connect(self.startGame)

    def startGame(self):
        self.ui.gameStartBtn.hide()
        self.obstacle = Obstacle.Obstacle(self.ui)
