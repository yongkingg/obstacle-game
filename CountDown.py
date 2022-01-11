import time
from PyQt5 import QtWidgets, QtCore, Qt
import threading

class CountDown(threading.Thread):
    def __init__(self,ui):
        threading.Thread.__init__(self)
        self.ui = ui
        self.sec = 60

    def run(self):
        while self.sec >= 0:
            self.ui.timeArea.setText(str(self.sec))
            self.sec -= 1
            time.sleep(1)
