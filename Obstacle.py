from PyQt5 import QtWidgets, QtCore, Qt
import math
import random
import time

class ObstacleThread(QtCore.QThread):
    resultSignal = QtCore.pyqtSignal(int,int,int)
    def __init__(self,ui,num):
        super().__init__()
        self.ui = ui
        self.num = num
        self.sign = ["+-","-+","--","++","_+","_-","+_","-_"]
        self.theta = None
        self.obstacleSpeed = None
        self.obstacle_xpos = 375
        self.obstacle_ypos = 375

        self.setValue()
        
    def setValue(self):
        self.theta = random.randint(0,360) / math.pi
        self.obstacleSpeed = random.randint(50,100)  

    def run(self):

        for index in range(0,20):
            self.obstacle_xpos = self.obstacle_xpos + (self.obstacleSpeed * math.cos(self.theta))
            self.obstacle_ypos = self.obstacle_ypos + (self.obstacleSpeed * math.sin(self.theta))

            self.resultSignal.emit(self.obstacle_xpos,self.obstacle_ypos,self.num)
            time.sleep(random.random())

class Obstacle:
    def __init__(self,ui):
        self.ui = ui
        self.threadList = []
        self.obstacleList = []
        self.playCount = 0

        for index in range(0,10):
            obstacle = QtWidgets.QLabel(self.ui.gamePage)
            obstacle.setGeometry(375,375,50,50)
            obstacle.setStyleSheet("background-color : black;")
            self.obstacleList.append(obstacle)
            
            makeObstacle = ObstacleThread(self.ui,index)
            makeObstacle.resultSignal.connect(self.showObstacle)
            self.threadList.append(makeObstacle)    
            self.threadList[index].start()

    def showObstacle(self,x_value,y_value,num):
        self.obstacleList[num].show()
        self.obstacleList[num].move(x_value,y_value)


