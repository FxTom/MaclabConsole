#!/usr/bin/python3
# -*-coding:UTF-8 -*
import Begin

if __name__ == "__main__":
    perso = "X"
    pos_perso = [1,1]
    objet  = {"gain":0}
    level_1 = Begin.charge_lab("level")
    Begin.game(level_1,objet,perso,pos_perso)
    if objet["gain"] == 3:
        print("You win the level, you're a expert!!!")
