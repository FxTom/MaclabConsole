# -*-coding:utf-8 -*
import os


def show_lab(lab,perso,pos_perso):
    """show the labyrinthe"""
    compteur_ligne = 0
    for i in lab:
        if compteur_ligne == pos_perso[1]:
            print(i[0:pos_perso[0]]+ perso + i[pos_perso[0]+1:])
        else:
            print(i)
        compteur_ligne = compteur_ligne + 1

def verification_deplacement(lab,pos_col,pos_ligne):
    n_cols = len(lab[0])
    n_lignes = len(lab)
    if pos_ligne < 0 or pos_col < 0 or pos_ligne > (n_lignes -1) or pos_col > (n_cols -1):
        return None
    elif lab[pos_ligne][pos_col] == "O" :
        return [-1,-1]
    elif lab[pos_ligne][pos_col] != " " :
        return None
    else:
        return [pos_col,pos_ligne]

def choice_gamers(lab,pos_perso):
    choix = input("Haut/Bas/Droite/Gauche")
    if choix == "Haut" or choix == "H":
        dep = verification_deplacement(lab,pos_perso[0],pos_perso[1]-1)
    elif choix == "B" or choix =="Bas" :
        dep = verification_deplacement(lab,pos_perso[0],pos_perso[1] +1)
    elif choix =="G" or choix == "Gauche" :
        dep = verification_deplacement(lab,pos_perso[0]-1,pos_perso[1])
    elif choix =="D" or choix == "Droite" :
        dep = verification_deplacement(lab,pos_perso[0]+1,pos_perso[1])
    elif choix =="Q" or choix =="Quitter" :
        os._exit(1)
    if dep == None:
        print("Deplacement impossible")
    else :
        pos_perso[0] = dep [0]
        pos_perso[1] = dep [1]

def charge_lab(nom):
    fic = open(nom + ".txt", "r")
    data = fic.readlines()
    for i in range(len(data)):
        data[i] = data[i].strip()
    return tuple(data)

def game(lab,perso,pos_perso):
    while True:
        show_lab(lab,perso,pos_perso)
        choice_gamers(lab,pos_perso)
        if pos_perso == [-1,-1]:
            print("You win the level")
            break

#############
#PROGRAMME PRINCIPAL
perso = "X"
pos_perso = [1,1]
level_1 = charge_lab("level")
game(level_1,perso,pos_perso)
