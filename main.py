from tkinter import *
from random import randint
from tkinter import messagebox
import subprocess

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
first_attempt_j1 = 0				#Variable qui détermine les 2 premiers coups de la partie
first_attempt_j2 = 0				#Variable qui détermine les 2 premiers coups de la partie
score_joueur1 = 0					#??
score_joueur2 = 0					#??
scorej1 = 0							#??
scorej2 = 0							#??
check_list_map = []					#Liste qui contient la carte ou sont placés les rectangles
color_j1 = 'red'					#Variable qui contient la couleur du joueur 1
color_j2 = 'blue'					#Variable qui contient la couleur du joueur 2
activate_obs = 0					#Variable qui indique si les obstacles doivent être placés
range_dice = 6
size_obs_compt = 1

root = Tk()
root.title("Duellum")
root.resizable(False, False)

empty_crown = PhotoImage(file='images/empty_crown.gif')
red_crown = PhotoImage(file='images/red_crown.gif')
blue_crown = PhotoImage(file='images/blue_crown.gif')


def easy_level():
	global NbC, C, size_obs_compt
	size_obs_compt = 1
	NbC = 20
	C = 40

def normal_level():
	global NbC, C, size_obs_compt
	size_obs_compt = 2
	NbC = 20*size_obs_compt
	C = 40//size_obs_compt

def hard_level():
	global NbC, C, size_obs_compt
	size_obs_compt = 3
	NbC = 20*size_obs_compt
	C = 40//size_obs_compt

def activation_obstacle():
	global activate_obs
	activate_obs = 1

def desactive_obstacle():
	global activate_obs
	activate_obs = 0
	
def modif_dices(nb):
	global range_dice
	if nb == 3:
		range_dice = 3
	if nb == 6:
		range_dice = 6
	if nb == 9:
		range_dice = 9

