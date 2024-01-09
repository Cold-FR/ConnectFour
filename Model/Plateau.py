from Model.Constantes import *
from Model.Pion import *


#
# Le plateau représente la grille où sont placés les pions.
# Il constitue le coeur du jeu car c'est dans ce fichier
# où vont être programmées toutes les règles du jeu.
#
# Un plateau sera simplement une liste de liste.
# Ce sera en fait une liste de lignes.
# Les cases du plateau ne pourront contenir que None ou un pion
#
# Pour améliorer la "rapidité" du programme, il n'y aura aucun test sur les paramètres.
# (mais c'est peut-être déjà trop tard car les tests sont fait en amont, ce qui ralentit le programme...)
#

def type_plateau(plateau: list) -> bool:
    """
    Permet de vérifier que le paramètre correspond à un plateau.
    Renvoie True si c'est le cas, False sinon.

    :param plateau: Objet qu'on veut tester
    :return: True s'il correspond à un plateau, False sinon
    """
    if type(plateau) != list:
        return False
    if len(plateau) != const.NB_LINES:
        return False
    wrong = "Erreur !"
    if next((wrong for line in plateau if type(line) != list or len(line) != const.NB_COLUMNS), True) == wrong:
        return False
    if next((wrong for line in plateau for c in line if not(c is None) and not type_pion(c)), True) == wrong:
        return False
    return True


def construirePlateau() -> list:
    """
    Fonction permettant de construire un plateau vide
    :return: Tableau 2D représentant un plateau
    """
    plateau = []
    for i in range(const.NB_LINES):
        line = []
        for j in range(const.NB_COLUMNS):
            line.append(None)
        plateau.append(line)
    return plateau


def placerPionPlateau(plateau: list, pion: dict, numCol: int) -> int:
    """
    Fonction plaçant un pion dans le plateau à la colonne correspondante
    :param plateau: Tableau 2D représentant un plateau
    :param pion: Dictionnaire représentant un pion
    :param numCol: Entier représentant le numéro de la colonne
    :return: Le numéro de la ligne où se retrouve le pion, ou -1 si la colonne est pleine
    :raise TypeError: Si le premier paramètre n’est pas un plateau
    :raise TypeError: Si le second paramètre n’est pas un pion
    :raise TypeError: Si le troisième paramètre n’est pas un entier
    :raise ValueError: Si le troisième paramètre n'est pas un numéro de colonne valide
    """
    if not type_plateau(plateau):
        raise TypeError('placerPionPlateau : Le premier paramètre ne correspond pas à un plateau')
    if not type_pion(pion):
        raise TypeError('placerPionPlateau : Le second paramètre n\'est pas un pion')
    if type(numCol) is not int:
        raise TypeError('placerPionPlateau : Le troisième paramètre n\'est pas un entier')
    if numCol < 0 or numCol > const.NB_COLUMNS - 1:
        raise ValueError(f'placerPionPlateau : La valeur de la colonne ({numCol}) n\'est pas correcte')

    i = -1
    while i < const.NB_LINES - 1 and plateau[i+1][numCol] is None:
        i += 1
    if i != -1:
        plateau[i][numCol] = pion

    return i
