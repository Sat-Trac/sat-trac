import tkinter as tk
import Storage as storage

# dotenv.set_key(dotenv_path=".env", key_to_set="test", value_to_set="Real Test 2")

class GUI:
    def __init__(self):
        self.__storage = storage.Storage

    def MotorManager(self):
        self.motorGUI = tk.Tk("Motor Manager")

    def Setup(self):
        pass

    def Test(self):
        pass



if __name__ == '__main__':
    gui = GUI()

    gui.MotorManager()
