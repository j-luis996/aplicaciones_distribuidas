from tkinter import *
 
def Call():
        lab= Label(root, text = 'Usted presiono\nel boton')
        lab.pack()
        boton['bg'] = 'blue'
        boton['fg'] = 'white'
 
root = Tk()
root.geometry('100x110+350+70')
boton = Button(root, text = 'Presionar', command = Call) 
boton.pack()
 
root.mainloop()
