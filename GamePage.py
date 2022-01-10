from PyQt5 import QtWidgets, QtCore, Qt
import Character
import Obstacle
import CountDown

class GamePage:
    def __init__(self,ui):
        self.ui = ui
        self.char = Character.Character(self.ui)
        # self.obstacle = Obstacle.Obstacle(self.ui)
        




