# -*-coding:utf-8 -*

level1 = ["""\
################
#              #
#              #
#              #
#              #
#              #
#              #
#              #
#              #
#              #
#              #
#              #
#              #
#              #
################"""]

def around_lab(size):                       #take the contour of the labyrinthe
    print("#{}#".format("#"*(size-2)))
    for i in range(size-2):
        print("#{}#".format(" "*(size-2)))
    print("#{}#".format("#"*(size-2)))


def show_lab(lab):                           #show the labyrinthe
    for i in lab:
        print(i)
