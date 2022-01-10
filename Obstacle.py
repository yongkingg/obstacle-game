from PyQt5 import QtWidgets, QtCore, Qt
import Pattern
import threading

class ObstacleThread(threading.Thread):
    def __init__(self,ui):
        threading.Thread.__init__(self)
        self.ui = ui

        self.obstacle = None
        self.obstacle_x = None
        self.obstacle_y = None

        self.makeObstacle()

    def makeObstacle(self):
        self.obstacle = QtWidgets.QLabel(self.ui.gamePage)
        self.obstacle_x = 375
        self.obstacle_y = 375
        self.obstacle.setGeometry(self.obstacle_x,self.obstacle_y,50,50)
        
    def run(self):
        pass

class Obstacle:
    def __init__(self,ui):
        self.ui = ui
        self.threadList = []
        for index in range(0,50):
            obstacle = ObstacleThread(self.ui)
            self.threadList.append(obstacle)    
            self.threadList[index].start()

# 클래스 하나 만들어놓고, 그걸 객체로 받음. 그 객체를 반복문으로 리스트에 담아놓음 
# 담아놓은 리스트의 길이만큼 스타트 걸어두면 됨.




























































