import tkinter as tk
import Storage as storage
#from motor import Motor

class HoldButton:
    def __init__(self, host, command=None, delay=None, **kwargs):  # Delay in ms
        self.__host = host
        self.__button = tk.Button(host, kwargs)
        self.__button.pack()
        self.__button.bind("<ButtonPress>", func=self.start)
        self.__button.bind("<ButtonRelease>", func=self.stop)
        self.__delay = delay
        self.__commands = command
        self.__timeon = 0

    def start(self, *args):
        print(f"On for: {self.__timeon}ms")
        if(self.__commands is not None):
            for command in self.__commands:
                command()
        if(self.__delay is not None):
            self.__timeon += self.__delay
            self.__after = self.__host.after(self.__delay, self.start)

    def stop(self, *args):
        print("stop")
        self.__timeon = 0
        self.__host.after_cancel(self.__after)
class GUI:
    def __init__(self):
        self.__storage = storage.Storage()

    def MotorManager(self):
        self.motorGUI = tk.Tk()
        self.motorGUI.title("Motor Manager")

        tk.mainloop()

    def Setup(self):
        self.motorGUI = tk.Tk()
        self.motorGUI.title("Setup")

        tk.mainloop()

    def Test(self):
        self.motorGUI = tk.Tk()
        self.motorGUI.title("Test")
        self.motorGUI.geometry("200x120")
        HoldButton(self.motorGUI, text="Every 100ms", delay=100)
        HoldButton(self.motorGUI, text="Every 200ms", delay=200)
        HoldButton(self.motorGUI, text="Every 500ms", delay=500)
        HoldButton(self.motorGUI, text="Every 1000ms", delay=1000)
        tk.mainloop()

if __name__ == '__main__':
    gui = GUI()

    gui.Test()
