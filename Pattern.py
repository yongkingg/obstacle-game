import threading
from PyQt5 import QtWidgets


class FirstType(threading.Thread):
    def __init__(self,ui):
        threading.Thread.__init__(self)
        self.ui = ui
        for index in range(0,50):    
            tmpBtn = QtWidgets.QLabel(self.ui.gamePage)

    def run(self):
        pass

