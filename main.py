from tkinter import *
from random import *

NbC = 15
C = 50
x0, y0 = 2, 2 
        
win = Tk()
win.title('Duellum')
win.resizable(False, False)

can = Canvas(win, bg='white', height = (NbC * C + x0), width = (NbC * C + y0))
can.pack()

def create_grille():
	for i in range(NbC + 1):
		can.create_line(x0 + C * i, y0, x0 + C * i, y0 + NbC * C, width = 1)
		can.create_line(x0, y0 + C * i, x0 + NbC * C, y0 + C * i, width = 1)

create_grille()

win.mainloop()
