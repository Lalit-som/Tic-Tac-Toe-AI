from tkinter import *
import tkinter.messagebox


#.......functions...........
def changeLevel():
    print ("Amater")

#change git
def showmessage():
    tkinter.messagebox.showinfo('About Tic Tac Toe','Made by Lalit Som\n version 1.0.0\nHow to play: Go check wikipedia')



def motion(event):
    _x, _y = event.x, event.y
    if (_x>50 and _x<390 and _y>50 and _y<390 and abs(_x-170)>10 and abs(_x-290)>10 and abs(_y-160)>10 and abs(_y-290)>10 ):

        if(_x<170 and _x>50):
            _x=0
        if(_x<290 and _x>170):
            _x=1
        if(_x<390 and _x>290):
            _x=2

        if(_y<160 and _y>50):
            _y=0
        if(_y<290 and _y>160):
            _y=1
        if(_y<390 and _y>290):
            _y=2

        user_clicked(_y,_x)


def reset_game(event):
    global g_gameEnd

    g_player1 =0 #red one
    g_winner =-1

    g_gameEnd=0
    g_chance=0
    for i in range(3):
        for j in range(3):
            g_game_grid[i][j]=-1

    bgcanvas.delete("all")
    board_img = bgcanvas.create_image(b_image_pos,b_image_pos,image=object_img_board)
    g_menu_level = 1
    g_menu_playas = 0





def user_clicked(_r,_c):
    global g_gameEnd
    if(g_gameEnd==0 and g_game_grid[_r][_c] ==-1 ):
        g_game_grid[_r][_c] = g_player1
        put_piece(g_player1,_r,_c)
        _stat = check_game_status()
        if(_stat==-1):
            runai(g_player1)
        else:
            print (check_game_status())
            g_gameEnd = 1



def put_piece(_player,_r,_c):
    if(_player == 0):
        _image = bgcanvas.create_image(img_pos_x +(_c*offset),img_pos_y + (_r*offset),image=object_img_red)
    else:
        _image = bgcanvas.create_image(img_pos_x +(_c*offset),img_pos_y + (_r*offset),image=object_img_blue)


def check_game_status():

    for i in range(3):
        if( g_game_grid[i][0] == g_game_grid[i][1] and g_game_grid[i][1] == g_game_grid[i][2] and g_game_grid[i][2] != -1  ):
            return g_game_grid[i][2]

    for i in range(3):
        if( g_game_grid[0][i] == g_game_grid[1][i] and g_game_grid[1][i] == g_game_grid[2][i] and g_game_grid[2][i] != -1  ):
            return g_game_grid[2][i]

    if( g_game_grid[0][0] == g_game_grid[1][1] and g_game_grid[1][1] == g_game_grid[2][2] and g_game_grid[2][2] != -1  ):
        return g_game_grid[2][2]

    if( g_game_grid[0][2] == g_game_grid[1][1] and g_game_grid[1][1] == g_game_grid[2][2] and g_game_grid[2][0] != -1  ):
        return g_game_grid[2][0]

    return -1







def runai(_user):
    _ai = 1
    if(_user == 1):
        _ai =1











"""
_player1 =0 #red one
_winner =-1
_gameEnd=0
_chance=0
_game_grid = [[-1] *3 for n in range(3)] #initial state
_menu_level = 1
_menu_playas = 0
"""







#...........main window...........

mainWnd = Tk()
mainWnd.wm_title("Tic Tac Toe")
mainWnd.iconbitmap("icon.ico")

#mainWnd.wm_attributes('-transparentcolor','pink')

#.............toolbar.............

menu_bar = Menu(mainWnd, tearoff=False)
mainWnd.config(menu = menu_bar)


submenu_levels = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Levels",menu=submenu_levels)
submenu_levels.add_command(label="*Moron", command = changeLevel);
submenu_levels.add_command(label="Pro", command = changeLevel);
submenu_levels.add_command(label="Legend", command = changeLevel);



submenu_player = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Play as..",menu=submenu_player)
submenu_player.add_command(label="*Player 1 X", command = changeLevel);
submenu_player.add_command(label="Player 2 O", command = changeLevel);
submenu_player.add_command(label="Random", command = changeLevel);



menu_bar.add_command(label="About", command=showmessage)



#.............options frame.............

option_frame = Frame(mainWnd, bg="#21252b", height="450", width="170",highlightthickness=1,highlightbackground ="#1a181f", relief=RAISED,pady =30 )
option_frame.pack(side=LEFT, fill=None, expand=False)
option_frame.pack_propagate(0)

game_name = Label(option_frame, text="T I C  T A C  T O E\n",bg ="#21252b",fg="#e97263", font=("Arial","13","bold"))
game_name.pack();

restart_btn = Button(option_frame, text="PLAY", font=("Helvetica","17","bold"),bg ="#4285fa", fg ="white",bd=0)
restart_btn.pack()
restart_btn.config(height=1, width=7)
restart_btn.bind('<Button-1>', reset_game)

level_info = Label(option_frame, text="Level : Moron",bg ="#21252b",fg="#9da5b4", font=("Arial","11"),pady=15)
level_info.pack();



player_info = Label(option_frame, text="You are Player X\n\n",bg ="#21252b",fg="#9da5b4", font=("Arial","11"))
player_info.pack();


ai_msg = Label(option_frame, text="Hey!\n Wanna Play? \n",bg ="#21252b",fg="#4285fa", font=("Arial","11"))
ai_msg.pack();


game_stat = Label(option_frame, text="You Won\n",bg ="#21252b",fg="green", font=("Arial","11"))
game_stat.pack(side=BOTTOM);



#.............game frame.............

game_frame = Frame(mainWnd, bg="#282c34", height="450", width="450", relief=SUNKEN)
game_frame.pack_propagate(0)
game_frame.pack(side=LEFT)


#.................main canvas..............
canvas_size =450
bgcanvas = Canvas(game_frame, width=canvas_size,height=canvas_size,highlightthickness=0,bg="#282c34")
bgcanvas.pack()
bgcanvas.bind('<Button-1>', motion)

#.............background_image.............
object_img_board = PhotoImage(file="tictactoeboard.png")
b_image_pos = canvas_size/2
board_img = bgcanvas.create_image(b_image_pos,b_image_pos,image=object_img_board)
#.............objects on board.............

object_img_red = PhotoImage(file="red.png")
object_img_blue = PhotoImage(file="blue.png")

img_pos_x =100
img_pos_y=100

offset = 126

#...................game vars....................

g_player1 =0 #red one
g_winner =-1
g_gameEnd=0
g_chance=0
g_game_grid = [[-1] *3 for n in range(3)] #initial state
g_menu_level = 1
g_menu_playas = 0


#.....................................
mainWnd.resizable(width=False, height =False)
mainWnd.mainloop()
