#!/usr/bin/python3
# -*-coding:UTF-8 -*
import Begin
from random import choice

if __name__ == "__main__":
#initialization characters
    perso = "X"
    pos_perso = [1,1]
    gift  = {"gain":0}
    level_rand = ["level1","level2","level3","level4","level5","level6","level7"]
    levels = random.choice(level_rand)
#Core program
    level = Begin.load_lab(levels)
    Begin.game(level,gift,perso,pos_perso)
