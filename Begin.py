# -*-coding:utf-8 -*
import os
import sys
import curses


def init_curses(lignes,cols,pos):
    curses.initscr()                 #initialisation du mode graphique
    curses.noecho()                  #Desactivation de l'affichage
    curses.cbreak()                  #Interception des touches tapez au clavier
    curses.curs_set(0)               #Desactivation de l'affichage

    window = curses.newwin(lignes,cols,pos[0],pos[1])   #Creation d'une fenetre (49 caractere de haut,79 de large positionner en 0,0 du terminal)
    window.border(0)                                    #activation du trace de la bordure de la fenetre
    window.keypad(1)                                    #activation du nombre de touches
    return window                                       # attente de l'appui d'une touche

def close_curses():
    curses.echo()
    curses.nocbreak()
    curses.curs_set(1)
    curses.endwin()

def init_colors():
    curses.start_color()
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_BLACK,curses.COLOR_BLUE)
    return ["RED","GREEN","BLUE"]

def color(code,l_color):
    return curses.color_pair(l_color.index(code)+1)


def load_lab(name):
    """Load the labyrinthe
    name: name of the file whithout the '.txt'"""
    fichier = open(name + ".txt", "r")
    item = fichier.readlines()
    for i in range(len(item)):
        item[i] = item[i].strip()
    return item

def show_lab(lab,perso,pos_perso,window,coul):
    """show the labyrinthe
    lab: is the variable with the lab
    perso: symbole show characters
    pos_perso: list show the position of chracters(line,column)
    win: window graphic mode
    coul: list of color for the graphic mode"""
    count_line = 0
    for i in lab:
        if count_line == pos_perso[1]:
            window.addstr(count_line+1,10,i[0:pos_perso[0]]+ perso + i[pos_perso[0]+1:])
            window.addstr(count_line +1,10 + pos_perso[0],perso,color("RED",coul))
        else:
            window.addstr(count_line +1 ,10, i)
        count_line += 1

def del_screen():
    """delete the screen of the terminal"""
    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        os.system("clear")

def discovery_tresor(tresor,gift):
    """
    increments the variable if the player passes on a gift
    if it's possible to past the guardian
    gift: data of the game
    """
    if tresor == "#":
        gift["gain"] = gift["gain"] + 1

def verify_deplacement(lab,pos_col,pos_line,gift):
    """
    show if the deplacement of th characters is agree or not
    lab: labyrinthe
    pos_col: position of the characters in column
    pos_line: position of the characters in pos_line
    """
    n_cols = len(lab[0])
    n_lines = len(lab)
    if pos_line < 0 or pos_col < 0 or pos_line > (n_lines -1) or pos_col > (n_cols -1):
        return None
    elif lab[pos_line][pos_col] == "O" :
        return [-1,-1]
    elif lab[pos_line][pos_col] == "#" :
        discovery_tresor(lab[pos_line][pos_col], gift)
        lab[pos_line] = lab[pos_line][:pos_col] + " " +lab[pos_line][pos_col +1 :]
        return [pos_col,pos_line]
    elif lab[pos_line][pos_col] != " " :
        return None
    else:
        return [pos_col,pos_line]


def choice_gamers(lab,pos_perso,gift,window):
    """
    asks the player to choose his move and checks if possible.
    lab:labyrinthe
    pos_perso: list show the position of characters(line,column)
    gift: data of the gamer
    """
    dep = None
    choix = window.getch()
    if choix == curses.KEY_UP:
        dep = verify_deplacement(lab,pos_perso[0],pos_perso[1]-1,gift)
    elif choix == curses.KEY_DOWN:
        dep = verify_deplacement(lab,pos_perso[0],pos_perso[1] +1,gift)
    elif choix == curses.KEY_LEFT :
        dep = verify_deplacement(lab,pos_perso[0]-1,pos_perso[1],gift)
    elif choix == curses.KEY_RIGHT :
        dep = verify_deplacement(lab,pos_perso[0]+1,pos_perso[1],gift)
    elif choix == 27 :
        close_curses()
        os._exit(1)
    if dep != None:
        pos_perso[0] = dep [0]
        pos_perso[1] = dep [1]

def game(lab,gift,perso,pos_perso,window,coul):
    """
    The main loop of the game displays the labyrinth in
    its different states after the player moves.
    """
    while True:
        show_lab(lab,perso,pos_perso,window,coul)
        choice_gamers(lab,pos_perso,objet,window)
        if pos_perso == [-1,-1] and gift["gain"] < 3:
            window.addstr(22,1,"Et la seringue!!!!",color("RED",coul))
            window.addstr(23,1,"appuyez sur une touche pour continuer",color("RED",coul))
            window.getch()
            window.addstr(1,20," "*50)
            window.addstr(1,21," "*50)
        elif pos_perso == [-1,-1] and gift["gain"] == 3:
            window.addstr(22,1,"BRAVO FELCITATIONS",color("GREEN",coul))
            window.addstr(23,1,"appuyez sur une touche pour continuer",color("RED",coul))
            window.getch()
            window.addstr(1,20," "*50)
            window.addstr(1,21, " "*50)
