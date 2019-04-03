from main import *

W, H = NbC*C, NbC*C
WE, HE = 300, NbC*C
WC = W + WE
M = WC/2

player_1 = PhotoImage(file='images/player_1.gif')
player_2 = PhotoImage(file='images/player_2.gif')
text_duellum = PhotoImage(file='images/text_duellum.gif')
text_jouer = PhotoImage(file='images/text_jouer.gif')
text_options = PhotoImage(file='images/text_options.gif')
text_quitter = PhotoImage(file='images/text_quitter.gif')
text_copyright = PhotoImage(file='images/text_copyright.gif')
text_retour = PhotoImage(file='images/text_retour.gif')
color_background = 'gainsboro'

def menu():
    global can
    can = Canvas(root, width = WC, height = H, highlightbackground = 'black', highlightcolor = 'black', cursor = 'circle', highlightthickness = 2, bd = 0)
    can.pack()
    can['bg'] = color_background
    
    b_play = Button(can, image = text_jouer)
    b_play_window = can.create_window(M, H/2.75, anchor = 'center', width = 200, window = b_play)
    b_play.configure(bg = color_background, pady = 15, relief = FLAT, command = lambda : start_game())

    b_option = Button(can, image = text_options)
    b_option_window = can.create_window(M, H/1.75, anchor = 'center', width = 200, window = b_option)
    b_option.configure(bg = color_background, pady = 15, relief = FLAT, command = option)

    b_exit = Button(can, image = text_quitter)
    b_exit_window = can.create_window(M, H/1.75 + (H/1.75 - H/2.75), anchor = 'center', width = 200 , window = b_exit)
    b_exit.configure(bg = color_background, relief = FLAT, command = lambda : close_window(root))

    text_copyright_img = can.create_image(W+225, H-20, image = text_copyright, anchor = 'center')
    texte_duellum_img = can.create_image(M, H/6, image = text_duellum, anchor = 'center')

def option():
    global win
    can.destroy()
    win = Canvas(root, width = WC, height = H, highlightbackground = 'black', highlightcolor = 'black', cursor = 'circle', highlightthickness = 2, bd = 0)
    win.pack()
    win['bg'] = color_background
    
    b_grille = Button(win, text="GRILLE")
    b_grille_window = win.create_window(M, H/2.90, anchor = 'center', width = 200, window = b_grille)
    b_grille.configure(bg = color_background, pady = 15, relief = FLAT, command = grille )

    b_obstacles = Button(win,text="OBSTACLES")
    b_obstacles_window = win.create_window(M,H/2.15, anchor = 'center', width= 200, window = b_obstacles)
    b_obstacles.configure(bg = color_background, pady = 15, relief = FLAT, command = obstacles)

    b_dices = Button(win,text="DÉS")
    b_dices_window = win.create_window(M,H/1.75, anchor = 'center', width= 200, window = b_dices)
    b_dices.configure(bg = color_background, pady = 15, relief = FLAT, command = dices)

    def close_option(root):
        win.destroy()
        menu()

    b_close = Button(win, image = text_retour)
    b_close_window = win.create_window(M, H/1.75 + (H/1.75 - H/2.75), anchor = 'center', width = 200, window = b_close)
    b_close.configure(bg = color_background, pady = 30, relief = FLAT, command = lambda : close_option(root))
    texte_copyright_img = win.create_image(W+225, H-20, image = text_copyright, anchor = 'center')

    root.mainloop()

