from tkinter import  *

def getvals():
    print(f"the usename value is {uservalue.get()}")
    print(f"the password value is {passvalue.get()}")
root=Tk()


root.geometry("166x150")
user = Label(root,text="Username")
password = Label(root,text="Password")
user.grid()
password.grid(row=1)

uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root, textvariable = uservalue)
passentry=Entry(root, textvariable = passvalue)

userentry.grid(row=0 , column=1)
passentry.grid(row=1 , column=1)
Button(text="Submits", command=getvals).grid()
root.mainloop()
