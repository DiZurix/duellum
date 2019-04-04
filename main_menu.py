from main import *

W, H = NbC*C, NbC*C
WE, HE = 300, NbC*C
WC = W + WE
M = WC/2

player_1red = PhotoImage(file='images/player_1red.gif')
player_1blue = PhotoImage(file='images/player_1blue.gif')
player_1cyan = PhotoImage(file='images/player_1cyan.gif')
player_1green = PhotoImage(file='images/player_1green.gif')
player_1pink = PhotoImage(file='images/player_1pink.gif')
player_1violet = PhotoImage(file='images/player_1violet.gif')
player_1yellow = PhotoImage(file='images/player_1yellow.gif')

player_2red = PhotoImage(file='images/player_2red.gif')
player_2blue = PhotoImage(file='images/player_2blue.gif')
player_2cyan = PhotoImage(file='images/player_2cyan.gif')
player_2green = PhotoImage(file='images/player_2green.gif')
player_2pink = PhotoImage(file='images/player_2pink.gif')
player_2violet = PhotoImage(file='images/player_2violet.gif')
player_2yellow = PhotoImage(file='images/player_2yellow.gif')

text_duellum = PhotoImage(file='images/text_duellum.gif')
text_jouer = PhotoImage(file='images/text_jouer.gif')
text_options = PhotoImage(file='images/text_options.gif')
text_quitter = PhotoImage(file='images/text_quitter.gif')
text_copyright = PhotoImage(file='images/text_copyright.gif')
text_retour = PhotoImage(file='images/text_retour.gif')
text_des = PhotoImage(file='images/text_des.gif')
text_grille = PhotoImage(file='images/text_grille.gif')
text_obstacle = PhotoImage(file='images/text_obstacle.gif')
grille_easy = PhotoImage (file='images/grille_easy.gif')
grille_normal = PhotoImage (file='images/grille_normal.gif')
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
    player_1red_img = can.create_image(M/2.1, H/6, image = player_1red, anchor = 'center')
    player_2blue_img = can.create_image(M*1.5, H/6, image = player_2blue, anchor = 'center')

def option():
    global win
    can.destroy()
    win = Canvas(root, width = WC, height = H, highlightbackground = 'black', highlightcolor = 'black', cursor = 'circle', highlightthickness = 2, bd = 0)
    win.pack()
    win['bg'] = color_background

    b_colors = Button(win, text="Couleurs joueurs")
    b_colors_window = win.create_window(M, H/6.5, anchor = 'center', width = 200, window = b_colors)
    b_colors.configure(bg = color_background, pady = 15, relief = FLAT, command = lambda : None)

    b_grille = Button(win, image = text_grille)
    b_grille_window = win.create_window(M, H/3.5, anchor = 'center', width = 200, window = b_grille)
    b_grille.configure(bg = color_background, pady = 15, relief = FLAT, command = grille)

    b_obstacles = Button(win,image = text_obstacle)
    b_obstacles_window = win.create_window(M,H/2.25, anchor = 'center', width= 200, window = b_obstacles)
    b_obstacles.configure(bg = color_background, pady = 15, relief = FLAT, command = obstacles)

    b_dices = Button(win,image = text_des)
    b_dices_window = win.create_window(M,H/1.65, anchor = 'center', width= 200, window = b_dices)
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

    b_grille_e = Button(win, image = grille_easy)
    b_grille_e_window = win.create_window(M/2.90, H/2.55, anchor = 'center', width = 296, window = b_grille_e)
    b_grille_e.configure(bg = color_background, pady = 15, relief = FLAT, command = lambda : easy_level())
    
    b_grille_n = Button(win, image = grille_normal)
    b_grille_n_window = win.create_window(M, H/2.55, anchor = 'center', width = 296, window = b_grille_n)
    b_grille_n.configure(bg = color_background, pady = 15, relief = FLAT, command = lambda: normal_level())

    b_grille_h = Button(win, text="HARD")
    b_grille_h_window = win.create_window(M*2, H/1.75, anchor = 'center', width = 200, window = b_grille_h)
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
    b_obstacles_non.configure(bg = color_background, pady = 15, relief = FLAT, command = lambda : desactive_obstacle())

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
    b_dices_3.configure(bg = color_background, pady = 15, relief = FLAT, command = lambda : modif_dices(3))

    b_dices_6 = Button(win, text="Dés à 6 faces")
    b_dices_6_window = win.create_window(M, H/2.15, anchor = 'center', width = 200, window = b_dices_6)
    b_dices_6.configure(bg = color_background, pady = 15, relief = FLAT, command = lambda: modif_dices(6))

    b_dices_9 = Button(win, text="Dés à 9 faces")
    b_dices_9_window = win.create_window(M, H/1.75, anchor = 'center', width = 200, window = b_dices_9)
    b_dices_9.configure(bg = color_background, pady = 15, relief = FLAT, command = lambda : modif_dices(9))

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
