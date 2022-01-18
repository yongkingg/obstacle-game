from PyQt5 import QtWidgets,QtGui,Qt,QtCore

class Config:
    def __init__(self):
        pass

    def dialog(self):
        self.alert = QtWidgets.QDialog()
        self.alert.resize(300,200)
        self.alert.setWindowTitle("")
        self.messege = QtWidgets.QLabel(self.alert)
        self.messege.setGeometry(0,0,300,200)
        self.messege.setAlignment(QtCore.Qt.AlignCenter)
        self.messege.setFont(QtGui.QFont("궁서",30))