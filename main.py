import tkinter
from tkinter import *

window = Tk()

def delete():
    if active1 == True:
        info_label.pack_forget()
    if active2 == True:
        ver_label.pack_forget()




def menu_callback():
    print("I'm in the menu callback!")
def submenu_callback():
    print("I'm in the submenu callback!")

def info():
     global info_label
     global active1
     active1 = True
     info_label = Label(text="Name: Harsh Tripathi ")
     info_label.pack()

def ver():
    global ver_label
    global active2
    active2 = True
    ver_label = Label(text="GUI Version : 2021.10.166")
    ver_label.pack()


window.minsize(width=600, height=400)    # minsize method
window.title("Convertor GUI Program")  # title method
window.config(padx=40, pady=40)


menu_widget = tkinter.Menu(window)
submenu_widget = tkinter.Menu(menu_widget, tearoff=False)
submenu_widget.add_command(label="Distance", command=submenu_callback)
submenu_widget.add_command(label="Currency", command=submenu_callback)
submenu_widget.add_command(label="Length", command=submenu_callback)
submenu_widget.add_command(label="Weight", command=submenu_callback)



menu_widget.add_cascade(label="Conversion", menu=submenu_widget)
menu_widget.add_command(label="Factors", command=menu_callback)
menu_widget.add_command(label="GUI Version", command=ver)
menu_widget.add_command(label="Developer Info", command=info)

window.config(menu=menu_widget)



window.minsize(width=600, height=400)  # minsize method
window.title("Convertor GUI Program")  # title method
window.config(padx=40, pady=40)

delete_button = Button(text="Delete the text", command=delete)
delete_button.place(x=450, y=330)



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
# def fun1():
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













