# -*-coding:utf-8 -*
import os
import sys

def charge_lab(nom):
    fichier = open(nom + ".txt", "r")
    donnee = fichier.readlines()
    for i in range(len(donnee)):
        donnee[i] = donnee[i].strip()
    return list(donnee)

def show_lab(lab,perso,pos_perso):
    compteur_ligne = 0
    for i in lab:
        if compteur_ligne == pos_perso[1]:
            print(i[0:pos_perso[0]]+ perso + i[pos_perso[0]+1:])
        else:
            print(i)
        compteur_ligne += 1

def efface_ecran():
    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        os.system("clear")

def decouverte_tresor(tresor,objet):
    if tresor == "#":
        objet["gain"] = objet["gain"] + 1

def verification_deplacement(lab,pos_col,pos_ligne,objet):
    n_cols = len(lab[0])
    n_lignes = len(lab)
    if pos_ligne < 0 or pos_col < 0 or pos_ligne > (n_lignes -1) or pos_col > (n_cols -1):
        return None
    elif lab[pos_ligne][pos_col] == "O" :
        return [-1,-1]
    elif lab[pos_ligne][pos_col] == "#" :
        decouverte_tresor(lab[pos_ligne][pos_col], objet)
        lab[pos_ligne] = lab[pos_ligne][:pos_col] + " " +lab[pos_ligne][pos_col +1 :]
        return [pos_col,pos_ligne]
    elif lab[pos_ligne][pos_col] != " " :
        return None
    else:
        return [pos_col,pos_ligne]


def choice_gamers(lab,pos_perso,objet):
    dep = None
    choix = input("pour jouer utiliser z/s/q/d ou utilisez 'Q' pour quitter  ")
    if choix == "z":
        dep = verification_deplacement(lab,pos_perso[0],pos_perso[1]-1,objet)
    elif choix == "s" :
        dep = verification_deplacement(lab,pos_perso[0],pos_perso[1] +1,objet)
    elif choix =="q" :
        dep = verification_deplacement(lab,pos_perso[0]-1,pos_perso[1],objet)
    elif choix =="d" :
        dep = verification_deplacement(lab,pos_perso[0]+1,pos_perso[1],objet)
    elif choix =="Q" :
        os._exit(1)
    if dep == None:
        print("Deplacement impossible")
    else :
        pos_perso[0] = dep [0]
        pos_perso[1] = dep [1]


def game(lab,objet,perso,pos_perso):
    while True:
        efface_ecran()
        show_lab(lab,perso,pos_perso)
        choice_gamers(lab,pos_perso,objet)
        if pos_perso == [-1,-1] and objet["gain"] < 3:
            print("Et la seringue?? vous êtes mort")
            break
        
