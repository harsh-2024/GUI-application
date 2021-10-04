from tkinter import *

window = Tk()

window.minsize(width=600, height=400)  # minsize method
window.title("Convertor GUI Program")  # title method
window.config(padx=40, pady=40)

my_label = Label(text="Enter the distance in Miles : ")
my_label.place(x=0, y=0)

input = Entry()
input.place(x=201)

def button_clicked():
            input_text = input.get()
            value = float(input_text)
            km_result = value*1.609
            result_label = Label(text=f"{value} miles equals {km_result} Kilometers")
            result_label.place(x=250, y=30)


my_button = Button(text="Convert to Kilometers", command=button_clicked)
my_button.place(x=120, y=30)



window.mainloop()    # for holding window













