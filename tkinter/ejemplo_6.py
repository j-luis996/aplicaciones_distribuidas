from tkinter import *

def DrawList():
        plist = ['Diego','Matilde','Ramon']
 
        for item in plist:
                listbox.insert(END,item)
                 
         
root = Tk()
 
listbox = Listbox(root)
boton = Button(root,text = "Presionar",command = DrawList)
 
boton.pack()
listbox.pack()
root.mainloop()
