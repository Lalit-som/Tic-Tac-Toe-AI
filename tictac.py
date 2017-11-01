from tkinter import *
import tkinter.messagebox
import _thread
import time
import random

# Author Lalit Som............
# github.com/lalitsom

#.......functions...........
def changePlayer(_var,_menu):
    global g_player1
    g_player1 = _var
    _playas = ["Player 1 RED","Player 2 BLUE"]

    _menu.entryconfigure(0,label=_playas[0])
    _menu.entryconfigure(1,label=_playas[1])

    _menu.entryconfigure(_var,label=_playas[_var]+"*")
    player_info.config(text ="You are "+_playas[_var] +"\n\n" )
    reset_game(0)



def changeLevel(_var,_menu):
    global g_menu_level
    g_menu_level = _var
    _levels = ["Moron","Pro","Legend"]

    _menu.entryconfigure(0,label=_levels[0])
    _menu.entryconfigure(1,label=_levels[1])
    _menu.entryconfigure(2,label=_levels[2])


    _menu.entryconfigure(_var,label=_levels[_var]+"*")

    level_info.config(text ="Level : "+_levels[_var] )
    reset_game(0)


def update_aimsg(var):

    default = ["Common I don't have whole day",
                "It's your move. I'm waiting.....",
                "Please use your brain and move fast. I have other places to go."]

    draw = ["Keep calm It's a Tie",
            "It's a Tie. Rematch?",
            "You just got spared"]

    lost = ["My CPU is not feeling well today. That's why you won.",
            "It's your lucky day.",
            "Cheater...",
            "Do not let this match go to your head.",
            "Yeah.. you won. so what?"]

    won = ["In your face sucker.",
            "Now get ready for my slave army you brainless human.",
            "Go read a book or something. Then come to play with me",
            "You need practice ..................................................... ",
            "..and I thought you can't identify a fool by his face",
            "Do not worry, I also have a moron level. just made for people like you",
            "Go start with moron level, You Moron."]

    compliment = ["Well done..",
                    "Nice"]

    insult = ["..and I thought you can't identify a fool by his face",
                "Go read a book or something.Then come to play with me"]

    trapped = ["Get ready to loose",
                "Go start with moron level, You Moron.",
                "Do whatever you can do to win this one.",
                "You got trapped",
                "Do not get Demotivated, but you are going to loose.",
                "Do not worry, I also have a moron level. It will suit you better.",
                "Bad move",
                "just think before you make mistakes, like this one.",
                "You can't win this one.",
                "Now I own this game"]

    blocked=["Not so fast.",
             "You can't win that easily.",
             "You sneaky bastard."]

    if(var=="default"):
        string = default[random.randint(0,len(default)-1)]
    elif(var=="draw"):
            string = draw[random.randint(0,len(draw)-1)]
    elif(var=="lost"):
            string = lost[random.randint(0,len(lost)-1)]
    elif(var=="won"):
            string = won[random.randint(0,len(won)-1)]
    elif(var=="insult"):
            string = insult[random.randint(0,len(insult)-1)]
    elif(var=="compliment"):
            string = compliment[random.randint(0,len(compliment)-1)]
    elif(var=="trapped"):
            string = trapped[random.randint(0,len(trapped)-1)]
    elif(var=="blocked"):
            string = blocked[random.randint(0,len(blocked)-1)]

    ai_msg.config(text=string)


def guimsg_set_gamewinner(_str):
    game_stat.config(text =_str)



def showmessage():
    tkinter.messagebox.showinfo('About Tic Tac Toe','Made by Lalit Som\n version 1.0.0\nHow to play: Go check wikipedia\nFeedback: mail me->  lalitsom27@gmail.com')



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
    global g_player1
    g_winner =-1
    g_gameEnd=0
    g_chance=0
    for i in range(3):
        for j in range(3):
            g_game_grid[i][j]=-1

    bgcanvas.delete("all")
    board_img = bgcanvas.create_image(b_image_pos,b_image_pos,image=object_img_board)
    guimsg_set_gamewinner("Game is Running...")
    update_aimsg("default")
    if(g_player1==1):
        user_clicked(-5,0)


