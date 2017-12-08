#!/usr/bin/python3
# -*-coding:UTF-8 -*

import Begin
import random
from random import choice

if __name__ == "__main__":
#initialization characters
    perso = "X"
    pos_perso = [1,1]
    gift  = {"gain":0}
    level_rand = ["level1","level2","level3","level4","level5","level6","level7"]
    levels = random.choice(level_rand)
    window = Begin.init_curses(25,41,(0,0))
    coul = Begin.init_colors()
#Core program
    level = Begin.load_lab(levels)
    Begin.game(level,gift,perso,pos_perso,window,coul)
    window.getch()
    Begin.close_curses()
