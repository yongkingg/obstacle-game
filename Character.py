from PyQt5 import QtWidgets, QtCore, Qt


class Character:
    def __init__(self,ui):
        self.ui = ui
        self.connectEvent()

    def connectEvent(self):
        self.ui.mainWindow.keyPressEvent = lambda event : self.keyEvent(event)

    def keyEvent(self,e):
        if e.key() == QtCore.Qt.Key_D:
            if self.ui.character_x >= 750:
                self.ui.character_x += 0
            else:
                self.ui.character_x += 20

        elif e.key() == QtCore.Qt.Key_A:
            if self.ui.character_x == -5:
                self.ui.character_x -= 0
            else:
                self.ui.character_x -= 20

        elif e.key() == QtCore.Qt.Key_W:
            if self.ui.character_y == 0:
                self.ui.character_y -= 0
            else: 
                self.ui.character_y -= 20

        elif e.key() == QtCore.Qt.Key_S:
            if self.ui.character_y >= 740:
                self.ui.character_y += 0
            else:
                self.ui.character_y += 20
        print(self.ui.character_x,self.ui.character_y)
        self.ui.character.move(self.ui.character_x,self.ui.character_y)
