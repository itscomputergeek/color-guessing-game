from tkinter import*
def vicky(event):
    print(f"You clicked the button {event.x},{event.y}")
root = Tk()

root.title("event tkinter")
root.geometry("660x360")
widget= Button(root,text='click me ')
widget.pack()
widget.bind('<Button-1>', vicky)
widget.bind('<Double-1>', quit)
root.mainloop()