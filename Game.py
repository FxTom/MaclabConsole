#!/usr/bin/python3
# -*-coding:UTF-8 -*
import Begin

if __name__ == "__main__":
#initialization characters
    perso = "X"
    pos_perso = [1,1]
    gift  = {"gain":0}

#Core program
    level_1 = Begin.load_lab("level1")
    Begin.game(level_1,gift,perso,pos_perso)