def user_clicked(_r,_c):
    global g_gameEnd
    _ai_is_player1 = _r
    if(_ai_is_player1==-5):
        _r=0
    if(g_gameEnd==0 and g_game_grid[_r][_c] ==-1 ):
        if(_ai_is_player1!=-5):
            g_game_grid[_r][_c] = g_player1
            put_piece(g_player1,_r,_c,0)

        _stat = check_game_status(return_list(g_game_grid))

        if(_stat==-1):
            _move = runai(g_player1)
            g_game_grid[_move[0]][_move[1]] = int(not(g_player1))
            _thread.start_new_thread( put_piece,(int(not(g_player1)), _move[0],_move[1],0.2))

        else:
            g_gameEnd = 1

        _stat = check_game_status(return_list(g_game_grid))
        if(_stat==5):
            update_aimsg("draw")
            guimsg_set_gamewinner("Draw")
        if(_stat==int(not(g_player1))):
            update_aimsg("won")
            guimsg_set_gamewinner("You Loose.. Bitch")
        if(_stat==g_player1):
            update_aimsg("lost")
            guimsg_set_gamewinner("YOU won..")


        if(_stat!=-1):
            g_gameEnd=1

def return_list(_mainlist):
    _tmplist = [[-1] *3 for n in range(3)]
    for i in range(3):
        for j in range(3):
            _tmplist[i][j] = _mainlist[i][j]

    return _tmplist


def put_piece(_player,_r,_c,_delay):
    time.sleep(_delay)
    if(_player == 0):
        _image = bgcanvas.create_image(img_pos_x +(_c*offset),img_pos_y + (_r*offset),image=object_img_red)
    else:
        _image = bgcanvas.create_image(img_pos_x +(_c*offset),img_pos_y + (_r*offset),image=object_img_blue)



def check_game_status(_tmp_g_game_grid):
    #print(g_game_grid)
    #print(_tmp_g_game_grid)

    for i in range(3):
        if( _tmp_g_game_grid[i][0] == _tmp_g_game_grid[i][1] and _tmp_g_game_grid[i][1] == _tmp_g_game_grid[i][2] and _tmp_g_game_grid[i][2] != -1  ):
            return _tmp_g_game_grid[i][2]

    for i in range(3):
        if( _tmp_g_game_grid[0][i] == _tmp_g_game_grid[1][i] and _tmp_g_game_grid[1][i] == _tmp_g_game_grid[2][i] and _tmp_g_game_grid[2][i] != -1  ):
            return _tmp_g_game_grid[2][i]

    if( _tmp_g_game_grid[0][0] == _tmp_g_game_grid[1][1] and _tmp_g_game_grid[1][1] == _tmp_g_game_grid[2][2] and _tmp_g_game_grid[2][2] != -1  ):
        return _tmp_g_game_grid[2][2]

    if( _tmp_g_game_grid[0][2] == _tmp_g_game_grid[1][1] and _tmp_g_game_grid[1][1] == _tmp_g_game_grid[2][0] and _tmp_g_game_grid[2][0] != -1  ):
        return _tmp_g_game_grid[2][0]
#.......................draw...............

    for i in range(3):
        for j in range(3):
            if(_tmp_g_game_grid[i][j]==-1):
                return -1

    return 5




def runai(_user):
    global g_game_grid
    _ai = int(not _user)


#.........special case...........only for legendary..........
    if(g_menu_level>=2):
        _legendmoves = legend_ai(return_list(g_game_grid), _user,1)
        if(_legendmoves[0]!=-1):
            print("legend is at work",_legendmoves)
            return _legendmoves[0],_legendmoves[1]


