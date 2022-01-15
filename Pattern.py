import random

class FirstPattern:
    def __init__(self):
        self.obstacle_xpos = 375
        self.obstacle_ypos = 375
        self.functionTurn = 0

    def plus_plus(self):
        self.obstacle_xpos += random.randint(30,40)
        self.obstacle_ypos += random.randint(30,40)

    def plus_minus(self):
        self.obstacle_xpos += random.randint(30,40)
        self.obstacle_ypos -= random.randint(30,40)

    def minus_plus(self):
        self.obstacle_xpos -= random.randint(30,40)
        self.obstacle_ypos += random.randint(30,40)

    def minus_minus(self):
        self.obstacle_xpos -= random.randint(30,40)
        self.obstacle_ypos -= random.randint(30,40)
    
    def showObstacle(self):
        if self.functionTurn == 0:
            self.plus_plus()
            self.functionTurn += 1
        elif self.functionTurn == 1:
            self.plus_minus()
            self.functionTurn += 1
        elif self.functionTurn == 2:
            self.minus_plus()
            self.functionTurn += 1
        elif self.functionTurn == 3:
            self.minus_minus()
            self.functionTurn += 1






class SecondPattern:
    def __init__(self):
        self.obstacle_xpos = 375
        self.obstacle_ypos = 375

    def setPos(self):
        pass

class ThridPattern:
    def __init__(self):
        self.obstacle_xpos = 375
        self.obstacle_ypos = 375

    def setPos(self):
        pass