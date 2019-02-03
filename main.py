from tkinter import *
from random import randint

NbC = 20
C = 40
x0, y0 = 2, 2
remove_dice = 0
dots = []
id1 = []
id2 = []
rect_list = []
nb_de1, nb_de2 = 0, 0
xi, yi = 25, 25
player = 1
state_launch = NORMAL
nb_shot = 0
abandon_j1 = 0
abandon_j2 = 0
dont_do_this = 0
can_i_place_here = 0

root = Tk()
root.title("Duellum")
root.resizable(False, False)

def launch_game():
	can = Canvas(root, bg = 'white', height = (NbC * C + x0), width = (NbC * C + y0))
	can.pack(side = LEFT)
	menu = Canvas(root, bg = 'white', height = (NbC * C + x0), width = 300)
	menu.pack(side = RIGHT)

	def create_grille():
		for i in range(NbC + 1):
			can.create_line(x0 + C * i, y0, x0 + C * i, y0 + NbC * C, width = 1)
			can.create_line(x0, y0 + C * i, x0 + NbC * C, y0 + C * i, width = 1)

	create_grille()
	
	def make_dice():
		global remove_dice, nb_de1, nb_de2, state_launch, nb_shot
		nb_de1, nb_de2 = randint(1, 6), randint(1, 6)
		x1, x2 = (NbC * C) / 5 - 45, (NbC * C) / 5 + 15
		y, r = 300*1.25-50, 10
		menu.create_rectangle(x1-5, y-5, x1+47, y+47, width = 1)
		menu.create_rectangle(x2-5, y-5, x2+47, y+47, width = 1)
		state_launch = DISABLED
		button()
		for i in range(len(id1)):
			menu.delete(id1[i])
		if player == 1:
			id1.append(menu.create_rectangle(xi, yi, xi + nb_de1 * C, yi + nb_de2 * C, fill = 'red'))
		if player == 2:
			id1.append(menu.create_rectangle(xi, yi, xi + nb_de1 * C, yi + nb_de2 * C, fill = 'blue'))
		if remove_dice != 0:
			for i in range(len(dots)):
				menu.delete(dots[i])
			remove_dice = 0
		if nb_de1 == 1:
			dots.append(menu.create_oval(x1 + 16, (y + 16), (x1 + 16) + r, (y + 16) + r, fill='black'))     #DE1
			remove_dice += 1
		if nb_de2 == 1:
			dots.append(menu.create_oval(x2 + 16, (y + 16), (x2 + 16) + r, (y + 16) + r, fill='black'))     #DE2
			remove_dice += 1
		if nb_de1 == 2:
			dots.append(menu.create_oval(x1, y + 16, x1 + r, (y + 16) + r, fill='black'))                   #DE1
			dots.append(menu.create_oval(x1 + 32, (y + 16), (x1 + 32) + r, (y + 16) + r, fill='black'))
			remove_dice += 1
		if nb_de2 == 2:
			dots.append(menu.create_oval(x2, y + 16, x2 + r, (y + 16) + r, fill='black'))                   #DE2
			dots.append(menu.create_oval(x2 + 32, (y + 16), (x2 + 32) + r, (y + 16) + r, fill='black'))
			remove_dice += 1
		if nb_de1 == 3:
			dots.append(menu.create_oval(x1 + 16, (y + 16), (x1 + 16) + r, (y + 16) + r, fill='black'))     #DE1
			dots.append(menu.create_oval(x1 + 32, y, (x1 + 32) + r, y + r, fill='black'))
			dots.append(menu.create_oval(x1, y + 32, x1 + r, (y + 32) + r, fill='black'))
			remove_dice += 1
		if nb_de2 == 3:
			dots.append(menu.create_oval(x2 + 16, (y + 16), (x2 + 16) + r, (y + 16) + r, fill='black'))     #DE2
			dots.append(menu.create_oval(x2 + 32, y, (x2 + 32) + r, y + r, fill='black'))
			dots.append(menu.create_oval(x2, y + 32, x2 + r, (y + 32) + r, fill='black'))
			remove_dice += 1
		if nb_de1 == 4:
			dots.append(menu.create_oval(x1, y, x1 + r, y + r, fill='black'))                               #DE1
			dots.append(menu.create_oval(x1 + 32, y, (x1 + 32) + r, y + r, fill='black'))
			dots.append(menu.create_oval(x1, y + 32, x1 + r, (y + 32) + r, fill='black'))
			dots.append(menu.create_oval(x1 + 32, y + 32, (x1 + 32) + r, (y + 32) + r, fill='black'))
			remove_dice += 1
		if nb_de2 == 4:
			dots.append(menu.create_oval(x2, y, x2 + r, y + r, fill='black'))                               #DE2
			dots.append(menu.create_oval(x2 + 32, y, (x2 + 32) + r, y + r, fill='black'))
			dots.append(menu.create_oval(x2, y + 32, x2 + r, (y + 32) + r, fill='black'))
			dots.append(menu.create_oval(x2 + 32, y + 32, (x2 + 32) + r, (y + 32) + r, fill='black'))
			remove_dice += 1
		if nb_de1 == 5:
			dots.append(menu.create_oval(x1, y, x1 + r, y + r, fill='black'))                               #DE1
			dots.append(menu.create_oval(x1 + 32, y, (x1 + 32) + r, y + r, fill='black'))
			dots.append(menu.create_oval(x1 + 16, (y + 16), (x1 + 16) + r, (y + 16) + r, fill='black'))
			dots.append(menu.create_oval(x1, y + 32, x1 + r, (y + 32) + r, fill='black'))
			dots.append(menu.create_oval(x1 + 32, y + 32, (x1 + 32) + r, (y + 32) + r, fill='black'))
			remove_dice += 1
		if nb_de2 == 5:
			dots.append(menu.create_oval(x2, y, x2 + r, y + r, fill='black'))                               #DE2
			dots.append(menu.create_oval(x2 + 32, y, (x2 + 32) + r, y + r, fill='black'))
			dots.append(menu.create_oval(x2 + 16, (y + 16), (x2 + 16) + r, (y + 16) + r, fill='black'))
			dots.append(menu.create_oval(x2, y + 32, x2 + r, (y + 32) + r, fill='black'))
			dots.append(menu.create_oval(x2 + 32, y + 32, (x2 + 32) + r, (y + 32) + r, fill='black'))
			remove_dice += 1
		if nb_de1 == 6:
			dots.append(menu.create_oval(x1, y, x1 + r, y + r, fill='black'))                               #DE1
			dots.append(menu.create_oval(x1 + 32, y, (x1 + 32) + r, y + r, fill='black'))
			dots.append(menu.create_oval(x1, y + 16, x1 + r, (y + 16) + r, fill='black'))
			dots.append(menu.create_oval(x1 + 32, (y + 16), (x1 + 32) + r, (y + 16) + r, fill='black'))
			dots.append(menu.create_oval(x1, y + 32, x1 + r, (y + 32) + r, fill='black'))
			dots.append(menu.create_oval(x1 + 32, y + 32, (x1 + 32) + r, (y + 32) + r, fill='black'))
			remove_dice += 1
		if nb_de2 == 6:
			dots.append(menu.create_oval(x2, y, x2 + r, y + r, fill='black'))                               #DE2
			dots.append(menu.create_oval(x2 + 32, y, (x2 + 32) + r, y + r, fill='black'))
			dots.append(menu.create_oval(x2, y + 16, x2 + r, (y + 16) + r, fill='black'))
			dots.append(menu.create_oval(x2 + 32, (y + 16), (x2 + 32) + r, (y + 16) + r, fill='black'))
			dots.append(menu.create_oval(x2, y + 32, x2 + r, (y + 32) + r, fill='black'))
			dots.append(menu.create_oval(x2 + 32, y + 32, (x2 + 32) + r, (y + 32) + r, fill='black'))
			remove_dice += 1
		nb_shot = 0
		return nb_de1, nb_de2
	
	def create_rectangle(evt):
		global player, state_launch, nb_shot, dont_do_this
		xG, yG = evt.x // C * C, evt.y // C * C
		dont_do_this = 0
		for i in range(len(rect_list)):
			for nb_1 in range(nb_de1):
				for nb_2 in range(nb_de2):
					if can.coords(rect_list[i])[2] > float(nb_1 * C + xG + x0) and can.coords(rect_list[i])[3] > float(nb_2 * C + yG + y0) and can.coords(rect_list[i])[0] <= float(nb_1 * C + xG + x0) and can.coords(rect_list[i])[1] <= float(nb_2 * C + yG + y0) and i % 2 == 0:
						dont_do_this += 1
					if can.coords(rect_list[i])[2] > float(- nb_1 * C + xG + x0) and can.coords(rect_list[i])[3] > float(- nb_2 * C + yG + y0) and can.coords(rect_list[i])[0] <= float(- nb_1 * C + xG + x0) and can.coords(rect_list[i])[1] <= float(- nb_2 * C + yG + y0) and i % 2 != 0:
						dont_do_this += 1
					if can.coords(rect_list[i])[2] > float(xG + x0) and can.coords(rect_list[i])[3] > float(yG + x0) and can.coords(rect_list[i])[0] <= float(xG + x0) and can.coords(rect_list[i])[1] <= float(yG + x0) and i % 2 == 0:
						dont_do_this += 1
					if can.coords(rect_list[i])[0] < float(xG + C + x0) and can.coords(rect_list[i])[1] < float(yG + C + x0) and can.coords(rect_list[i])[2] >= float(xG + C + x0) and can.coords(rect_list[i])[3] >= float(yG + C + x0) and i % 2 != 0:
						dont_do_this += 1
			nb_2 = 0
		if dont_do_this == 0:
			if player == 1 and nb_shot == 0 and abandon_j1 != 1:
				rect_list.append(can.create_rectangle(xG + x0, yG + y0, nb_de1 * C + xG + x0, nb_de2 * C + yG + y0, fill = 'red'))
				if abandon_j2 != 1:
					player += 1
			elif player == 2 and nb_shot == 0 and abandon_j2 != 1:
				xG, yG = (evt.x + C) // C * C, (evt.y + C) // C * C
				rect_list.append(can.create_rectangle(xG + x0, yG + y0, - nb_de1 * C + xG + x0, - nb_de2 * C  + yG + y0, fill = 'blue'))
				if abandon_j1 != 1:
					player -= 1
			nb_shot += 1
			state_launch = NORMAL
			button()

	def give_up():
		global abandon_j1, abandon_j2, player, state_launch
		if player == 1:
			abandon_j1 = 1
			player = 2
		elif player == 2:
			abandon_j2 = 1
			player = 1
		if abandon_j1 == 1 and abandon_j2 == 1:
			can.destroy()
			menu.destroy()
			root.destroy()
		state_launch = NORMAL
		button()
		return player

	def return_rectangle(evt):
		global nb_de1, nb_de2, id1
		nb_de1, nb_de2 = nb_de2, nb_de1
		for i in range(len(id1)):
			menu.delete(id1[i])
		if player == 1:
			id1.append(menu.create_rectangle(xi, yi, xi + nb_de1 * C, yi + nb_de2 * C, fill = 'red'))
		if player == 2:
			id1.append(menu.create_rectangle(xi, yi, xi + nb_de1 * C, yi + nb_de2 * C, fill = 'blue'))
		mvt_rect(evt)

	def button():
		roll_button = Button(menu, state = state_launch, text = "Lancer dés")
		roll_button_win = menu.create_window((NbC * C + x0) / 4.9, 410, anchor = 'center', height = 50, width = 150*1, window = roll_button)
		roll_button.configure(bg = 'grey', relief = FLAT, command = make_dice)
		
	def mvt_rect(evt):
		reduc = 5
		for i in range(len(id2)):
			can.delete(id2[i])
		if player == 1 and state_launch == DISABLED:
			id2.append(can.create_rectangle(evt.x - reduc, evt.y - reduc, nb_de1 * C + evt.x + x0 - reduc, nb_de2 * C + evt.y + y0 - reduc, fill = 'red'))
		if player == 2 and state_launch == DISABLED:
			id2.append(can.create_rectangle(evt.x + reduc, evt.y + reduc, - nb_de1 * C + evt.x + x0 + reduc, - nb_de2 * C + evt.y + y0 + reduc, fill = 'blue'))

	give_up_button = Button(menu, text = "Abandonner")
	give_up_button_win = menu.create_window((NbC * C + x0) / 4.9, 750, anchor = 'center', height = 50, width = 150*1, window = give_up_button)
	give_up_button.configure(bg = 'grey', relief = FLAT, command = give_up)
	
	button()
	def clic(event):
		print("x="+ str(event.x)+ " --- y=" + str(event.y))
	
	can.bind("<Button-2>",clic)
	can.bind('<Button-1>', create_rectangle)
	can.bind('<Button-3>', return_rectangle)
	can.bind('<Motion>', mvt_rect)
	
	root.mainloop()

launch_game() #find_overlapping
