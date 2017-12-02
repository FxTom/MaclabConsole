# -*-coding:utf-8 -*
import os
import sys
import random

def show_lab(lab,perso,pos_perso):
    """show the labyrinthe"""
    compteur_ligne = 0
    for i in lab:
        if compteur_ligne == pos_perso[1]:
            print(i[0:pos_perso[0]]+ perso + i[pos_perso[0]+1:])
        else:
            print(i)
        compteur_ligne += 1

def verification_deplacement(lab,pos_col,pos_ligne):
    n_cols = len(lab[0])
    n_lignes = len(lab)
    data = 0
    if pos_ligne < 0 or pos_col < 0 or pos_ligne > (n_lignes -1) or pos_col > (n_cols -1):
        return None
    elif lab[pos_ligne][pos_col] == "O" :
        return [-1,-1]
    elif lab[pos_ligne][pos_col] == "1" or lab[pos_ligne][pos_col] == "2" or lab[pos_ligne][pos_col] == "3":
        lab[pos_ligne]= lab[pos_ligne][:pos_col] + " " +lab[pos_ligne][pos_col +1 :]
        return [pos_col,pos_ligne], data == "3"
    elif lab[pos_ligne][pos_col] != " " :
        return None
    else:
        return [pos_col,pos_ligne]

def choice_gamers(lab,pos_perso):
    dep = None
    choix = input("pour jouer utiliser z/s/q/d ou utilisez 'Q' pour quitter  ")
    if choix == "z":
        dep = verification_deplacement(lab,pos_perso[0],pos_perso[1]-1)
    elif choix == "s" :
        dep = verification_deplacement(lab,pos_perso[0],pos_perso[1] +1)
    elif choix =="q" :
        dep = verification_deplacement(lab,pos_perso[0]-1,pos_perso[1])
    elif choix =="d" :
        dep = verification_deplacement(lab,pos_perso[0]+1,pos_perso[1])
    elif choix =="Q" :
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
    return list(data)

def efface_ecran():
    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        os.system("clear")

def game(lab,perso,pos_perso):
    while True:
        efface_ecran()
        show_lab(lab,perso,pos_perso)
        choice_gamers(lab,pos_perso)
        if pos_perso == [-1,-1] and data == "3":
            print("#####################################")
            print("You win the level, you're a expert!!!")
            break
