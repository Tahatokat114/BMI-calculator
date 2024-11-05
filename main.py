import tkinter

pencere = tkinter.Tk()
pencere.title("BMI Calculator")
pencere.config(bg="white")
pencere.geometry("300x300+600+300")

label3 = None
label4 = None
label5 = None
label6= None
label7 = None
label8 = None
label9 = None

def hesapla():
    global label3,label4,label5,label6,label7,label8,label9
    if label3 is not None:
        label3.destroy()
    if label8 is not None:
        label8.destroy()
    if label9 is not None:
        label9.destroy()
    try:
        x = float(boy.get())
        y = float(kilo.get())

        if x <0 or y<0:
            label9 = tkinter.Label(pencere, text="Lutfen degerlerinizi dogru giriniz")
            label9.place(x=77, y=220)
            return

        bmi = y / (x * x)
        label3 = tkinter.Label(pencere,text=f"Your BMI: {bmi}")
        label3.pack()
        if label4 is not None:
            label4.destroy()
        if label5 is not None:
            label5.destroy()
        if label6 is not None:
            label6.destroy()
        if label7 is not None:
            label7.destroy()

        if bmi <= 18.4:
            label4 = tkinter.Label(pencere, text="UNDERWEIGHT")
            label4.place(x=105, y=220)
        elif 18.5 <= bmi <= 24.9:
            label5 = tkinter.Label(pencere, text="NORMAL")
            label5.place(x=125, y=220)
        elif 25 <= bmi <= 39.9:
            label6 = tkinter.Label(pencere, text="OVERWEIGHT")
            label6.place(x=105, y=220)
        elif bmi >= 40:
            label7 = tkinter.Label(pencere, text="OBESE")
            label7.place(x=125, y=220)
    except ValueError:
            label8 = tkinter.Label(pencere, text="Lutfen gecerli bir sayi giriniz")
            label8.place(x=77 , y=220 )



label1 = tkinter.Label(pencere,text="Enter your weight in KG: ",bg="yellow",fg="blue",font="Arial 12 bold")
label1.place(x=77 ,y=25)

label2 = tkinter.Label(pencere,text="Enter your height in M: ",bg="yellow",fg="blue",font="Arial 12 bold")
label2.place(x=77 ,y=95)

kilo = tkinter.Entry(pencere,width=15)
kilo.pack(padx=50,pady=50)


boy= tkinter.Entry(pencere,width=15)
boy.pack()


buton = tkinter.Button(pencere,text = "Calculate",command=hesapla)
buton.pack(padx=30,pady=30)





pencere.mainloop()