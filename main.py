from tkinter import *
from random import randint
from tkinter import messagebox

NbC = 20							#Nombre de carré sur une colonne/ligne
C = 40								#Taille des carrés
x0, y0 = 2, 2						#Position initiale pour la grille
remove_dice = 0						#Variable pour supprimer les dés
dots = []							#Liste contenant les dés
moving_rect = []					#Liste qui gérer le déplacement du cube
rect_list = []						#Liste qui contient les rectangles crées
nb_de1, nb_de2 = 0, 0				#Variable contenant la valeur des dés
player = 1							#Variable qui détermine quelle est le joueur actuel (1 = J1, 2 = J2)
state_launch = NORMAL				#Désactive ou non le boutton 'Lancer'
nb_shot = 0							#Variable qui permet de savoir si le joueur a déjà joué ou non
abandon_j1, abandon_j2 = 0, 0		#Variable qui permet de savoir si J1/J2 a abandonné ou non
first_attempt = 0					#Variable qui détermine les 2 premiers coups de la partie
compt_red, compt_blue = [], []		#Liste qui contient les rectangles rouges/bleus
score_joueur1 = 0					#??
score_joueur2 = 0					#??
scorej1 = 0							#??
scorej2 = 0							#??
placement_error = 0
check_contour = 0

root = Tk()
root.title("Duellum")
root.resizable(False, False)