#..........check if I can Win in this move
    if(g_menu_level>=0):
        for i in range(3):
            for j in range(3):
                if(g_game_grid[i][(j+1)%3]==_ai and g_game_grid[i][(j+2)%3]==_ai and g_game_grid[i][(j+3)%3]!=_user ):
                    return i,(j+3)%3

        for i in range(3):
            for j in range(3):
                if(g_game_grid[(j+1)%3][i]==_ai and g_game_grid[(j+2)%3][i]==_ai and g_game_grid[(j+3)%3][i]!=_user ):
                    return (j+3)%3,i


        for i in range(3):
            if(g_game_grid[(i+1)%3][(i+1)%3]==_ai and g_game_grid[(i+2)%3][(i+2)%3]==_ai and g_game_grid[(i+3)%3][(i+3)%3]!=_user ):
                    return (i+3)%3,(i+3)%3

                    #.........diagonal 1
        for i in range(3):
            if(g_game_grid[(i+1)%3][(i+1)%3]==_ai and g_game_grid[(i+2)%3][(i+2)%3]==_ai and g_game_grid[(i+3)%3][(i+3)%3]!=_user ):
                    return (i+3)%3,(i+3)%3


                    #.........diagonal 2
        for i in range(3):
            if(g_game_grid[0][2]==_ai and g_game_grid[2][0]==_ai and g_game_grid[1][1]!=_user ):
                    return 1,1
            if(g_game_grid[1][1]==_ai and g_game_grid[2][0]==_ai and g_game_grid[0][2]!=_user ):
                    return 0,2
            if(g_game_grid[0][2]==_ai and g_game_grid[1][1]==_ai and g_game_grid[2][0]!=_user ):
                    return 2,0


    update_aimsg("blocked")

# .......check if user can win in this move..............
    if(g_menu_level>=1):
        for i in range(3):
            for j in range(3):
                if(g_game_grid[i][(j+1)%3]==_user and g_game_grid[i][(j+2)%3]==_user and g_game_grid[i][(j+3)%3]!=_ai ):
                    return i,(j+3)%3

        for i in range(3):
            for j in range(3):
                if(g_game_grid[(j+1)%3][i]==_user and g_game_grid[(j+2)%3][i]==_user and g_game_grid[(j+3)%3][i]!=_ai ):
                    return (j+3)%3,i

    #.........diagonal 1
        for i in range(3):
            if(g_game_grid[(i+1)%3][(i+1)%3]==_user and g_game_grid[(i+2)%3][(i+2)%3]==_user and g_game_grid[(i+3)%3][(i+3)%3]!=_ai ):
                    return (i+3)%3,(i+3)%3


    #.........diagonal 2
        for i in range(3):
            if(g_game_grid[0][2]==_user and g_game_grid[2][0]==_user and g_game_grid[1][1]!=_ai ):
                    return 1,1
            if(g_game_grid[1][1]==_user and g_game_grid[2][0]==_user and g_game_grid[0][2]!=_ai ):
                    return 0,2
            if(g_game_grid[0][2]==_user and g_game_grid[1][1]==_user and g_game_grid[2][0]!=_ai ):
                    return 2,0



    update_aimsg("default")

#...........choose centre if avalaible
    if(g_menu_level>=1):
        if g_game_grid[1][1]==-1:
            return 1,1



#.....default case..ai choose  random location ............................


    if(g_menu_level>=0):
        i = random.randint(0,3)
        j = random.randint(0,3)
        for i1 in range(3):
            for j1 in range(3):
                if g_game_grid[(i+i1)%3][(j+j1)%3]==-1:
                    return (i+i1)%3,(j+j1)%3


#.......MIN mAX Algo.................................
def legend_ai(_local_grid, _opponent, _chance):
    if(_local_grid[1][1]==-1):
        return 1,1
    _min = 100000; _i_max =1; _j_max=1;
    for _i1 in range(3):
        for _j1 in range(3):
            if(_local_grid[_i1][_j1]==-1):
                _tmp = min_max_search( return_list(_local_grid), _i1,_j1,_opponent,_chance,0)
                _total = _tmp[0] + _tmp[1] + _tmp[2]
                if(_total!=0):
                    print(_tmp,_i1,_j1,_total,(_tmp[2]*100)/_total)
                    if( (_tmp[2]*100)/_total< _min ):
                        _min = (_tmp[2]*100)/_total
                        _i_max= _i1
                        _j_max = _j1

    return _i_max,_j_max

def min_max_search(_local_grid, i1_,j1_, _opponent, _chance,_lvl):
    #return won,draw,lost
    #if(_lvl>1):
        #return 0
    _ai = int(not _opponent)

