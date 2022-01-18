from ast import While
from concurrent.futures import thread
from PyQt5 import QtWidgets, QtCore, Qt
import math
import threading
import random
import time
from argon2 import PasswordHasher

from sqlalchemy import false

class ObstacleThread(QtCore.QThread):
    resultSignal = QtCore.pyqtSignal(int,int,int)
    def __init__(self,ui,num):
        super().__init__()
        self.ui = ui
        self.num = num
        self.theta = random.randint(0,360) / math.pi
        self.obstacleSpeed = random.randint(50,100)  
        self.obstacle_xpos = 375
        self.obstacle_ypos = 375
        self.obstacleAlive = True
        
    # 가로 -5 755
    # 세로 0 740

    def check_xpos(self):
        if self.obstacle_xpos >= 730:
            if math.cos(self.theta) >= 0:
                self.obstacle_xpos = self.obstacle_xpos - (self.obstacleSpeed * math.cos(self.theta))
            elif math.cos(self.theta) < 0:
                self.obstacle_xpos = self.obstacle_xpos + (self.obstacleSpeed * math.cos(self.theta))
            self.theta += math.pi
        elif self.obstacle_xpos <= 0:
            if math.cos(self.theta) >= 0:
                self.obstacle_xpos = self.obstacle_xpos + (self.obstacleSpeed * math.cos(self.theta))
            elif math.cos(self.theta) < 0:
                self.obstacle_xpos = self.obstacle_xpos - (self.obstacleSpeed * math.cos(self.theta))
            self.theta += math.pi
        else:
            self.obstacle_xpos = round(self.obstacle_xpos + (self.obstacleSpeed * math.cos(self.theta)))
            
        if self.obstacle_xpos % 10 >= 5:
            self.obstacle_xpos = int(self.obstacle_xpos/10) * 10 + 10
        else:
            self.obstacle_xpos = int(self.obstacle_xpos/10) * 10 


    def check_ypos(self):
        if self.obstacle_ypos >= 730:
            if math.sin(self.theta) >= 0:
                self.obstacle_ypos = self.obstacle_ypos - (self.obstacleSpeed * math.sin(self.theta))
            elif math.sin(self.theta) < 0:
                self.obstacle_ypos = self.obstacle_ypos + (self.obstacleSpeed * math.sin(self.theta))
            self.theta += math.pi
        elif self.obstacle_ypos <= 0:
            if math.sin(self.theta) >= 0:
                self.obstacle_ypos = self.obstacle_ypos + (self.obstacleSpeed * math.sin(self.theta))
            elif math.sin(self.theta) < 0:
                self.obstacle_ypos = self.obstacle_ypos - (self.obstacleSpeed * math.sin(self.theta))
            self.theta += math.pi

        else:
            self.obstacle_ypos = round(self.obstacle_ypos + (self.obstacleSpeed * math.sin(self.theta)))

        if self.obstacle_ypos % 10 >= 5:
            self.obstacle_ypos = int(self.obstacle_ypos/10) * 10 + 10
        else:
            self.obstacle_ypos = int(self.obstacle_ypos/10) * 10 

    def run(self):
        while True:
            self.check_xpos()
            self.check_ypos()
            print(self.obstacle_xpos,self.obstacle_ypos)
            self.resultSignal.emit(self.obstacle_xpos,self.obstacle_ypos,self.num)
            time.sleep(random.random())

class Obstacle:
    def __init__(self,ui):
        self.ui = ui
        self.threadList = []
        self.obstacleList = []
        self.obstacleCount = 10
        self.playCount = 0
        for index in range(0,self.obstacleCount):
            obstacle = QtWidgets.QLabel(self.ui.gamePage)
            obstacle.setGeometry(375,400,50,50)
            obstacle.setStyleSheet("background-color : black;")
            obstacle.show()
            self.obstacleList.append(obstacle)
            
            makeObstacle = ObstacleThread(self.ui,index)
            makeObstacle.resultSignal.connect(self.showObstacle)
            self.threadList.append(makeObstacle)    
            self.threadList[index].start()

    def showObstacle(self,x_value,y_value,num):
        self.obstacleList[num].move(x_value,y_value)
        