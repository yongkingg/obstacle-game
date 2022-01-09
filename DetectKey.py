from typing_extensions import runtime
from pynput.keyboard import Key, Listener
import threading


class DetectKeyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)             
        self.up = 0
        self.down = 0
        self.left = 0
        self.rignt = 0

    def on_press(self,key):
        if key == Key.up:
            print("Up")
        elif key == Key.down:
            print("down")
        elif key == Key.left:
            print("left")
        elif key == Key.right:
            print("right")

    def run(self):
        with Listener(on_press= self.on_press) as listener:
            listener.join()

  