def launch_game(): #LANCEMENT DU PROGRAMME PRINCIPALE
	can = Canvas(root, bg = 'white', height = (NbC * C + x0), width = (NbC * C + y0))
	can.pack(side = LEFT)
	menu = Canvas(root, bg = 'white', height = (NbC * C + x0), width = 300)
	menu.pack(side = RIGHT)

	crown_img = menu.create_image(300/2, (NbC * C + x0) / 5, image = empty_crown, anchor='center')

	def create_grille(): #FONCTION POUR CREER LA GRILLE
		for i in range(NbC + 1):
			can.create_line(x0 + C * i, y0, x0 + C * i, y0 + NbC * C, width = 1)
			can.create_line(x0, y0 + C * i, x0 + NbC * C, y0 + C * i, width = 1)

	def make_dice(): #FONCTION POUR CREER LES DES
		global remove_dice, nb_de1, nb_de2, state_launch, nb_shot, range_dice
		nb_de1, nb_de2 = randint(1, range_dice), randint(1, range_dice)
		x1, x2 = (NbC * C) / 6 - 30, (NbC * C) / 6 + 30
		y, r = 350, 10
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
		if nb_de1 == 7:		#DE1 FACE7
			dots.append(menu.create_oval(x1, y, x1 + r, y + r, fill='black'))
			dots.append(menu.create_oval(x1 + 32, y, (x1 + 32) + r, y + r, fill='black'))
			dots.append(menu.create_oval(x1, y + 16, x1 + r, (y + 16) + r, fill='black'))
			dots.append(menu.create_oval(x1 + 32, (y + 16), (x1 + 32) + r, (y + 16) + r, fill='black'))
			dots.append(menu.create_oval(x1, y + 32, x1 + r, (y + 32) + r, fill='black'))
			dots.append(menu.create_oval(x1 + 32, y + 32, (x1 + 32) + r, (y + 32) + r, fill='black'))
			dots.append(menu.create_oval(x1 + 16, (y + 16), (x1 + 16) + r, (y + 16) + r, fill='black'))
		if nb_de2 == 7:		#DE2 FACE7
			dots.append(menu.create_oval(x2, y, x2 + r, y + r, fill='black'))
			dots.append(menu.create_oval(x2 + 32, y, (x2 + 32) + r, y + r, fill='black'))
			dots.append(menu.create_oval(x2, y + 16, x2 + r, (y + 16) + r, fill='black'))
			dots.append(menu.create_oval(x2 + 32, (y + 16), (x2 + 32) + r, (y + 16) + r, fill='black'))
			dots.append(menu.create_oval(x2, y + 32, x2 + r, (y + 32) + r, fill='black'))
			dots.append(menu.create_oval(x2 + 32, y + 32, (x2 + 32) + r, (y + 32) + r, fill='black'))
			dots.append(menu.create_oval(x2 + 16, (y + 16), (x2 + 16) + r, (y + 16) + r, fill='black'))
		if nb_de1 == 8:		#DE1 FACE8
			dots.append(menu.create_oval(x1, y, x1 + r, y + r, fill='black'))
			dots.append(menu.create_oval(x1 + 32, y, (x1 + 32) + r, y + r, fill='black'))
			dots.append(menu.create_oval(x1, y + 16, x1 + r, (y + 16) + r, fill='black'))
			dots.append(menu.create_oval(x1 + 32, (y + 16), (x1 + 32) + r, (y + 16) + r, fill='black'))
			dots.append(menu.create_oval(x1, y + 32, x1 + r, (y + 32) + r, fill='black'))
			dots.append(menu.create_oval(x1 + 32, y + 32, (x1 + 32) + r, (y + 32) + r, fill='black'))
			dots.append(menu.create_oval(x1 + 16, y + 32, (x1 + 16) + r, (y + 32) + r, fill='black'))
			dots.append(menu.create_oval(x1 + 16, y, (x1 + 16) + r, y + r, fill='black'))
		if nb_de2 == 8:		#DE1 FACE8
			dots.append(menu.create_oval(x2, y, x2 + r, y + r, fill='black'))
			dots.append(menu.create_oval(x2 + 32, y, (x2 + 32) + r, y + r, fill='black'))
			dots.append(menu.create_oval(x2, y + 16, x2 + r, (y + 16) + r, fill='black'))
			dots.append(menu.create_oval(x2 + 32, (y + 16), (x2 + 32) + r, (y + 16) + r, fill='black'))
			dots.append(menu.create_oval(x2, y + 32, x2 + r, (y + 32) + r, fill='black'))
			dots.append(menu.create_oval(x2 + 32, y + 32, (x2 + 32) + r, (y + 32) + r, fill='black'))
			dots.append(menu.create_oval(x2 + 16, y + 32, (x2 + 16) + r, (y + 32) + r, fill='black'))
			dots.append(menu.create_oval(x2 + 16, y, (x2 + 16) + r, y + r, fill='black'))
		if nb_de1 == 9:		#DE1 FACE9
			dots.append(menu.create_oval(x1, y, x1 + r, y + r, fill='black'))
			dots.append(menu.create_oval(x1 + 32, y, (x1 + 32) + r, y + r, fill='black'))
			dots.append(menu.create_oval(x1, y + 16, x1 + r, (y + 16) + r, fill='black'))
			dots.append(menu.create_oval(x1 + 32, (y + 16), (x1 + 32) + r, (y + 16) + r, fill='black'))
			dots.append(menu.create_oval(x1, y + 32, x1 + r, (y + 32) + r, fill='black'))
			dots.append(menu.create_oval(x1 + 32, y + 32, (x1 + 32) + r, (y + 32) + r, fill='black'))
			dots.append(menu.create_oval(x1 + 16, y + 32, (x1 + 16) + r, (y + 32) + r, fill='black'))
			dots.append(menu.create_oval(x1 + 16, y, (x1 + 16) + r, y + r, fill='black'))
			dots.append(menu.create_oval(x1 + 16, y + 16, (x1 + 16) + r, (y + 16) + r, fill='black'))
		if nb_de2 == 9:		#DE1 FACE9
			dots.append(menu.create_oval(x2, y, x2 + r, y + r, fill='black'))
			dots.append(menu.create_oval(x2 + 32, y, (x2 + 32) + r, y + r, fill='black'))
			dots.append(menu.create_oval(x2, y + 16, x2 + r, (y + 16) + r, fill='black'))
			dots.append(menu.create_oval(x2 + 32, (y + 16), (x2 + 32) + r, (y + 16) + r, fill='black'))
			dots.append(menu.create_oval(x2, y + 32, x2 + r, (y + 32) + r, fill='black'))
			dots.append(menu.create_oval(x2 + 32, y + 32, (x2 + 32) + r, (y + 32) + r, fill='black'))
			dots.append(menu.create_oval(x2 + 16, y + 32, (x2 + 16) + r, (y + 32) + r, fill='black'))
			dots.append(menu.create_oval(x2 + 16, y, (x2 + 16) + r, y + r, fill='black'))
			dots.append(menu.create_oval(x2 + 16, y + 16, (x2 + 16) + r, (y + 16) + r, fill='black'))
		remove_dice += 1
		nb_shot = 0
		return nb_de1, nb_de2

	def create_rect(evtX, evtY): #FONCTION POUR CREER LES RECTANGLES
		global player, nb_shot, state_launch
		if nb_shot == 0:
			complet_list_map(evtX, evtY)
			if player == 1 and abandon_j1 != 1:		#CREER LE RECTANGLE POUR LE J1
				rect_list.append(can.create_rectangle(evtX // C * C + x0, evtY // C * C + y0, nb_de1 * C + evtX // C * C + x0, nb_de2 * C + evtY // C * C + y0, fill = color_j1))
				can.create_text(nb_de1 / 2 * C + evtX // C * C, nb_de2 / 2 * C + evtY // C * C, text = nb_de1 * nb_de2, anchor = CENTER, fill = 'gainsboro')
				if abandon_j2 != 1:
					player += 1
			elif player == 2 and abandon_j2 != 1:	#CREER LE RECTANGLE POUR LE J2
				rect_list.append(can.create_rectangle((evtX + C) // C * C + x0, (evtY + C) // C * C + y0, - nb_de1 * C + (evtX + C) // C * C + x0, - nb_de2 * C + (evtY + C) // C * C + y0, fill = color_j2))
				can.create_text(- nb_de1 / 2 * C + (evtX + C) // C * C, - nb_de2 / 2 * C + (evtY + C) // C * C, text = nb_de1 * nb_de2, anchor = CENTER, fill = 'gainsboro')
				if abandon_j1 != 1: 
					player -= 1
			nb_shot += 1
			state_launch = NORMAL
			button()
			score()

	def create_obstacle():
		global size_obs_1, size_obs_2
		if activate_obs == 1:
			color_obs = 'gray16'
			size_obs_1 = randint(2 * size_obs_compt, 4 * size_obs_compt)
			size_obs_2 = randint(2 * size_obs_compt, 4 * size_obs_compt)
			px0, py0 = (NbC//2 * C + x0), (NbC//2 * C + y0)
			rect_list.append(can.create_rectangle(px0 - C * size_obs_1, py0 - C * size_obs_1, px0, py0, fill = color_obs))
			rect_list.append(can.create_rectangle(px0 + C * size_obs_1, py0 + C * size_obs_1, px0, py0, fill = color_obs))
			rect_list.append(can.create_rectangle(px0 + C * size_obs_2, py0 - C * size_obs_2, px0, py0, fill = color_obs))
			rect_list.append(can.create_rectangle(px0 - C * size_obs_2, py0 + C * size_obs_2, px0, py0, fill = color_obs))
			complet_list_map(px0, py0)

	def complet_list_map(evtX, evtY):
		if activate_obs > 0:	#MODIFIE LA CARTE POUR LES OBSTACLES
			for i in range(size_obs_1):
				for k in range(size_obs_1):
					check_list_map[NbC//2 + k][NbC//2 + i] = 9
					check_list_map[NbC//2 - 1 - k][NbC//2 - 1 - i] = 9
				k = 0
			for i in range(size_obs_2):
				for k in range(size_obs_2):
					check_list_map[NbC//2 + k][NbC//2 - 1 - i] = 6
					check_list_map[NbC//2 - 1 - k][NbC//2 + i] = 6
				k = 0
		if player == 1 and abandon_j1 == 0 or abandon_j2 != 0: #MODIFIE LA CARTE POUR LE JOUEUR 1
			for nb_1 in range(nb_de1):
				for nb_2 in range(nb_de2):
					check_list_map[evtY // C + nb_2][evtX // C + nb_1] = 1
				check_list_map[evtY // C + nb_2][evtX // C + nb_1] = 1
				nb_2 = 0
		if player == 2 and abandon_j2 == 0 or abandon_j1 != 0: #MODIFIE LA CARTE POUR LE JOUEUR 2
			for nb_1 in range(nb_de1):
				for nb_2 in range(nb_de2):
					check_list_map[evtY // C - nb_2][evtX // C - nb_1] = 2
				check_list_map[evtY // C - nb_2][evtX // C - nb_1] = 2
				nb_2 = 0
		#print(check_list_map)

	def check_error_rect(evt): #FONCTION QUI REGARDE SI LE RECTANGLE PEUT ETRE PLACE
		global first_attempt_j1, first_attempt_j2
		placement_error = 0
		check_contour = 0
		evtX, evtY = evt.x, evt.y
		if evtY // C == 0 and evtX // C == 0 and player == 1: #OBLIGE LE PREMIER COUP A ETRE AU COIN SUPERIEUR GAUCHE J1
			first_attempt_j1 += 1
			check_contour += 1
		if evtY // C == NbC - 1 and evtX // C == NbC - 1 and player == 2: #OBLIGE LE PREMIER COUP A ETRE AU COIN INFERIEUR DROITE J2
			first_attempt_j2 += 1
			check_contour += 1
		if state_launch != NORMAL and evtY // C < NbC and evtX // C < NbC:
			for nb_1 in range(nb_de1):
				for nb_2 in range(nb_de2):
					if player == 1: #FONCTION J1
						if check_list_map[evtY // C + nb_2][evtX // C + nb_1] != 0 or check_list_map[evtY // C + nb_2][evtX // C + nb_1] != 0:
							#VERIFIE SI LE RECTANGLE EN TOUCHE AUCUN
							placement_error += 1
						if check_list_map[evtY // C + nb_2 + 1][evtX // C + nb_1] == 1 or check_list_map[evtY // C + nb_2][evtX // C + nb_1 + 1] == 1 or check_list_map[evtY // C + nb_2 - 1][evtX // C + nb_1] == 1 or check_list_map[evtY // C + nb_2][evtX // C + nb_1 - 1] == 1:
							#VERIFIE SI LE RECTANGLE EST PROCHE D'UN AUTRE RECTANGLE
							check_contour += 1
					if player == 2: #FONTION J2
						if check_list_map[evtY // C - nb_2][evtX // C - nb_1] != 0 or check_list_map[evtY // C - nb_2][evtX // C - nb_1] != 0:
							#VERIFIE SI LE RECTANGLE EN TOUCHE AUCUN
							placement_error += 1
						if check_list_map[evtY // C - nb_2 + 1][evtX // C - nb_1] == 2 or check_list_map[evtY // C - nb_2][evtX // C - nb_1 + 1] == 2 or check_list_map[evtY // C - nb_2 - 1][evtX // C - nb_1] == 2 or check_list_map[evtY // C - nb_2][evtX // C - nb_1 - 1] == 2:
							#VERIFIE SI LE RECTANGLE EST PROCHE D'UN AUTRE RECTANGLE
							check_contour += 1
				nb_2 = 0
		if nb_de1 > 0 and nb_de2 > 0 and placement_error == 0 and check_contour > 0:
			if first_attempt_j1 > 0 and player == 1 or first_attempt_j2 > 0 and player == 2:
				create_rect(evtX, evtY)

	def create_list_map(): #FONCTION QUI CREER LA CARTE
		for i in range(NbC + 1):
			check_list_map.append([0] * (NbC+1))
			if i == NbC:
				for i in range(NbC + 1): #CREER UNE LIGNE SUPPLEMENTAIRE EN BAS ET A GAUCHE POUR EMPECHER LES ERREURS
					check_list_map[i][NbC] = 9
					check_list_map[NbC][i] = 9

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
			if bn == 'no':
					menu.destroy()
					can.destroy()
					root.destroy()
			if bn == 'yes':
					menu.destroy()
					can.destroy()
					root.destroy()
					subprocess.call(["python.exe", "main_menu.py"])
		state_launch = NORMAL
		button()
		return player

	def return_rectangle(evt): #FONCTION POUR RETOURNER LE RECTANGLE
		global nb_de1, nb_de2
		nb_de1, nb_de2 = nb_de2, nb_de1
		root.event_generate('<Motion>')

	def button(): #BUTTON POUR LANCER LES DES
		roll_button = Button(menu, state = state_launch, text = "Lancer dés")
		roll_button_win = menu.create_window(150, (NbC * C + x0) / 1.75, anchor = 'center', height = 50, width = 150, window = roll_button)
		roll_button.configure(bg = 'grey', relief = FLAT, command = make_dice)

	def mvt_rect(evt): #FONCTION QUI CREE UN RECTANGLE SOUS LE CURSEUR DE LA SOURIS
		reduc = 5
		for i in range(len(moving_rect)):
			can.delete(moving_rect[i])
		if player == 1 and state_launch == DISABLED:
			moving_rect.append(can.create_rectangle(evt.x - reduc, evt.y - reduc, nb_de1 * C + evt.x + x0 - reduc, nb_de2 * C + evt.y + y0 - reduc, fill = color_j1))
		if player == 2 and state_launch == DISABLED:
			moving_rect.append(can.create_rectangle(evt.x + reduc, evt.y + reduc, - nb_de1 * C + evt.x + x0 + reduc, - nb_de2 * C + evt.y + y0 + reduc, fill = color_j2))

	def score(): #FONCTION QUI AFFICHE LES SCORES
		global score_joueur1, score_joueur2, scorej1, scorej2
		if player == 2 and abandon_j1 == 0 or abandon_j2 == 1:
			scorej1 += nb_de1 * nb_de2
			menu.delete(score_joueur1)
			score_joueur1 = menu.create_text(75, (NbC * C + x0) / 1.4, text = scorej1, font = ("Courier",35),fill = color_j1)
			menu.itemconfigure(score_joueur1, text = str(scorej1))
		if player == 1 and abandon_j2 == 0 or abandon_j1 == 1:
			scorej2 += nb_de1 * nb_de2
			menu.delete(score_joueur2)
			score_joueur2 = menu.create_text(225, (NbC * C + x0) / 1.4, text = scorej2, font = ("Courier",35),fill = color_j2)
			menu.itemconfigure(score_joueur2, text = str(scorej2))
		if scorej1 > scorej2:
			crown_img = menu.create_image(300/2, (NbC * C + x0) / 5, image = red_crown, anchor='center')
		if scorej2 > scorej1:
			crown_img = menu.create_image(300/2, (NbC * C + x0) / 5, image = blue_crown, anchor='center')


	give_up_button = Button(menu, text = "Abandonner")
	give_up_button_win = menu.create_window(150, (NbC * C + x0) / 1.1, anchor = 'center', height = 50, width = 150, window = give_up_button)
	give_up_button.configure(bg = 'grey', relief = FLAT, command = give_up)

	score_separation = menu.create_text(150, (NbC * C + x0) / 1.4, text="-", font = ("Courier",35),fill = 'black')

	create_list_map()
	create_obstacle()
	create_grille()
	button()

	can.event_add('<<panic>>', '<Motion>', '<ButtonRelease>')
	can.bind('<Button-1>', check_error_rect)
	can.bind('<Button-3>', return_rectangle)
	can.bind('<<panic>>', mvt_rect)

	root.mainloop()

#launch_game()
