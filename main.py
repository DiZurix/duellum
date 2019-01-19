from tkinter import *
from random import randint

NbC = 32
C = 24
x0, y0 = 2, 2
remove_dice = 0
dots_1 = []
dots_2 = []
        
root = Tk()
root.title('Duellum')
root.resizable(False, False)

def launch_game():
	can = Canvas(root, bg='white', height = (NbC * C + x0), width = (NbC * C + y0))
	can.pack(side=LEFT)
	menu = Canvas(root, bg='white', height = (NbC * C + x0), width = 300)
	menu.pack(side=RIGHT)

	def create_grille():
		for i in range(NbC + 1):
			can.create_line(x0 + C * i, y0, x0 + C * i, y0 + NbC * C, width = 1)
			can.create_line(x0, y0 + C * i, x0 + NbC * C, y0 + C * i, width = 1)

	create_grille()
	
	def make_dice_1():
		global remove_dice
		nb = randint(1, 6)
		x, y, r = (NbC * C + x0) / 5 - 50, 300*1.25-50, 10
		if remove_dice != 0:
			for i in range(len(dots_1)):
				menu.delete(dots_1[i])
			remove_dice = 0
		if nb == 1:
			dots_1.append(menu.create_oval(x + 16, (y + 16), (x + 16) + r, (y + 16) + r, fill='black'))
			remove_dice += 1
		elif nb == 2:
			dots_1.append(menu.create_oval(x, y + 16, x + r, (y + 16) + r, fill='black'))
			dots_1.append(menu.create_oval(x + 32, (y + 16), (x + 32) + r, (y + 16) + r, fill='black'))
			remove_dice += 1
		elif nb == 3:
			dots_1.append(menu.create_oval(x + 16, (y + 16), (x + 16) + r, (y + 16) + r, fill='black'))
			dots_1.append(menu.create_oval(x + 32, y, (x + 32) + r, y + r, fill='black'))
			dots_1.append(menu.create_oval(x, y + 32, x + r, (y + 32) + r, fill='black'))
			remove_dice += 1
		elif nb == 4:
			dots_1.append(menu.create_oval(x, y, x + r, y + r, fill='black'))
			dots_1.append(menu.create_oval(x + 32, y, (x + 32) + r, y + r, fill='black'))
			dots_1.append(menu.create_oval(x, y + 32, x + r, (y + 32) + r, fill='black'))
			dots_1.append(menu.create_oval(x + 32, y + 32, (x + 32) + r, (y + 32) + r, fill='black'))
			remove_dice += 1
		elif nb == 5:
			dots_1.append(menu.create_oval(x, y, x + r, y + r, fill='black'))
			dots_1.append(menu.create_oval(x + 32, y, (x + 32) + r, y + r, fill='black'))
			dots_1.append(menu.create_oval(x + 16, (y + 16), (x + 16) + r, (y + 16) + r, fill='black'))
			dots_1.append(menu.create_oval(x, y + 32, x + r, (y + 32) + r, fill='black'))
			dots_1.append(menu.create_oval(x + 32, y + 32, (x + 32) + r, (y + 32) + r, fill='black'))
			remove_dice += 1
		elif nb == 6:
			dots_1.append(menu.create_oval(x, y, x + r, y + r, fill='black'))
			dots_1.append(menu.create_oval(x + 32, y, (x + 32) + r, y + r, fill='black'))
			dots_1.append(menu.create_oval(x, y + 16, x + r, (y + 16) + r, fill='black'))
			dots_1.append(menu.create_oval(x + 32, (y + 16), (x + 32) + r, (y + 16) + r, fill='black'))
			dots_1.append(menu.create_oval(x, y + 32, x + r, (y + 32) + r, fill='black'))
			dots_1.append(menu.create_oval(x + 32, y + 32, (x + 32) + r, (y + 32) + r, fill='black'))
			remove_dice += 1
		return nb
		
	def make_dice_2():
		global remove_dice
		nb = randint(1, 6)
		x, y, r = (NbC * C + x0) / 5 + 20, 300*1.25-50, 10
		if remove_dice != 0:
			for i in range(len(dots_2)):
				menu.delete(dots_2[i])
			remove_dice = 0
		if nb == 1:
			dots_2.append(menu.create_oval(x + 16, (y + 16), (x + 16) + r, (y + 16) + r, fill='black'))
			remove_dice += 1
		elif nb == 2:
			dots_2.append(menu.create_oval(x, y + 16, x + r, (y + 16) + r, fill='black'))
			dots_2.append(menu.create_oval(x + 32, (y + 16), (x + 32) + r, (y + 16) + r, fill='black'))
			remove_dice += 1
		elif nb == 3:
			dots_2.append(menu.create_oval(x + 16, (y + 16), (x + 16) + r, (y + 16) + r, fill='black'))
			dots_2.append(menu.create_oval(x + 32, y, (x + 32) + r, y + r, fill='black'))
			dots_2.append(menu.create_oval(x, y + 32, x + r, (y + 32) + r, fill='black'))
			remove_dice += 1
		elif nb == 4:
			dots_2.append(menu.create_oval(x, y, x + r, y + r, fill='black'))
			dots_2.append(menu.create_oval(x + 32, y, (x + 32) + r, y + r, fill='black'))
			dots_2.append(menu.create_oval(x, y + 32, x + r, (y + 32) + r, fill='black'))
			dots_2.append(menu.create_oval(x + 32, y + 32, (x + 32) + r, (y + 32) + r, fill='black'))
			remove_dice += 1
		elif nb == 5:
			dots_2.append(menu.create_oval(x, y, x + r, y + r, fill='black'))
			dots_2.append(menu.create_oval(x + 32, y, (x + 32) + r, y + r, fill='black'))
			dots_2.append(menu.create_oval(x + 16, (y + 16), (x + 16) + r, (y + 16) + r, fill='black'))
			dots_2.append(menu.create_oval(x, y + 32, x + r, (y + 32) + r, fill='black'))
			dots_2.append(menu.create_oval(x + 32, y + 32, (x + 32) + r, (y + 32) + r, fill='black'))
			remove_dice += 1
		elif nb == 6:
			dots_2.append(menu.create_oval(x, y, x + r, y + r, fill='black'))
			dots_2.append(menu.create_oval(x + 32, y, (x + 32) + r, y + r, fill='black'))
			dots_2.append(menu.create_oval(x, y + 16, x + r, (y + 16) + r, fill='black'))
			dots_2.append(menu.create_oval(x + 32, (y + 16), (x + 32) + r, (y + 16) + r, fill='black'))
			dots_2.append(menu.create_oval(x, y + 32, x + r, (y + 32) + r, fill='black'))
			dots_2.append(menu.create_oval(x + 32, y + 32, (x + 32) + r, (y + 32) + r, fill='black'))
			remove_dice += 1
		return nb
		
	def launch_dice():
		make_dice_1()
		make_dice_2()
	
	roll_button = Button(menu, text="Lancer dés")
	roll_button_win = menu.create_window((NbC * C + x0) / 5, 300*1.3, anchor = 'center', width = 150/2, window = roll_button)
	roll_button.configure(bg = 'grey', relief = FLAT, command = launch_dice)
	root.mainloop()

launch_game()
