import tkinter
from tkinter import *

window = Tk()


def hide_frames():
    distance_frame.pack_forget()
    currency_frame.pack_forget()
    length_frame.pack_forget()
    weight_frame.pack_forget()
    gui_ver_frame.pack_forget()
    dev_info_frame.pack_forget()


def dist_calc():
    input_text = input1.get()
    value = float(input_text)
    km_result = value*1.609
    result_label = Label(distance_frame,text=f"{value} miles equals {km_result} Kilometers")
    result_label.place(x=250, y=100)

def distance_tab_labels():
    my_label = Label(distance_frame, text="Enter the distance in Miles").place(x=40, y=40)
    global input1
    input1 = Entry(distance_frame)
    input1.place(x=201,y=40)
    dist_calc_button = Button(distance_frame, text="Convert to Kilometers", command=dist_calc).place(x=120,y=100)

def cur_calc():
    input_text = input2.get()
    value = float(input_text)
    km_result = value*74.692
    result_label = Label(currency_frame,text=f"{value} USD equals {km_result} INR")
    result_label.place(x=250, y=100)


def currency_tab_labels():
    my_label = Label(currency_frame, text="Enter the amount in USD").place(x=40, y=40)
    global input2
    input2 = Entry(currency_frame)
    input2.place(x=201,y=40)
    cur_calc_button = Button(currency_frame, text="Convert to INR", command=cur_calc).place(x=120,y=100)

def len_calc():
    input_text = input3.get()
    value = float(input_text)
    km_result = value*2.54
    result_label = Label(length_frame,text=f"{value} Inches equals {km_result} Centimeters")
    result_label.place(x=270, y=100)



def length_tab_labels():
    my_label = Label(length_frame, text="Enter the length in Inches").place(x=40, y=40)
    global input3
    input3 = Entry(length_frame)
    input3.place(x=201,y=40)
    cur_calc_button = Button(length_frame, text="Convert to Centimeters", command=len_calc).place(x=120,y=100)

def wt_calc():
    input_text = input4.get()
    value = float(input_text)
    km_result = value*0.453
    result_label = Label(weight_frame,text=f"{value} Pound equals {km_result} Kilograms")
    result_label.place(x=270, y=100)



def weight_tab_labels():
    my_label = Label(weight_frame, text="Enter the weight in Pound").place(x=40, y=40)
    global input4
    input4 = Entry(weight_frame)
    input4.place(x=201,y=40)
    cur_calc_button = Button(weight_frame, text="Convert to Kilogram", command=wt_calc).place(x=120,y=100)


def gui_tab_labels():
    my_label = Label(gui_ver_frame, text=" GUI Version : 2021.10.166").place(x=200, y=50)


def dev_tab_labels():
    my_label = Label(dev_info_frame, text=" Harsh Tripathi ").place(x=200, y=50)







def distance_frame_fun():
    hide_frames()
    distance_frame.pack(fill="both", expand=1)
    distance_tab_labels()

def currency_frame_fun():
    hide_frames()
    currency_frame.pack(fill="both", expand=1)
    currency_tab_labels()

def length_frame_fun():
    hide_frames()
    length_frame.pack(fill="both", expand=1)
    length_tab_labels()
def weight_frame_fun():
    hide_frames()
    weight_frame.pack(fill="both", expand=1)
    weight_tab_labels()

def gui_frame_fun():
    hide_frames()
    gui_ver_frame.pack(fill="both", expand=1)
    gui_tab_labels()

def dev_frame_fun():
    hide_frames()
    dev_info_frame.pack(fill="both", expand=1)
    dev_tab_labels()





window.minsize(width=600, height=400)    # minsize method
window.title("Convertor GUI Program")  # title method

menu_widget = tkinter.Menu(window)
submenu_widget = tkinter.Menu(menu_widget, tearoff=False)
submenu_widget.add_command(label="Distance", command=distance_frame_fun)
submenu_widget.add_command(label="Currency", command=currency_frame_fun)
submenu_widget.add_command(label="Length", command=length_frame_fun)
submenu_widget.add_command(label="Weight", command=weight_frame_fun)



menu_widget.add_cascade(label="Conversion", menu=submenu_widget)
menu_widget.add_command(label="GUI Version", command=gui_frame_fun)
menu_widget.add_command(label="Developer Info",command=dev_frame_fun)



window.config(menu=menu_widget)

distance_frame = Frame(width=600, height=400, bg="#4c5670")
currency_frame = Frame(width=600, height=400, bg="#4c5670")
length_frame= Frame(width=600, height=400, bg="#4c5670")
weight_frame = Frame(width=600, height=400, bg="#4c5670")
gui_ver_frame = Frame(width=600, height=400, bg="#b3b8c7")
dev_info_frame = Frame(width=600, height=400, bg="#b3b8c7")


window.minsize(width=600, height=400)  # minsize method
window.title("Convertor GUI Program")  # title method






window.mainloop()    # for holding window













