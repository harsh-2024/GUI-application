from tkinter import *

window = Tk()

window.minsize(width=600, height=400)  # minsize method
window.title("Convertor GUI Program")  # title method
window.config(padx=40, pady=40)

my_label1 = Label(text="Enter the distance in Miles : ")
my_label1.place(x=0, y=0)

my_label2 = Label(text="Enter the currency in dollars : ")
my_label2.place(x=0, y=70)

my_label3_0 = Label(text="Know Your Body Mass Index here ")
my_label3_0.place(x=0, y=130)

my_label3_1 = Label(text="Enter your height in CM : ")
my_label3_1.place(x=0, y=160)

my_label3_2 = Label(text="Enter your weight in KG : ")
my_label3_2.place(x=0, y=180)



input1 = Entry()
input1.place(x=201)

input2 = Entry()
input2.place(x=201,  y=70)

input3_1 = Entry()
input3_1.place(x=201, y=160)

input3_2 = Entry()
input3_2.place(x=201, y=180)

def fun1():
            input_text = input1.get()
            value = float(input_text)
            km_result = value*1.609
            result_label = Label(text=f"{value} miles equals {km_result} Kilometers")
            result_label.place(x=250, y=30)

def fun2():
            input_text = input2.get()
            value = int(input_text)
            rupee = value*74.27
            result_label = Label(text=f"{value} equals {rupee} USD")
            result_label.place(x=250, y=100)



def fun3():
            input_text_1 = input3_1.get()
            input_text_2 = input3_2.get()
            value1 = float(input_text_1)
            value2 = float(input_text_2)
            bmi = round(value1/(value2*value2), 4)
            result_label = Label(text=f"Your BMI is {bmi} CM/KG^2")
            result_label.place(x=210, y=210)




my_button1 = Button(text="Convert to Kilometers", command=fun1)
my_button1.place(x=120, y=30)

my_button2 = Button(text="Convert to rupees : ", command=fun2)
my_button2.place(x=120, y=100)

my_button3 = Button(text="Calculate : ", command=fun3)
my_button3.place(x=130, y=210)



window.mainloop()    # for holding window













