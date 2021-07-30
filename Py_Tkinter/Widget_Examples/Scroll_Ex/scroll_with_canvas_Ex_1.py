from tkinter import *

root = Tk()
root.geometry('500x500')

w = Canvas(root, width=200, height=200,
           borderwidth=0,
           highlightthickness=0,
           background='Coral'
          )
w.pack(padx=10,pady=10)
w.config(scrollregion=[0,0,400,400])  # adds a  400x400 scroll region

w.create_text(300,20,text="hello canvas")
w.create_polygon(10,50,150,100,290,250 , fill= 'red' , outline='black')
# w.create_polygon(410,650,450,600,490,650 , fill= 'red' , outline='black') will be out of range, so can not be displayed

hbar=Scrollbar(root,orient=HORIZONTAL)
hbar.pack(side=BOTTOM,fill=X)

hbar.config(command=w.xview)
w.config(xscrollcommand=hbar.set)

root.mainloop()
