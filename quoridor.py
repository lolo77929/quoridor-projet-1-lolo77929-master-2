# -*- coding: utf-8 -*-
"""Module d'interface utilisateur de Quoridor

Ce module permet d'interagir avec le joueur
en offrant un interface en ligne de commande.

Functions:
    * analyser_commande - Retourne la liste des parties reçues du serveur
    * afficher_damier_ascii - Affiche la représentation graphique
                              du damier en ligne de commande.
    * TODO: Ajoutez vos autres fonctions le cas échéant,
            supprimer le TODO une fois complété.
"""
import argparse


def analyser_commande():
    """Génère un analyseur de ligne de commande

    En utilisant le module argparse, génère un analyseur de ligne de commande.
    L'analyseur offre (1) argument positionnel:

        IDUL: IDUL du joueur.

    Ainsi que les (2) arguments optionnel:

        help: show this help message and exit
        parties: Lister les identifiants de vos 20 dernières parties.

    Returns:
        Namespace: Retourne un objet de type Namespace possédant
            les clef «idul» et «lister».
    """
    parser = argparse.ArgumentParser()

    # TODO: Insérer ici les bons appels à la méthode add_argument,
    #       retirer le TODO une fois complété.

    return parser.parse_args()


def afficher_damier_ascii(grille):
    """Afficher le damier

    Ne faites preuve d'aucune originalité dans votre «art ascii»,
    car votre fonction sera testée par un programme et celui-ci est
    de nature intolérante (votre affichage doit être identique à
    celui illustré). Notez aussi que votre fonction sera testée
    avec plusieurs états de jeu différents.

    Args:
        grille (dict): Dictionnaire représentant l'état du jeu.

    Examples:
        >>> grille = {
                "joueurs": [
                    {"nom": "wawil13", "murs": 7, "pos": [5, 5]},
                    {"nom": "automate", "murs": 3, "pos": [8, 6]}
                ],
                "murs": {
                    "horizontaux": [[4, 4], [2, 6], [3, 8], [5, 8], [7, 8]],
                    "verticaux": [[6, 2], [4, 4], [2, 6], [7, 5], [7, 7]]
                }
            }
        >>> afficher_damier_ascii(grille)

            Légende:
               1=wawil13,  murs=|||||||
               2=automate, murs=|||
               -----------------------------------
            9 | .   .   .   .   .   .   .   .   . |
              |                                   |
            8 | .   .   .   .   .   . | .   .   . |
              |        ------- -------|-------    |
            7 | . | .   .   .   .   . | .   .   . |
              |   |                               |
            6 | . | .   .   .   .   . | .   2   . |
              |    -------            |           |
            5 | .   .   . | .   1   . | .   .   . |
              |           |                       |
            4 | .   .   . | .   .   .   .   .   . |
              |            -------                |
            3 | .   .   .   .   . | .   .   .   . |
              |                   |               |
            2 | .   .   .   .   . | .   .   .   . |
              |                                   |
            1 | .   .   .   .   .   .   .   .   . |
            --|-----------------------------------
              | 1   2   3   4   5   6   7   8   9
    """
    # TODO: Complétez cette fonction, retirer le TODO une fois complété.
    pass


# TODO: Vous pouvez créer des fonctions additionnels si vous en sentez le besoin,
#       Il ne devrait pas y avoir autre chose que des définitions de fonctions.
#       Retirer le TODO une fois complété.
# TODO: Supprimer le code et les commentaires superflux.
# TODO: Supprimer les TODO une fois complété.
