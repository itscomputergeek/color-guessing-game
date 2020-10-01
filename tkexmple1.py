import threading
import tkinter
import time
w=50
h=50
left=0
top=0
def runTak():
    global w,h,left,top
    while(True):
        w+=2
        h+=2
        left+=3
        top+=3
        root.geometry(str(w) + "x" + str(h) + "+" + str(left) + "+" + str(top))
        time.sleep(.5)
        root=tkinter.Tk()
        th1=threading.Thread(target=runTk)
        th1.setDaemon(True)
        th1.start()
        r
        root.minsize(400,300)
        root.maxsize(400,300)
        root.mainloop()