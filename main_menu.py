from tkinter import *

C = 64
NbC = 9 
W, H = NbC*C, NbC*C
WE, HE = 300, NbC*C
WC = W + WE
M = WC/2

root = Tk()
root.title('Duellum')
root.resizable(False, False)

player_1 = PhotoImage(file='images/player_1.gif')
player_1 = player_1.zoom(int(C/64))
player_2 = PhotoImage(file='images/player_2.gif')
player_2 = player_2.zoom(int(C/64))
text_duellum = PhotoImage(file='images/text_duellum.gif')
text_duellum = text_duellum.zoom(int(C/64))
text_jouer = PhotoImage(file='images/text_jouer.gif')
text_jouer = text_jouer.zoom(int(C/64))
text_tutoriel = PhotoImage(file='images/text_tutoriel.gif')
text_tutoriel = text_tutoriel.zoom(int(C/64))
text_quitter = PhotoImage(file='images/text_quitter.gif')
text_quitter = text_quitter.zoom(int(C/64))
text_copyright = PhotoImage(file='images/text_copyright.gif')
text_copyright = text_copyright.zoom(int(C/64))
color_background = 'gainsboro'

def menu():
	global can
	global Y
	can = Canvas(root, width = WC, height = H, highlightbackground = 'black', highlightcolor = 'black', cursor = 'circle', highlightthickness = 2, bd = 0)
	can.pack()
	can['bg'] = color_background
	
	b_play = Button(can, image = text_jouer)
	b_play_window = can.create_window(M, H/2.75, anchor = 'center', width = 200*C/64, window = b_play)
	b_play.configure(bg = color_background, pady = 15, relief = FLAT, command = lambda : start_game())

	b_tutorial = Button(can, image = text_tutoriel)
	b_tutorial_window = can.create_window(M, H/1.75, anchor = 'center', width = 200*C/64, window = b_tutorial)
	b_tutorial.configure(bg = color_background, pady = 15, relief = FLAT, command = tutorial)

	b_exit = Button(can, image = text_quitter)
	b_exit_window = can.create_window(M, H/1.75 + (H/1.75 - H/2.75), anchor = 'center', width = 200*C/64, window = b_exit)
	b_exit.configure(bg = color_background, relief = FLAT, command = lambda : close_window(root))

	text_copyright_img = can.create_image(W+225, H-20, image = text_copyright, anchor = 'center')
	texte_duellum_img = can.create_image(M, H/6, image = text_duellum, anchor = 'center')

	

def tutorial():
	can.destroy()
	win = Canvas(root, width = WC, height = H, highlightbackground = 'black', highlightcolor = 'black', cursor = 'circle', highlightthickness = 2, bd = 0)
	win.pack()
	win['bg'] = color_background

	def close_tutorial(root):
		win.destroy()
		menu()

	b_close = Button(win, image = text_quitter)
	b_close_window = win.create_window(M, H/1.75 + (H/1.75 - H/2.75), anchor = 'center', width = 200*C/64, window = b_close)
	b_close.configure(bg = color_background, pady = 30, relief = FLAT, command = lambda : close_tutorial(root))
	texte_copyright_img = win.create_image(W+225, H-20, image = text_copyright, anchor = 'center')

	root.mainloop()

def close_window(root):
    root.destroy()

def start_game():
	can.pack_forget()

menu()
root.mainloop()
