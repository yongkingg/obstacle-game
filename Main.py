# from pynput.keyboard import Key, Listener

# def on_press(key):
#     print('{0} pressed'.format(
#         key))

# def on_release(key):
#     print('{0} release'.format(
#         key))
#     if key == Key.esc:
#         # Stop listener
#         return False

# # Collect events until released
# with Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()


import Ui
from PyQt5 import QtWidgets, QtCore, Qt
import keyboard
import sys

class Main  :
    def __init__(self):
        self.ui = Ui.Ui()
        self.ui.mainWindow.keyPressEvent = lambda event : self.keyEvent(event)

    def keyEvent(self,e):
        if e.key() == QtCore.Qt.Key_F:
            print("F눌림")


    


if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())                              

