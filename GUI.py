import tkinter as tk
import tkinter.font as tkFont

import AzMotor
import AltMotor
import time
import RPi.GPIO as GPIO
### Need to set up AltMotor and AzMotor Objects upon start ###


class App:
    def __init__(self, root):
        PUL2 = 16  # Stepper Drive Pulses
        DIR2 = 20  # Controller Direction Bit (High for Controller default / LOW to Force a Direction Change).
        ENA2 = 21
        PUL1 = 17  # Stepper Drive Pulses
        DIR1 = 27  # Controller Direction Bit (High for Controller default / LOW to Force a Direction Change).
        ENA1 = 22 
        self.az = AzMotor.AzMotor(ENA1, PUL1, DIR1, 6400, 1)
        self.alt = AltMotor.AltMotor(ENA2, PUL2, DIR2,6400, 1)
        #setting title
        root.title("Satellite Tracker")
        #setting window size
        width=600
        height=225
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        btn_zero_all=tk.Button(root)
        btn_zero_all["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btn_zero_all["font"] = ft
        btn_zero_all["fg"] = "#000000"
        btn_zero_all["justify"] = "center"
        btn_zero_all["text"] = "Zero All"
        btn_zero_all.place(x=20,y=20,width=70,height=25)
        btn_zero_all["command"] = self.btn_zero_all_command

        btn_zero_az=tk.Button(root)
        btn_zero_az["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btn_zero_az["font"] = ft
        btn_zero_az["fg"] = "#000000"
        btn_zero_az["justify"] = "center"
        btn_zero_az["text"] = "Zero Az"
        btn_zero_az.place(x=100,y=20,width=70,height=25)
        btn_zero_az["command"] = self.btn_zero_az_command

        btn_zero_alt=tk.Button(root)
        btn_zero_alt["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btn_zero_alt["font"] = ft
        btn_zero_alt["fg"] = "#000000"
        btn_zero_alt["justify"] = "center"
        btn_zero_alt["text"] = "Zero Alt"
        btn_zero_alt.place(x=100,y=60,width=70,height=25)
        btn_zero_alt["command"] = self.btn_zero_alt_command

        lbox_sat_select=tk.Listbox(root)
        lbox_sat_select["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        lbox_sat_select["font"] = ft
        lbox_sat_select["fg"] = "#333333"
        lbox_sat_select["justify"] = "center"
        lbox_sat_select.place(x=390,y=20,width=180,height=30)

        rad_jog_speed_1=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        rad_jog_speed_1["font"] = ft
        rad_jog_speed_1["fg"] = "#333333"
        rad_jog_speed_1["justify"] = "left"
        rad_jog_speed_1["text"] = " .1 Deg"
        rad_jog_speed_1.place(x=110,y=110,width=85,height=25)
        rad_jog_speed_1["value"] = ".1"
        rad_jog_speed_1["command"] = self.rad_jog_speed_1_command
        rad_jog_speed_1.select()

        rad_jog_speed_2=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        rad_jog_speed_2["font"] = ft
        rad_jog_speed_2["fg"] = "#333333"
        rad_jog_speed_2["justify"] = "left"
        rad_jog_speed_2["text"] = " 1 Deg"
        rad_jog_speed_2.place(x=110,y=130,width=85,height=25)
        rad_jog_speed_2["value"] = "1"
        rad_jog_speed_2["command"] = self.rad_jog_speed_2_command

        rad_jog_speed_3=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        rad_jog_speed_3["font"] = ft
        rad_jog_speed_3["fg"] = "#333333"
        rad_jog_speed_3["justify"] = "left"
        rad_jog_speed_3["text"] = "10 Deg"
        rad_jog_speed_3.place(x=110,y=150,width=85,height=25)
        rad_jog_speed_3["value"] = "10"
        rad_jog_speed_3["command"] = self.rad_jog_speed_3_command

        btn_alt_minus=tk.Button(root)
        btn_alt_minus["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btn_alt_minus["font"] = ft
        btn_alt_minus["fg"] = "#000000"
        btn_alt_minus["justify"] = "center"
        btn_alt_minus["text"] = "Alt -"
        btn_alt_minus.place(x=200,y=150,width=70,height=25)
        btn_alt_minus["command"] = self.btn_alt_minus_command

        btn_alt_plus=tk.Button(root)
        btn_alt_plus["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btn_alt_plus["font"] = ft
        btn_alt_plus["fg"] = "#000000"
        btn_alt_plus["justify"] = "center"
        btn_alt_plus["text"] = "Alt +"
        btn_alt_plus.place(x=200,y=110,width=70,height=25)
        btn_alt_plus["command"] = self.btn_alt_plus_command

        btn_goto_zero=tk.Button(root)
        btn_goto_zero["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btn_goto_zero["font"] = ft
        btn_goto_zero["fg"] = "#000000"
        btn_goto_zero["justify"] = "center"
        btn_goto_zero["text"] = "Go To Zero"
        btn_goto_zero.place(x=20,y=60,width=70,height=25)
        btn_goto_zero["command"] = self.btn_goto_zero_command

        btn_get_tracking_data=tk.Button(root)
        btn_get_tracking_data["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btn_get_tracking_data["font"] = ft
        btn_get_tracking_data["fg"] = "#000000"
        btn_get_tracking_data["justify"] = "center"
        btn_get_tracking_data["text"] = "Get Tracking Data"
        btn_get_tracking_data.place(x=430,y=60,width=107,height=30)
        btn_get_tracking_data["command"] = self.btn_get_tracking_data_command

        btn_go=tk.Button(root)
        btn_go["bg"] = "#5fb878"
        ft = tkFont.Font(family='Times',size=10)
        btn_go["font"] = ft
        btn_go["fg"] = "#000000"
        btn_go["justify"] = "center"
        btn_go["text"] = "GO!"
        btn_go.place(x=390,y=100,width=80,height=80)
        btn_go["command"] = self.btn_go_command

        btn_stop=tk.Button(root)
        btn_stop["bg"] = "#cc0000"
        ft = tkFont.Font(family='Times',size=10)
        btn_stop["font"] = ft
        btn_stop["fg"] = "#000000"
        btn_stop["justify"] = "center"
        btn_stop["text"] = "STOP!"
        btn_stop.place(x=490,y=100,width=80,height=80)
        btn_stop["command"] = self.btn_stop_command

        GLabel_681=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_681["font"] = ft
        GLabel_681["fg"] = "#333333"
        GLabel_681["justify"] = "center"
        GLabel_681["text"] = "ALTITUDE"
        GLabel_681.place(x=200,y=20,width=70,height=25)

        GLabel_896=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_896["font"] = ft
        GLabel_896["fg"] = "#333333"
        GLabel_896["justify"] = "center"
        GLabel_896["text"] = "AZIMUTH"
        GLabel_896.place(x=290,y=20,width=70,height=25)

        lbl_cur_alt=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lbl_cur_alt["font"] = ft
        lbl_cur_alt["fg"] = "#333333"
        lbl_cur_alt["justify"] = "center"
        lbl_cur_alt["text"] = "Curr Alt"
        lbl_cur_alt.place(x=200,y=50,width=70,height=25)

        lbl_cur_az=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lbl_cur_az["font"] = ft
        lbl_cur_az["fg"] = "#333333"
        lbl_cur_az["justify"] = "center"
        lbl_cur_az["text"] = "Curr Az"
        lbl_cur_az.place(x=290,y=50,width=70,height=25)

        btn_az_plus=tk.Button(root)
        btn_az_plus["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btn_az_plus["font"] = ft
        btn_az_plus["fg"] = "#000000"
        btn_az_plus["justify"] = "center"
        btn_az_plus["text"] = "Az +"
        btn_az_plus.place(x=290,y=110,width=70,height=25)
        btn_az_plus["command"] = self.btn_az_plus_command

        btn_alt_minus=tk.Button(root)
        btn_alt_minus["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btn_alt_minus["font"] = ft
        btn_alt_minus["fg"] = "#000000"
        btn_alt_minus["justify"] = "center"
        btn_alt_minus["text"] = "Az -"
        btn_alt_minus.place(x=290,y=150,width=70,height=25)
        btn_alt_minus["command"] = self.btn_az_minus_command

        GLabel_491=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_491["font"] = ft
        GLabel_491["fg"] = "#333333"
        GLabel_491["justify"] = "center"
        GLabel_491["text"] = "Jog Speed:"
        GLabel_491.place(x=30,y=130,width=70,height=25)

        GLabel_218=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_218["font"] = ft
        GLabel_218["fg"] = "#333333"
        GLabel_218["justify"] = "right"
        GLabel_218["text"] = "Local Time:"
        GLabel_218.place(x=10,y=190,width=70,height=25)

        lbl_local_time=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lbl_local_time["font"] = ft
        lbl_local_time["fg"] = "#333333"
        lbl_local_time["justify"] = "left"
        lbl_local_time["text"] = "00:00:00"
        lbl_local_time.place(x=80,y=190,width=70,height=25)

        GLabel_504=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_504["font"] = ft
        GLabel_504["fg"] = "#333333"
        GLabel_504["justify"] = "right"
        GLabel_504["text"] = "Zulu Time:"
        GLabel_504.place(x=470,y=190,width=70,height=25)

        lbl_zulu_time=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lbl_zulu_time["font"] = ft
        lbl_zulu_time["fg"] = "#333333"
        lbl_zulu_time["justify"] = "left"
        lbl_zulu_time["text"] = "00:00:00"
        lbl_zulu_time.place(x=530,y=190,width=70,height=25)

    def btn_zero_all_command(self):
        # reset current altitude and azimuth positions to zero
        print("command")


    def btn_zero_az_command(self):
        # reset current azimuth position to zero
        print("command")


    def btn_zero_alt_command(self):
        # reset current altitude position to zero
        print("command")


    def rad_jog_speed_1_command(self):
        # probably don't need any code here
        print("command")


    def rad_jog_speed_2_command(self):
        # probably don't need any code here
        print("command")


    def rad_jog_speed_3_command(self):
        # probably don't need any code here
        print("command")


    def btn_alt_minus_command(self):
        # move the altitude negative by the amount selected in the jog speed radio buttons
        print("command")


    def btn_alt_plus_command(self):
        # move the altitude positive by the amount selected in the jog speed radio buttons
        print("command")


    def btn_goto_zero_command(self):
        # move the altitude and azimuth to zero positions
        print("command")


    def btn_get_tracking_data_command(self):
        # use the api class methods to retrieve a set of data to use in tracking
        print("command")

    def btn_go_command(self):
        time.sleep(1)
        self.az.go_to_azimith(10)
        time.sleep(1)
        self.az.go_to_azimith(180)
        time.sleep(1)
        self.az.go_to_azimith(250)
        time.sleep(1)
        self.alt.turn_to_altitude(10)
        time.sleep(1)
        self.alt.turn_to_altitude(180)
        time.sleep(1)
        self.alt.turn_to_altitude(250)
        
        # this button should be disabled until tracking data is retrieved
        # once pushed, all other buttons should be disabled except for STOP
        # it should look up the current time in the tracking data then use the
        # AltMotor and AzMotor methods to go to the correct position
        print("command")


    def btn_stop_command(self):
        GPIO.cleanup()
        exit()
        # This should stop all movement immediately and re-enable other buttons on the form
        print("command")


    def btn_az_plus_command(self):
        # move the azimuth positive by the amount selected in the jog speed radio buttons
        print("command")


    def btn_az_minus_command(self):
        print(time.perf_counter())
        #self.az.turn_degrees(1)
        #root.after(1, lambda: app.btn_az_minus_command())
        #print(time.perf_counter())
        # move the azimuth negative by the amount selected in the jog speed radio buttons

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    

    #root.after(100, lambda: app.btn_az_minus_command())
    
    root.mainloop()



