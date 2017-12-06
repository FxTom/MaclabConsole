# -*-coding:utf-8 -*
import os
import sys


def load_lab(name):
    """Load the labyrinthe
    name: name of the file whithout the '.txt'"""
    fichier = open(name + ".txt", "r")
    item = fichier.readlines()
    for i in range(len(item)):
        item[i] = item[i].strip()
    return item

def show_lab(lab,perso,pos_perso):
    """show the labyrinthe
    lab: is the variable with the lab
    perso: symbole show characters
    pos_perso: list show the position of chracters(line,column)"""
    count_line = 0
    for i in lab:
        if count_line == pos_perso[1]:
            print(i[0:pos_perso[0]]+ perso + i[pos_perso[0]+1:])
        else:
            print(i)
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


def choice_gamers(lab,pos_perso,gift):
    """
    asks the player to choose his move and checks if possible.
    lab:labyrinthe
    pos_perso: list show the position of characters(line,column)
    gift: data of the gamer
    """
    dep = None
    choix = input("pour jouer utiliser z/s/q/d ou utilisez 'E' pour quitter  ")
    if choix == "z":
        dep = verify_deplacement(lab,pos_perso[0],pos_perso[1]-1,gift)
    elif choix == "s" :
        dep = verify_deplacement(lab,pos_perso[0],pos_perso[1] +1,gift)
    elif choix =="q" :
        dep = verify_deplacement(lab,pos_perso[0]-1,pos_perso[1],gift)
    elif choix =="d" :
        dep = verify_deplacement(lab,pos_perso[0]+1,pos_perso[1],gift)
    elif choix =="E" :
        os._exit(1)
    if dep == None:
        print("Deplacement impossible")
    else :
        pos_perso[0] = dep [0]
        pos_perso[1] = dep [1]

def game(lab,objet,perso,pos_perso):
    """
    The main loop of the game displays the labyrinth in
    its different states after the player moves.
    """
    while True:
        del_screen()
        show_lab(lab,perso,pos_perso)
        choice_gamers(lab,pos_perso,objet)
        if pos_perso == [-1,-1] and objet["gain"] < 3:
            print("Et la seringue!!!!")
            break
        elif pos_perso == [-1,-1] and objet["gain"] == 3:
            print("Bravo!!!! Boss anéantie!")
            break
