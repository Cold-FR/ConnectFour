# Model/Pion.py

from Model.Constantes import *

#
# Ce fichier implémente les données/fonctions concernant le pion
# dans le jeu du Puissance 4
#
# Un pion est caractérisé par :
# - sa couleur (const.ROUGE ou const.JAUNE)
# - un identifiant de type int (pour l'interface graphique)
#
# L'identifiant sera initialisé par défaut à None
#

def type_pion(pion: dict) -> bool:
    """
    Détermine si le paramètre peut être ou non un Pion

    :param pion: Paramètre dont on veut savoir si c'est un Pion ou non
    :return: True si le paramètre correspond à un Pion, False sinon.
    """
    return type(pion) == dict and len(pion) == 2 and const.COULEUR in pion.keys() \
        and const.ID in pion.keys() \
        and pion[const.COULEUR] in const.COULEURS \
        and (pion[const.ID] is None or type(pion[const.ID]) == int)


def construirePion(color: int) -> dict:
    """
    Fonction permettant de construire un pion
    :param color: Couleur du pion à construire
    :return: Dictionnaire représentant un pion
    :raise TypeError: Si le paramètre n’est pas un entier
    :raise ValueError: Si l’entier ne représente pas une couleur
    """
    if type(color) is not int:
        raise TypeError('construirePion : Le paramètre n\'est pas de type entier')
    if color is not in const.COULEURS:
        raise ValueError(f'construirePion : la couleur ({color}) n\'est pas correcte')

    return {const.COULEUR: color, const.ID: None}


def getCouleurPion(pion: dict) -> int:
    """
    Fonction récupérant la couleur d'un pion
    :param pion: Dictionnaire représentant un pion
    :return: Couleur du pion
    :raise TypeError: Si le paramètre n'est pas un pion
    """
    if not type_pion(pion):
        raise TypeError('getCouleurPion : Le paramètre n\'est pas un pion')
    return pion[const.COULEUR]