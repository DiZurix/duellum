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
    
    b_difficulty = Button(win, text="Difficulté")
    b_difficulty_window = win.create_window(M, H/2.90, anchor = 'center', width = 200, window = b_difficulty)
    b_difficulty.configure(bg = color_background, pady = 15, relief = FLAT, command = difficulty )

    def close_option(root):
        win.destroy()
        menu()

    b_close = Button(win, image = text_retour)
    b_close_window = win.create_window(M, H/1.75 + (H/1.75 - H/2.75), anchor = 'center', width = 200, window = b_close)
    b_close.configure(bg = color_background, pady = 30, relief = FLAT, command = lambda : close_option(root))
    texte_copyright_img = win.create_image(W+225, H-20, image = text_copyright, anchor = 'center')

    root.mainloop()

def difficulty():
    global win
    win.destroy()
    win = Canvas (root, width = WC, height = H, highlightbackground = 'black', highlightcolor = 'black', cursor = 'circle', highlightthickness = 2, bd = 0)
    win.pack()
    win['bg'] = color_background

    b_difficulty_e = Button(win, text="EASY")
    b_difficulty_e_window = win.create_window(M, H/2.90, anchor = 'center', width = 200, window = b_difficulty_e)
    b_difficulty_e.configure(bg = color_background, pady = 15, relief = FLAT, command = lambda : easy_level())
    
    b_difficulty_n = Button(win, text="NORMAL")
    b_difficulty_n_window = win.create_window(M, H/2.15, anchor = 'center', width = 200, window = b_difficulty_n)
    b_difficulty_n.configure(bg = color_background, pady = 15, relief = FLAT, command = lambda: normal_level())

    b_difficulty_h = Button(win, text="HARD")
    b_difficulty_h_window = win.create_window(M, H/1.75, anchor = 'center', width = 200, window = b_difficulty_h)
    b_difficulty_h.configure(bg = color_background, pady = 15, relief = FLAT, command = lambda : hard_level())
    
    def close_difficulty(root):
        win.destroy()
        option()

    b_close = Button(win, image = text_retour)
    b_close_window = win.create_window(M, H/1.75 + (H/1.75 - H/2.75), anchor = 'center', width = 200, window = b_close)
    b_close.configure(bg = color_background, pady = 30, relief = FLAT, command = lambda : close_difficulty(root))
    texte_copyright_img = win.create_image(W+225, H-20, image = text_copyright, anchor = 'center')

    root.mainloop()
    
def close_window(root):
    root.destroy()

def start_game():
    can.pack_forget()
    launch_game()

menu()
root.mainloop()
