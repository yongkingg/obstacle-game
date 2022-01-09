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


import PyQt5
from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import DetectKey
import Ui

class Main  :
    def __init__(self):
        self.ui = Ui.Ui()
        self.detectKey = DetectKey.DetectKeyThread()
        self.detectKey.run()


    


if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())                              

