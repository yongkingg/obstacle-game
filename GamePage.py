from PyQt5 import QtWidgets, QtCore, Qt
import Character
import Obstacle
import CountDown
import Config


class GamePage:
    def __init__(self,ui,level):
        self.ui = ui
        self.level = level
        self.threadList = []
        self.obstacleList = []
        self.setLevel()
        self.char = Character.Character(self.ui)
        self.connectEvent()

    def connectEvent(self):
        self.ui.gameStartBtn.clicked.connect(self.startGame)

    def countDown(self):
        self.runCountDown = CountDown.CountDown(self.ui)
        self.runCountDown.daemon = True
        self.runCountDown.start()

    def startGame(self):
        self.ui.gameStartBtn.hide()
        self.countDown()
        self.ui.showLife()
        self.obstacleCount = 5 + (self.level*5)

        for index in range(0,self.obstacleCount):
            obstacle = QtWidgets.QLabel(self.ui.gamePage)
            obstacle.setGeometry(375,400,50,50)
            obstacle.setStyleSheet("background-color : black;")
            obstacle.show()
            self.obstacleList.append(obstacle)
            
            makeObstacle = Obstacle.ObstacleThread(self.ui,index)
            makeObstacle.resultSignal.connect(self.showObstacle)
            self.threadList.append(makeObstacle)    
            self.threadList[index].start()

    def showObstacle(self,x_value,y_value,num):
        self.obstacleList[num].move(x_value,y_value)
        
        if self.ui.life != 0:
            if (x_value <= self.ui.character_x + 50 and x_value >= self.ui.character_x - 50) and (y_value <= self.ui.character_y + 50 and y_value >= self.ui.character_y - 50):
                self.ui.life -= 1
                self.ui.showLife.setText("Life :" + str(self.ui.life))

        elif self.ui.life == 0:
            for index in range(0,len(self.threadList)):
                self.threadList[index].obstacleAlive = False
            self.ui.showLife.setText("Life :" + str(self.ui.life)) 
            self.getConfig = Config.Config()
            self.getConfig.dialog()
            self.getConfig.messege.setText("Game Over!")
            self.getConfig.alert.show()
            self.runCountDown.state_run = False




    def setLevel(self):
        if self.level == self.ui.levelBtnText[0]:
            self.level = 1
        elif self.level == self.ui.levelBtnText[1]:
            self.level = 2
        elif self.level == self.ui.levelBtnText[2]:
            self.level = 3
