from tkinter import *


root=Tk()

def getvals():
    print(f"{namevalue.get(), gendervalue.get(), phonevalue.get(), emergencyvalue.get(), paymentmodevalue.get() ,foodservicevalue.get() }" )

    with open("record.txt", "a") as f:
        f.write(f"{namevalue.get(), gendervalue.get(), phonevalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()}\n" )



root.geometry("644x344")
Label(root, text=" Welcome to vicky travels",font="comicsansms 14 bold").grid(row=0,column=3)

name = Label(root,text="Name")
gender = Label(root,text="Gender")
phone= Label(root,text="Phone")
emergency= Label(root,text="Emergency Contact")
paymentmode= Label(root,text="Payment Mode")

name.grid(row=1,column=2)
gender.grid(row=2,column=2)
phone.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)

namevalue=StringVar()
gendervalue=StringVar()
phonevalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()
foodservicevalue=IntVar()

nameentery=Entry(root, textvariable=namevalue)
genderentry=Entry(root, textvariable=gendervalue)
phoneentry=Entry(root, textvariable=phonevalue)
emergencyentry=Entry(root, textvariable=emergencyvalue)
paymentmodeentry=Entry(root, textvariable=paymentmodevalue)

nameentery.grid(row=1,column=3)
genderentry.grid(row=2,column=3)
phoneentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymentmodeentry.grid(row=5,column=3)

foodservice=Checkbutton(text="Wants to get your meal", variable=foodservicevalue)
foodservice.grid(row=6,column=3)

Button(root, text="Submit", command=getvals).grid(row=7,column=3)


root.mainloop()