def grille():
    global win
    win.destroy()
    win = Canvas (root, width = WC, height = H, highlightbackground = 'black', highlightcolor = 'black', cursor = 'circle', highlightthickness = 2, bd = 0)
    win.pack()
    win['bg'] = color_background

    b_grille_e = Button(win, text="EASY")
    b_grille_e_window = win.create_window(M, H/2.90, anchor = 'center', width = 200, window = b_grille_e)
    b_grille_e.configure(bg = color_background, pady = 15, relief = FLAT, command = lambda : easy_level())
    
    b_grille_n = Button(win, text="NORMAL")
    b_grille_n_window = win.create_window(M, H/2.15, anchor = 'center', width = 200, window = b_grille_n)
    b_grille_n.configure(bg = color_background, pady = 15, relief = FLAT, command = lambda: normal_level())

    b_grille_h = Button(win, text="HARD")
    b_grille_h_window = win.create_window(M, H/1.75, anchor = 'center', width = 200, window = b_grille_h)
    b_grille_h.configure(bg = color_background, pady = 15, relief = FLAT, command = lambda : hard_level())
    
    def close_grille(root):
        win.destroy()
        option()

    b_close = Button(win, image = text_retour)
    b_close_window = win.create_window(M, H/1.75 + (H/1.75 - H/2.75), anchor = 'center', width = 200, window = b_close)
    b_close.configure(bg = color_background, pady = 30, relief = FLAT, command = lambda : close_grille(root))
    texte_copyright_img = win.create_image(W+225, H-20, image = text_copyright, anchor = 'center')

    root.mainloop()

def obstacles():
    global win
    win.destroy()
    win = Canvas (root, width = WC, height = H, highlightbackground = 'black', highlightcolor = 'black', cursor = 'circle', highlightthickness = 2, bd = 0)
    win.pack()
    win['bg'] = color_background

    b_obstacles_oui = Button(win, text="ACTIVE")
    b_obstacles_oui_window = win.create_window(M, H/2.90, anchor = 'center', width = 200, window = b_obstacles_oui)
    b_obstacles_oui.configure(bg = color_background, pady = 15, relief = FLAT, command = lambda : activation_obstacle())
    
    b_obstacles_non = Button(win, text="DESACTIVE")
    b_obstacles_non_window = win.create_window(M, H/2.15, anchor = 'center', width = 200, window = b_obstacles_non)
    b_obstacles_non.configure(bg = color_background, pady = 15, relief = FLAT, command = lambda: desactive_obstacle())


    
    def close_obstacles(root):
        win.destroy()
        option()

    b_close = Button(win, image = text_retour)
    b_close_window = win.create_window(M, H/1.75 + (H/1.75 - H/2.75), anchor = 'center', width = 200, window = b_close)
    b_close.configure(bg = color_background, pady = 30, relief = FLAT, command = lambda : close_obstacles(root))
    texte_copyright_img = win.create_image(W+225, H-20, image = text_copyright, anchor = 'center')

    root.mainloop()

def dices():
    global win
    win.destroy()
    win = Canvas (root, width = WC, height = H, highlightbackground = 'black', highlightcolor = 'black', cursor = 'circle', highlightthickness = 2, bd = 0)
    win.pack()
    win['bg'] = color_background

    b_dices_3 = Button(win, text="Dés à 3 faces")
    b_dices_3_window = win.create_window(M, H/2.90, anchor = 'center', width = 200, window = b_dices_3)
    b_dices_3.configure(bg = color_background, pady = 15, relief = FLAT, command = lambda : dice_3())
    
    b_dices_6 = Button(win, text="Dés à 6 faces")
    b_dices_6_window = win.create_window(M, H/2.15, anchor = 'center', width = 200, window = b_dices_6)
    b_dices_6.configure(bg = color_background, pady = 15, relief = FLAT, command = lambda: dice_6())

    b_dices_9 = Button(win, text="Dés à 9 faces")
    b_dices_9_window = win.create_window(M, H/1.75, anchor = 'center', width = 200, window = b_dices_9)
    b_dices_9.configure(bg = color_background, pady = 15, relief = FLAT, command = lambda : dice_9())


    
    def close_dices(root):
        win.destroy()
        option()

    b_close = Button(win, image = text_retour)
    b_close_window = win.create_window(M, H/1.75 + (H/1.75 - H/2.75), anchor = 'center', width = 200, window = b_close)
    b_close.configure(bg = color_background, pady = 30, relief = FLAT, command = lambda : close_dices(root))
    texte_copyright_img = win.create_image(W+225, H-20, image = text_copyright, anchor = 'center')

    root.mainloop()
    
def close_window(root):
    root.destroy()

def start_game():
    can.pack_forget()
    launch_game()

menu()
root.mainloop()