def launch_game(): #LANCEMENT DU PROGRAMME PRINCIPALE
	can = Canvas(root, bg = 'white', height = (NbC * C + x0), width = (NbC * C + y0))
	can.pack(side = LEFT)
	menu = Canvas(root, bg = 'white', height = (NbC * C + x0), width = 300)
	menu.pack(side = RIGHT)

	def create_grille(): #FONCTION POUR CREER LA GRILLE
		for i in range(NbC + 1):
			can.create_line(x0 + C * i, y0, x0 + C * i, y0 + NbC * C, width = 1)
			can.create_line(x0, y0 + C * i, x0 + NbC * C, y0 + C * i, width = 1)

	def make_dice(): #FONCTION POUR CREER LES DES
		global remove_dice, nb_de1, nb_de2, state_launch, nb_shot
		nb_de1, nb_de2 = randint(1, 6), randint(1, 6)
		x1, x2 = (NbC * C) / 5 - 45, (NbC * C) / 5 + 15
		y, r = 325, 10
		menu.create_rectangle(x1-5, y-5, x1+47, y+47, width = 1)
		menu.create_rectangle(x2-5, y-5, x2+47, y+47, width = 1)
		state_launch = DISABLED
		button()
		if remove_dice != 0:
			for i in range(len(dots)):
				menu.delete(dots[i])
			remove_dice = 0
		if nb_de1 == 1:		#DE1 FACE1
			dots.append(menu.create_oval(x1 + 16, (y + 16), (x1 + 16) + r, (y + 16) + r, fill='black'))
		if nb_de2 == 1:		#DE2 FACE1
			dots.append(menu.create_oval(x2 + 16, (y + 16), (x2 + 16) + r, (y + 16) + r, fill='black'))
		if nb_de1 == 2:		#DE1 FACE2
			dots.append(menu.create_oval(x1, y + 16, x1 + r, (y + 16) + r, fill='black'))
			dots.append(menu.create_oval(x1 + 32, (y + 16), (x1 + 32) + r, (y + 16) + r, fill='black'))
		if nb_de2 == 2:		#DE2 FACE2
			dots.append(menu.create_oval(x2, y + 16, x2 + r, (y + 16) + r, fill='black'))
			dots.append(menu.create_oval(x2 + 32, (y + 16), (x2 + 32) + r, (y + 16) + r, fill='black'))
		if nb_de1 == 3:		#DE1 FACE3
			dots.append(menu.create_oval(x1 + 16, (y + 16), (x1 + 16) + r, (y + 16) + r, fill='black'))	
			dots.append(menu.create_oval(x1 + 32, y, (x1 + 32) + r, y + r, fill='black'))
			dots.append(menu.create_oval(x1, y + 32, x1 + r, (y + 32) + r, fill='black'))
		if nb_de2 == 3:		#DE2 FACE3
			dots.append(menu.create_oval(x2 + 16, (y + 16), (x2 + 16) + r, (y + 16) + r, fill='black'))
			dots.append(menu.create_oval(x2 + 32, y, (x2 + 32) + r, y + r, fill='black'))
			dots.append(menu.create_oval(x2, y + 32, x2 + r, (y + 32) + r, fill='black'))
		if nb_de1 == 4:		#DE1 FACE4
			dots.append(menu.create_oval(x1, y, x1 + r, y + r, fill='black'))
			dots.append(menu.create_oval(x1 + 32, y, (x1 + 32) + r, y + r, fill='black'))
			dots.append(menu.create_oval(x1, y + 32, x1 + r, (y + 32) + r, fill='black'))
			dots.append(menu.create_oval(x1 + 32, y + 32, (x1 + 32) + r, (y + 32) + r, fill='black'))
		if nb_de2 == 4:		#DE2 FACE4
			dots.append(menu.create_oval(x2, y, x2 + r, y + r, fill='black'))
			dots.append(menu.create_oval(x2 + 32, y, (x2 + 32) + r, y + r, fill='black'))
			dots.append(menu.create_oval(x2, y + 32, x2 + r, (y + 32) + r, fill='black'))
			dots.append(menu.create_oval(x2 + 32, y + 32, (x2 + 32) + r, (y + 32) + r, fill='black'))
		if nb_de1 == 5:		#DE1 FACE5
			dots.append(menu.create_oval(x1, y, x1 + r, y + r, fill='black'))
			dots.append(menu.create_oval(x1 + 32, y, (x1 + 32) + r, y + r, fill='black'))
			dots.append(menu.create_oval(x1 + 16, (y + 16), (x1 + 16) + r, (y + 16) + r, fill='black'))
			dots.append(menu.create_oval(x1, y + 32, x1 + r, (y + 32) + r, fill='black'))
			dots.append(menu.create_oval(x1 + 32, y + 32, (x1 + 32) + r, (y + 32) + r, fill='black'))
		if nb_de2 == 5:		#DE2 FACE5
			dots.append(menu.create_oval(x2, y, x2 + r, y + r, fill='black'))
			dots.append(menu.create_oval(x2 + 32, y, (x2 + 32) + r, y + r, fill='black'))
			dots.append(menu.create_oval(x2 + 16, (y + 16), (x2 + 16) + r, (y + 16) + r, fill='black'))
			dots.append(menu.create_oval(x2, y + 32, x2 + r, (y + 32) + r, fill='black'))
			dots.append(menu.create_oval(x2 + 32, y + 32, (x2 + 32) + r, (y + 32) + r, fill='black'))
		if nb_de1 == 6:		#DE1 FACE6
			dots.append(menu.create_oval(x1, y, x1 + r, y + r, fill='black'))
			dots.append(menu.create_oval(x1 + 32, y, (x1 + 32) + r, y + r, fill='black'))
			dots.append(menu.create_oval(x1, y + 16, x1 + r, (y + 16) + r, fill='black'))
			dots.append(menu.create_oval(x1 + 32, (y + 16), (x1 + 32) + r, (y + 16) + r, fill='black'))
			dots.append(menu.create_oval(x1, y + 32, x1 + r, (y + 32) + r, fill='black'))
			dots.append(menu.create_oval(x1 + 32, y + 32, (x1 + 32) + r, (y + 32) + r, fill='black'))
		if nb_de2 == 6:		#DE2 FACE6
			dots.append(menu.create_oval(x2, y, x2 + r, y + r, fill='black'))
			dots.append(menu.create_oval(x2 + 32, y, (x2 + 32) + r, y + r, fill='black'))
			dots.append(menu.create_oval(x2, y + 16, x2 + r, (y + 16) + r, fill='black'))
			dots.append(menu.create_oval(x2 + 32, (y + 16), (x2 + 32) + r, (y + 16) + r, fill='black'))
			dots.append(menu.create_oval(x2, y + 32, x2 + r, (y + 32) + r, fill='black'))
			dots.append(menu.create_oval(x2 + 32, y + 32, (x2 + 32) + r, (y + 32) + r, fill='black'))
		remove_dice += 1
		nb_shot = 0
		return nb_de1, nb_de2

	def create_rect(evt): #FONCTION POUR CREER LES RECTANGLES
		global player, state_launch, nb_shot, first_attempt, compt_red, compt_blue, check_contour, placement_error
		xG, yG = evt.x // C * C, evt.y // C * C
		xG2, yG2 = (evt.x + C) // C * C, (evt.y + C) // C * C
		check_error_rect(xG, yG, xG2, yG2)
		if -nb_de1 * C + xG2 + x0 < 0 or -nb_de1 * C + xG2 + x0 > NbC * C + x0 or -nb_de2 * C + yG2 + y0 < 0 or -nb_de2 * C + yG2 + y0 > NbC * C + x0:
			if player == 2:
				placement_error += 1 #VERIFIE SI LE RECTANGLE DE J2 NE SORT PAS DE LA GRILLE
		if placement_error == 0 and nb_shot == 0:
			if player == 1 and abandon_j1 != 1 and first_attempt == 1 or player == 1 and abandon_j1 != 1 and check_contour > 0:
				#Vérifie si aucune erreur est detecté et place le rectangle
				rect_list.append(can.create_rectangle(xG + x0, yG + y0, nb_de1 * C + xG + x0, nb_de2 * C + yG + y0, fill = 'red'))
				can.create_text(nb_de1 / 2 * C + xG, nb_de2 / 2 * C + yG, text = nb_de1 * nb_de2, anchor = CENTER, fill = 'white')
				if first_attempt != 0:
					first_attempt += 1
				if abandon_j2 != 1:
					player += 1
			elif player == 2 and abandon_j2 != 1 and first_attempt == 1 or player == 2 and abandon_j2 != 1 and check_contour > 0:
				#Vérifie si aucune erreur est detecté et place le rectangle
				rect_list.append(can.create_rectangle(xG2 + x0, yG2 + y0, - nb_de1 * C + xG2 + x0, - nb_de2 * C + yG2 + y0, fill = 'blue'))
				can.create_text(- nb_de1 / 2 * C + xG2, - nb_de2 / 2 * C + yG2, text = nb_de1 * nb_de2, anchor = CENTER, fill = 'white')
				if first_attempt != 0:
					first_attempt += 1
				if abandon_j1 != 1:
					player -= 1
			else:
				create_rect(evt)
			nb_shot += 1
			state_launch = NORMAL
			button()
			score()
			
	def check_error_rect(xG, yG, xG2, yG2):
		global player, state_launch, nb_shot, first_attempt, compt_red, compt_blue, check_contour, placement_error
		placement_error = 0
		check_contour = 0
		for i in range(len(rect_list)):
			if can.itemcget((rect_list[i]), 'fill') == 'red':
				if compt_red.count(i) == 0:
					compt_red.append(i)
			elif can.itemcget((rect_list[i]), 'fill') == 'blue':
				if compt_blue.count(i) == 0:
					compt_blue.append(i)
			for nb_1 in range(nb_de1 + 1):
				for nb_2 in range(nb_de2 + 1):
					if placement_error > 0:
						break
					if can.coords(rect_list[i])[2] > float(nb_1 * C + xG + x0) and can.coords(rect_list[i])[3] > float(nb_2 * C + yG + y0) and can.coords(rect_list[i])[0] < float(nb_1 * C + xG + x0) and can.coords(rect_list[i])[1] < float(nb_2 * C + yG + y0) and player == 1:
						placement_error += 1	#REGARDE SI LE RECTANGLE DU J1 N'EST PAS EN COLLISION AVEC LES AUTRES
					if can.coords(rect_list[i])[2] > float(- nb_1 * C + xG2 + x0) and can.coords(rect_list[i])[3] > float(- nb_2 * C + yG2 + y0) and can.coords(rect_list[i])[0] < float(- nb_1 * C + xG2 + x0) and can.coords(rect_list[i])[1] < float(- nb_2 * C + yG2 + y0) and player == 2:
						placement_error += 1	#REGARDE SI LE RECTANGLE DU J2 N'EST PAS EN COLLISION AVEC LES AUTRES
					if can.coords(rect_list[i])[2] > float(xG + x0) and can.coords(rect_list[i])[3] > float(yG + x0) and can.coords(rect_list[i])[0] < float(xG + x0) and can.coords(rect_list[i])[1] < float(yG + x0) and player == 1:
						placement_error += 1	#REGARDE SI LE CLIQUE DU J1 N'EST PAS EN COLLISION AVEC LES RECTANGLES
					if can.coords(rect_list[i])[2] > float(xG + C + x0) and can.coords(rect_list[i])[3] > float(yG + C + x0) and can.coords(rect_list[i])[0] < float(xG + C + x0) and can.coords(rect_list[i])[1] < float(yG + C + x0) and player == 2:
						placement_error += 1	#REGARDE SI LE CLIQUE DU J2 N'EST PAS EN COLLISION AVEC LES RECRANGLE
					for k in compt_red:
						if can.coords(rect_list[k])[2] >= float(nb_1 * C + xG + x0) and can.coords(rect_list[k])[3] >= float(nb_2 * C + yG + y0) and can.coords(rect_list[k])[0] <= float(nb_1 * C + xG + x0) and can.coords(rect_list[k])[1] <= float(nb_2 * C + yG + y0) and player == 1:
							check_contour += 1	#REGARDE SI LE RECTANGLE DU J1 EST PROCHE D'UN RECTANGLE DE LA MÊME COULEUR
					for k in compt_blue:
						if can.coords(rect_list[k])[2] >= float(- nb_1 * C + xG2 + x0) and can.coords(rect_list[k])[3] >= float(- nb_2 * C + yG2 + y0) and can.coords(rect_list[k])[0] <= float(- nb_1 * C + xG2 + x0) and can.coords(rect_list[k])[1] <= float(- nb_2 * C + yG2 + y0) and player == 2:
							check_contour += 1	#REGARDE SI LE RECTANGLE DU J2 EST PROCHE D'UN RECTANGLE DE LA MÊME COULEUR
				nb_2 = 0
		if first_attempt < 2 and xG == 0 and yG == 0 and player == 1 or first_attempt < 2 and xG2 == NbC * C and yG2 == NbC * C and player == 2:
			check_contour += 1 #VERIFIE SI LE PREMIER COUP ET A UNE EXTREMITE
		if nb_de1 * C + xG + x0 < 0 or nb_de1 * C + xG + x0 > NbC * C + x0 or nb_de2 * C + yG + y0 < 0 or nb_de2 * C + yG + y0 > NbC * C + x0:
			if player == 1:
				placement_error += 1 #VERIFIE SI LE RECTANGLE DE J1 NE SORT PAS DE LA GRILLE
		return check_contour, placement_error

	def give_up(): #FONCTION QUI PERMET D'ABANDONNER
		global abandon_j1, abandon_j2, player, state_launch
		if player == 1:
			abandon_j1 = 1
			player = 2
		elif player == 2:
			abandon_j2 = 1
			player = 1
		if abandon_j1 == 1 and abandon_j2 == 1:
			if scorej1 > scorej2:
					bn= messagebox.askquestion("Resultats", ("Le joueur 1 a gagné !\nVoulez vous rejouer ?"))
			elif scorej1 < scorej2:
					bn= messagebox.askquestion("Resultats", ("Le joueur 2 a gagné !\nVoulez vous rejouer ?"))
			elif scorej1 == scorej2:
					bn= messagebox.askquestion("Resultats", ("Egalité ! Personne n'a gagné\nVoulez vous rejouer ?"))
			if bn == "no":
					menu.destroy()
					can.destroy()
					root.destroy()
			if bn == "yes":
					menu.pack_forget()
					can.pack_forget()
					reinitial()
		state_launch = NORMAL
		button()
		return player

	def return_rectangle(evt): #FONCTION POUR RETOURNER LE RECTANGLE
		global nb_de1, nb_de2
		nb_de1, nb_de2 = nb_de2, nb_de1
		root.event_generate('<Motion>')

	def button(): #BUTTON POUR LANCER LES DES
		roll_button = Button(menu, state = state_launch, text = "Lancer dés")
		roll_button_win = menu.create_window((NbC * C + x0) / 4.9, 410, anchor = 'center', height = 50, width = 150*1, window = roll_button)
		roll_button.configure(bg = 'grey', relief = FLAT, command = make_dice)

	def mvt_rect(evt): #FONCTION QUI CREE UN RECTANGLE SOUS LE CURSEUR DE LA SOURIS
		reduc = 5
		for i in range(len(moving_rect)):
			can.delete(moving_rect[i])
		if player == 1 and state_launch == DISABLED:
			moving_rect.append(can.create_rectangle(evt.x - reduc, evt.y - reduc, nb_de1 * C + evt.x + x0 - reduc, nb_de2 * C + evt.y + y0 - reduc, fill = 'red'))
		if player == 2 and state_launch == DISABLED:
			moving_rect.append(can.create_rectangle(evt.x + reduc, evt.y + reduc, - nb_de1 * C + evt.x + x0 + reduc, - nb_de2 * C + evt.y + y0 + reduc, fill = 'blue'))

	def score(): #FONCTION QUI AFFICHE LES SCORES
		global score_joueur1, score_joueur2, scorej1, scorej2
		if player == 2 and abandon_j1 == 0 or abandon_j2 == 2:
			scorej1 += nb_de1 * nb_de2
			menu.delete(score_joueur1)
			score_joueur1 = menu.create_text((NbC * C + x0) / 8.4, 575, text = scorej1, font = ("Courier",35),fill = 'red')
			menu.itemconfigure(score_joueur1, text=str(scorej1))
		if player == 1 and abandon_j2 == 0 or abandon_j1 == 1:
			scorej2 += nb_de1 * nb_de2
			menu.delete(score_joueur2)
			score_joueur2 = menu.create_text((NbC * C + x0) / 3.6, 575, text = scorej2, font = ("Courier",35),fill = 'blue')
			menu.itemconfigure(score_joueur2, text = str(scorej2))

	def reinitial(): #FONCTION QUI SERT A METTRE LES VARIABLES A LEUR ETAT INITIALE
		global remove_dice, dots, moving_rect, rect_list, player, nb_de1, nb_de2, state_launch, nb_shot, abandon_j1, abandon_j2, first_attempt, compt_red, compt_blue, score_joueur1, score_joueur2, scorej1, scorej2
		remove_dice = 0
		dots = []
		moving_rect = []
		rect_list = []
		player = 1
		nb_de1, nb_de2 = 0, 0
		state_launch = NORMAL
		nb_shot = 0
		abandon_j1 = 0
		abandon_j2 = 0
		first_attempt = 0
		compt_red, compt_blue = [], []
		score_joueur1 = 0
		score_joueur2 = 0
		scorej1 = 0
		scorej2 = 0
		launch_game()

	give_up_button = Button(menu, text = "Abandonner")
	give_up_button_win = menu.create_window((NbC * C + x0) / 4.9, 750, anchor = 'center', height = 50, width = 150*1, window = give_up_button)
	give_up_button.configure(bg = 'grey', relief = FLAT, command = give_up)

	score_separation = menu.create_text((NbC * C + x0) / 5.0, 575, text="-", font = ("Courier",35),fill = 'black')

	create_grille()
	button()

	can.event_add('<<panic>>', '<Motion>', '<ButtonRelease>')
	can.bind('<Button-1>', create_rect)
	can.bind('<Button-3>', return_rectangle)
	can.bind('<<panic>>', mvt_rect)

	root.mainloop()

launch_game()
