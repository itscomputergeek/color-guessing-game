from tkinter  import*

root = Tk()

root.geometry("1620x4555")

root.minsize(778,434)

root.maxsize(778,434)
root.title("Python3.72")
photo=PhotoImage(file="1.png")
f1= Frame (root,borderwidth=9 ,bg="grey",relief=SUNKEN)
f1.pack(side=LEFT,fill="x")
b1=Button(f1,fg="black",text="print now")
b1.pack()

l=Label(f1,text=''' The JARVIS''')

l.pack(pady=142)
root.mainloop()
