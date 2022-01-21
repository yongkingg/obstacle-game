import StartPage
from PyQt5 import QtWidgets,QtGui,Qt,QtCore

class Config:
    def __init__(self,ui,text):
        self.ui = ui
        self.text = text

    def dialog(self):
        self.alert = QtWidgets.QDialog()
        self.alert.resize(300,200)
        self.alert.setWindowTitle("")
        self.messege = QtWidgets.QLabel(self.alert)
        self.messege.setGeometry(0,0,300,200)
        self.messege.setAlignment(QtCore.Qt.AlignCenter)
        self.messege.setFont(QtGui.QFont("궁서",30))

    def gameover_dialog(self):
        
        font = QtGui.QFont()
        font.setFamily("궁서")
        font.setPointSize(25)
        font.setPixelSize(25)

        self.alert = QtWidgets.QDialog()
        self.alert.resize(300,200)
        self.alert.setWindowTitle("")
        self.messege = QtWidgets.QLabel(self.alert)
        self.messege.setGeometry(0,0,300,200)
        self.messege.setAlignment(QtCore.Qt.AlignCenter)
        self.messege.setFont(font)
        self.messege.setText(self.text)


        self.button_dialog = []
        self.button_dialog_Text = ["Restart","Quit"]
        for index in range(0,2):
            tmpBtn = QtWidgets.QPushButton(self.messege)
            xPos = 40 + index * 120
            tmpBtn.setGeometry(xPos,140,100,50)
            tmpBtn.setText(self.button_dialog_Text[index])
            tmpBtn.setFont(font)
            
            self.button_dialog.append(tmpBtn)
        self.connectEvent()
    
    def connectEvent(self):
        self.button_dialog[0].clicked.connect(self.restartGame)
        self.button_dialog[1].clicked.connect(self.quitGame)


    def quitGame(self):
        self.ui.mainWindow.close()
        self.alert.close()

    def restartGame(self):
        self.ui.mainWindow.close()
        self.alert.close()
        self.restart = StartPage.StartPage()
        self.ui.stackedWidget.setCurrentIndex(0)  


