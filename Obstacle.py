from PyQt5 import QtWidgets, QtCore, Qt
import threading
import random
import time
# 쓰레드를 Gui 내부에서 잘 돌아가도록 다듬은 것
# 가독성을 위해 QThread나 Thread 둘 중 하나만 사용할 것.

class ObstacleThread(QtCore.QThread):
    resultSignal = QtCore.pyqtSignal(int,int,int)
    def __init__(self,ui,num):
        super().__init__()
        self.ui = ui
        self.num = num
        self.obstacle = None
        self.obstacle_xpos = 375
        self.obstacle_ypos = 375
        self.sign = ["+-","-+","--","++"]
        self.obstacleSpeed = None

        # self.makeObstacle()
        self.signCheck()
        
    def makeObstacle(self):
        self.obstacle = QtWidgets.QLabel(self.ui.gamePage)
        self.obstacle_xpos = 375
        self.obstacle_ypos = 375
        self.obstacle.setGeometry(self.obstacle_xpos,self.obstacle_ypos,10,10)
        self.obstacle.setStyleSheet("background-color : black;")
        self.obstacle.show()

    def signCheck(self):
        randomInt = random.randint(0,3)
        self.sign = self.sign[randomInt]
       
    def run(self):
        for index in range(0,10):
            if self.sign == "+-":
                self.obstacle_xpos += random.randint(30,40)
                self.obstacle_ypos -= random.randint(30,40)
            elif self.sign == "-+":
                self.obstacle_xpos -= random.randint(30,40)
                self.obstacle_ypos += random.randint(30,40)
            elif self.sign == "++":
                self.obstacle_xpos += random.randint(30,40)
                self.obstacle_ypos += random.randint(30,40)
            elif self.sign == "--":
                self.obstacle_xpos -= random.randint(30,40)
                self.obstacle_ypos -= random.randint(30,40)
            self.resultSignal.emit(self.obstacle_xpos,self.obstacle_ypos,self.num)
            time.sleep(1)

class Obstacle:
    def __init__(self,ui):
        self.ui = ui
        self.threadList = []
        self.obstacleList = []
        self.playCount = 0
        for index in range(0,4):
            makeObstacle = ObstacleThread(self.ui,index)
            makeObstacle.resultSignal.connect(self.showObstacle)
            makeObstacle.start()
            self.threadList.append(makeObstacle)    
            
            obstacle = QtWidgets.QLabel(self.ui.gamePage)
            obstacle.setGeometry(375,375,50,50)
            obstacle.setStyleSheet("background-color : black;")
            self.obstacleList.append(obstacle)            

    # @QtCore.pyqtSlot(int,int)
    def showObstacle(self,x_value,y_value,num):
        self.obstacleList[num].show()
        self.obstacleList[num].move(x_value,y_value)

# 왜 move인데 움직이지 않고 새로 생성되는가 ? 
# 왜 시작점이 똑같지 않은가 ? 


# 클래스 하나 만들어놓고, 그걸 객체로 받음. 그 객체를 반복문으로 리스트에 담아놓음 
# 담아놓은 리스트의 길이만큼 스타트 걸어두면 됨.
# 시그널 슬롯 
# 쓰레드는 원래 만든다. 
# 메인쓰레드는 이제 서브스레드의 값이 바뀌었을때 바뀐걸 인지하고 적용해야 한다. 그때 쓰는 방법이 시그널 슬롯이다.
# 쓰레드가 값을 바꿀때 슬롯으로 값을 보내면 된다. 
# 그 슬롯 안에서 받아온 값을 바탕으로 화면에 적용
# 그 슬롯은 보통 메 인쓰레드 안에 있다. 
