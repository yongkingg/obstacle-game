from ast import While
from concurrent.futures import thread
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import math
import threading
import random
import time
import Config

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
            self.resultSignal.emit(self.obstacle_xpos,self.obstacle_ypos,self.num)
            time.sleep(random.random())
            
            if self.obstacleAlive == False:
                break
            


