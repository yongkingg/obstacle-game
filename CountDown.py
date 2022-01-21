import time
from PyQt5 import QtWidgets, QtCore, Qt, QtGui
import threading
import Config


class CountDown(threading.Thread):
    def __init__(self,ui,threadList,obstacle):
        threading.Thread.__init__(self)
        self.ui = ui

        self.threadList = threadList
        self.obstacle = obstacle
        self.sec = 60
        self.state_run = True

    def run(self):
        while self.sec >= 1:
            self.sec -= 1
            self.ui.timeArea.setText(str(self.sec))
            time.sleep(1)
            if self.state_run == False:
                break
            elif self.sec == 0:
                for index in range(0,len(self.threadList)):
                    self.threadList[index].obstacleAlive = False
                    self.ui.lifeSpace.setText("Success!")
                break

    def showAlert(self):
        configText = "Success!"
        self.getConfig = Config.Config(self.ui,configText)
        self.getConfig.gameover_dialog()
        self.getConfig.alert.show()