#if ai wins return 1
    if(_chance==1):
        _local_grid[i1_][j1_] = _ai
        for i in range(3):
            for j in range(3):
                if (_local_grid[i][j]==-1):
                    tmp = return_list(_local_grid)
                    tmp[i][j] = _opponent
                    _stat = check_game_status(return_list(tmp))
                    if(_stat == _opponent):
                        return 0,0,1
    else:
        #if opponent wins return -1
        _local_grid[i1_][j1_] = _opponent
        for i in range(3):
            for j in range(3):
                if (_local_grid[i][j]==-1):
                    tmp = return_list(_local_grid)
                    tmp[i][j] = _ai
                    _stat = check_game_status(return_list(tmp))
                    if(_stat == _ai):
                        return 1,0,0

    _stat = check_game_status(return_list(_local_grid))
    if(_stat == 5):                 #if grid is full and draw return 0
        return 0,1,0

    _sum =[0,0,0]
    #print("what agin")
    for i in range(3):
        for j in range(3):
            if(_local_grid[i][j]==-1):
                _tmp= min_max_search(return_list(_local_grid), i, j,_opponent,int(not _chance),_lvl+1)
                _sum[0]+=_tmp[0]
                _sum[1]+=_tmp[1]
                _sum[2]+=_tmp[2]
                #print("new ",_tmp,_local_grid,i,j,_lvl)

    return _sum


#...........main window...........

mainWnd = Tk()
mainWnd.wm_title("Tic Tac Toe")
#mainWnd.iconbitmap("icon.ico")



#.............toolbar.............

menu_bar = Menu(mainWnd, tearoff=False)
mainWnd.config(menu = menu_bar)


submenu_levels = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Levels",menu=submenu_levels)


submenu_levels.add_command(label="Moron", command = lambda: changeLevel(0,submenu_levels));
submenu_levels.add_command(label="Pro",command = lambda: changeLevel(1,submenu_levels));
submenu_levels.add_command(label="Legend", command = lambda: changeLevel(2,submenu_levels));



submenu_player = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Play as..",menu=submenu_player)
submenu_player.add_command(label="Player 1 RED*", command = lambda: changePlayer(0,submenu_player));
submenu_player.add_command(label="Player 2 BLUE", command = lambda: changePlayer(1,submenu_player));



menu_bar.add_command(label="About", command=showmessage)



#.............options frame left side part of main wnd.............

option_frame = Frame(mainWnd, bg="#21252b", height="450", width="170",highlightthickness=1,highlightbackground ="#1a181f", relief=RAISED,pady =30 )
option_frame.pack(side=LEFT, fill=None, expand=False)
option_frame.pack_propagate(0)

game_name = Label(option_frame, text="T I C  T A C  T O E\n",bg ="#21252b",fg="#e97263", font=("Arial","13","bold"))
game_name.pack();

restart_btn = Button(option_frame, text="RESET", font=("Helvetica","17","bold"),bg ="#4285fa", fg ="white",bd=0)
restart_btn.pack()
restart_btn.config(height=1, width=7)
restart_btn.bind('<Button-1>', reset_game)

level_info = Label(option_frame, text="Level : Moron",bg ="#21252b",fg="#9da5b4", font=("Arial","11"),pady=15)
level_info.pack();

player_info = Label(option_frame, text="You are Player 1 RED\n\n",bg ="#21252b",fg="#9da5b4", font=("Arial","11"))
player_info.pack();


ai_msg = Label(option_frame, text="It's your move. I'm waiting.......",bg ="#21252b",fg="#4285fa", font=("Arial","11"),wraplength="150")
ai_msg.pack();


game_stat = Label(option_frame, text="You Won\n",bg ="#21252b",fg="green", font=("Arial","11"))
game_stat.pack(side=BOTTOM);



#.............game frame right side part of main window or main gui.............

game_frame = Frame(mainWnd, bg="#282c34", height="450", width="450", relief=SUNKEN)
game_frame.pack_propagate(0)
game_frame.pack(side=LEFT)


#.................main canvas where images get drawn..............
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

#...................game variables....................

g_player1 =0 #red one
g_winner =-1
g_gameEnd=0
g_chance=0
g_game_grid = [[-1] *3 for n in range(3)] #initial state
g_menu_level = 0
g_menu_playas = 0

changeLevel(0,submenu_levels)

#.....................................
mainWnd.resizable(width=False, height =False)
mainWnd.mainloop()
