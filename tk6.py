from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("750x555")
def myFunc():
     print("813531842")
def help():
    print("yeah ")
    tmsg.showinfo("Help,""i will help you",)
def rate():
    tmsg.askquestion("was your enprince good"," do you want to anything else")
    if value=="yes":
        msg= "rate us on appstore"
    else:
        msg= "we will call you soon"

def harsita():
    ans=tmsg.askretrycancel("Harsita se dosti kar lo"," harsita dost nahi banegi")
    if ans:
        print("retry karne pe katega")
    else:
        print("acha kiya cancel kar diya nahi to kat k cheli jaygi")




root.title("pychram")
#use these funton to create menus
filemenu = Menu(root)
m1= Menu(filemenu,tearoff=0)
m1.add_command(label="Newproject",command=myFunc)
m1.add_command(label="save",command=myFunc)
m1.add_command(label="save as",command=myFunc)
m1.add_command(label="create",command=myFunc)
root.config(menu=filemenu)
filemenu.add_cascade(label="File",menu=m1)
m2= Menu(filemenu,tearoff=0)
m2.add_command(label="Cut",command=myFunc)
m2.add_command(label="Copy",command=myFunc)
m2.add_command(label="Copy as",command=myFunc)
m2.add_command(label="Paste",command=myFunc)
root.config(menu=filemenu).0
filemenu.add_cascade(label="edit",menu=m2)

m3 = Menu(filemenu,tearoff=0)
m3.add_command(label="help",command=help)
m3.add_command(label="Rate us",command=rate)
m3.add_command(label="befrind harshita",command=harsita)
root.config(menu=filemenu)
filemenu.add_cascade(label="Help",menu=m3)


root.mainloop()