import tkinter
from tkinter import *

window = Tk()

# def delete():
#     if active1 == True:
#         info_label.destroy()
#     if active2 == True:
#         ver_label.destroy()




def menu_callback():
    print("I'm in the menu callback!")
def submenu_callback():
    print("I'm in the submenu callback!")


# def info():
#      global info_label
#      global active1
#      active1 = True
#      info_label = Label(text="Name: Harsh Tripathi ")
#      info_label.pack()
#
# def ver():
#     global ver_label
#     global active2
#     active2 = True
#     ver_label = Label(text="GUI Version : 2021.10.166")
#     ver_label.pack()
def hide_frames():
    distance_frame.pack_forget()
    currency_frame.pack_forget()
    length_frame.pack_forget()
    weight_frame.pack_forget()


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
def weight_frame_fun():
    hide_frames()
    weight_frame.pack(fill="both", expand=1)




window.minsize(width=600, height=400)    # minsize method
window.title("Convertor GUI Program")  # title method


menu_widget = tkinter.Menu(window)
submenu_widget = tkinter.Menu(menu_widget, tearoff=False)
submenu_widget.add_command(label="Distance", command=distance_frame_fun)
submenu_widget.add_command(label="Currency", command=currency_frame_fun)
submenu_widget.add_command(label="Length", command=length_frame_fun)
submenu_widget.add_command(label="Weight", command=weight_frame_fun)



menu_widget.add_cascade(label="Conversion", menu=submenu_widget)
menu_widget.add_command(label="Factors", command=menu_callback)
menu_widget.add_command(label="GUI Version", command=menu_callback)
menu_widget.add_command(label="Developer Info",command=menu_callback)



window.config(menu=menu_widget)

distance_frame = Frame(width=600, height=400, bg="red")
currency_frame = Frame(width=600, height=400, bg="blue")
length_frame= Frame(width=600, height=400, bg="purple")
weight_frame = Frame(width=600, height=400,)


window.minsize(width=600, height=400)  # minsize method
window.title("Convertor GUI Program")  # title method


# delete_button = Button(text="Delete the text", command=delete)
# delete_button.place(x=450, y=330)



# my_label1 = Label(text="Enter the distance in Miles : ")
# my_label1.place(x=0, y=0)
#
# my_label2 = Label(text="Enter the currency in dollars : ")
# my_label2.place(x=0, y=70)
#
# my_label3_0 = Label(text="Know Your Body Mass Index here ")
# my_label3_0.place(x=0, y=130)
#
# my_label3_1 = Label(text="Enter your height in CM : ")
# my_label3_1.place(x=0, y=160)
#
# my_label3_2 = Label(text="Enter your weight in KG : ")
# my_label3_2.place(x=0, y=180)
#
#
#
# input1 = Entry()
# input1.place(x=201)
#
# input2 = Entry()
# input2.place(x=201,  y=70)
#
# input3_1 = Entry()
# input3_1.place(x=201, y=160)
#
# input3_2 = Entry()
# input3_2.place(x=201, y=180)
#
# def distance():
#             input_text = input1.get()
#             value = float(input_text)
#             km_result = value*1.609
#             result_label = Label(text=f"{value} miles equals {km_result} Kilometers")
#             result_label.place(x=250, y=30)
#
# def fun2():
#             input_text = input2.get()
#             value = int(input_text)
#             rupee = value*74.27
#             result_label = Label(text=f"{value} equals {rupee} USD")
#             result_label.place(x=250, y=100)
#
#
#
# def fun3():
#             input_text_1 = input3_1.get()
#             input_text_2 = input3_2.get()
#             value1 = float(input_text_1)
#             value2 = float(input_text_2)
#             bmi = round(value1/(value2*value2), 4)
#             result_label = Label(text=f"Your BMI is {bmi} CM/KG^2")
#             result_label.place(x=210, y=210)
#
#
#
#
# my_button1 = Button(text="Convert to Kilometers", command=fun1)
# my_button1.place(x=120, y=30)
#
# my_button2 = Button(text="Convert to rupees : ", command=fun2)
# my_button2.place(x=120, y=100)
#
# my_button3 = Button(text="Calculate : ", command=fun3)
# my_button3.place(x=130, y=210)



window.mainloop()    # for holding window













