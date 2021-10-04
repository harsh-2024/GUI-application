from tkinter import *

window = Tk()

window.minsize(width=600, height=400)  # minsize method
window.title("Convertor GUI Program")  # title method
window.config(padx=40, pady=40)

my_label1 = Label(text="Enter the distance in Miles : ")
my_label1.place(x=0, y=0)

my_label2 = Label(text="Enter the currency in dollars : ")
my_label2.place(x=0, y=70)



input1 = Entry()
input1.place(x=201)

input2 = Entry()
input2.place(x=201,  y=70)

def button_clicked():
            input_text = input1.get()
            value = float(input_text)
            km_result = value*1.609
            result_label = Label(text=f"{value} miles equals {km_result} Kilometers")
            result_label.place(x=250, y=30)


my_button1 = Button(text="Convert to Kilometers", command=button_clicked)
my_button1.place(x=120, y=30)

my_button2 = Button(text="Convert to rupees : ")
my_button2.place(x=120, y=100)




window.mainloop()    # for holding window













