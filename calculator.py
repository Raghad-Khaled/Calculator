from tkinter import *

class Calculator(Frame):
    def __init__(self):
        Frame.__init__(self,bg="blue")
        self.option_add('*font','arial 25 bold')
        self.pack(expand=YES,fill=BOTH)
        self.master.title('Calculator') # Set title to background

        display=StringVar()
        obj= Entry(self,relief=RIDGE, textvariable=display, justify="left",bd=20,bg="powder blue",width=30)
        # bd :background porders   justify :the place of righting  bg:the color of back ground
        obj.pack(side=TOP,expand=YES, fill=BOTH)

        clearbutton=Button(self, text="c",bg="white", bd=2 ,command=lambda stord=display: stord.set(""))
        clearbutton.pack(side=TOP, expand=YES, fill=BOTH)

        for exp in ("987/","654+","321-","0.*"):
            frame=Frame(self,bg="silver",bd=2)
            frame.pack(side=TOP, expand=YES, fill=BOTH)
            for char in exp:
                butt=Button(frame, text=char,bg="white", bd=2 ,command=lambda stord=display,ch=char: stord.set(stord.get()+ch))
                butt.pack(side=LEFT, expand=YES, fill=BOTH)

        equal=Button(self, text="=",bg="white", bd=2 ,command=lambda stord=display: stord.set(eval(stord.get())))
        equal.pack(side=TOP, expand=YES, fill=BOTH)





Calculator().mainloop()