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
python
        help: show this help message and exit
        parties: Lister les identifiants de vos 20 dernières parties.

    Returns:
        Namespace: Retourne un objet de type Namespace possédant
            les clef «idul» et «lister».
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('-p', '--parties', action="store_true", help='Lister les identifiants de vos 20 dernières parties')
    parser.add_argument('IDUL', nargs='+', help='IDUL du joueur')

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
    légende = (f'Légende:\n    1='+'{0:<10}'.format(grille['joueurs'][0]['nom']+',')+ 
               'murs={}\n    2='.format('|'*grille['joueurs'][0]['murs'])+
               '{0:<10}'.format(grille['joueurs'][1]['nom']+',')+
               'murs={}\n'.format('|'*grille['joueurs'][1]['murs']))
    
    vierge = (' ' + ('.' + ' '*3)*8 + '. ' + ' '*35)*8 + (' ' + ('.' + ' '*3)*8 + '. ')
    liste = list(vierge)
    
    liste.insert((70 * (grille['joueurs'][0]['pos'][1]-1) + # Placer le joueur #1
                  (4*grille['joueurs'][0]['pos'][0]) - 3), '1')
    del liste[liste.index('1')+1]
    
    liste.insert((70 * (grille['joueurs'][1]['pos'][1]-1) + # Placer le joueur #2
                  (4*grille['joueurs'][1]['pos'][0]) - 3), '2')
    del liste[liste.index('2')+1]
    
    for i in grille['murs']['horizontaux']: # Placer les murs horizontaux
        L, C = i
        for x in range(7):
            liste.insert((((2*(C-1))-1)*35)+(L*4)-4+x, '-')
            del liste[(((2*(C-1))-1)*35)+(L*4)-3+x]
    
    for i in grille['murs']['verticaux']:# Placer les murs verticaux
        L, C = i
        for x in range(3):
            liste.insert(((2*(C-1)+x)*35 + (L*4)-5), '|')
            del liste[(2*(C-1)+x)*35 + (L*4)-4]
    
    lignea = '   {}\n'.format('-'*35) # La grille
    ligne9a = '9 |{}|\n'.format(''.join(liste[560:]))
    ligne8b = '  |{}|\n'.format(''.join(liste[525:560]))
    ligne8a = '8 |{}|\n'.format(''.join(liste[490:525]))
    ligne7b = '  |{}|\n'.format(''.join(liste[455:490]))
    ligne7a = '7 |{}|\n'.format(''.join(liste[420:455]))
    ligne6b = '  |{}|\n'.format(''.join(liste[385:420]))
    ligne6a = '6 |{}|\n'.format(''.join(liste[350:385]))
    ligne5b = '  |{}|\n'.format(''.join(liste[315:350]))
    ligne5a = '5 |{}|\n'.format(''.join(liste[280:315]))
    ligne4b = '  |{}|\n'.format(''.join(liste[245:280]))
    ligne4a = '4 |{}|\n'.format(''.join(liste[210:245]))
    ligne3b = '  |{}|\n'.format(''.join(liste[175:210]))
    ligne3a = '3 |{}|\n'.format(''.join(liste[140:175]))
    ligne2b = '  |{}|\n'.format(''.join(liste[105:140]))
    ligne2a = '2 |{}|\n'.format(''.join(liste[70:105]))
    ligne1b = '  |{}|\n'.format(''.join(liste[35:70]))
    ligne1a = '1 |{}|\n'.format(''.join(liste[:35]))
    ligneb = '--|{}\n'.format('-'*35)
    lignec = '  | 1   2   3   4   5   6   7   8   9'
    
    print(légende, lignea, ligne9a, ligne8b, ligne8a, ligne7b, ligne7a, 
      ligne6b, ligne6a, ligne5b, ligne5a, ligne4b, ligne4a, ligne3b, 
      ligne3a, ligne2b, ligne2a, ligne1b, ligne1a, ligneb, lignec)
      
    # TODO: Complétez cette fonction, retirer le TODO une fois complété.
    pass


# TODO: Vous pouvez créer des fonctions additionnels si vous en sentez le besoin,
#       Il ne devrait pas y avoir autre chose que des définitions de fonctions.
#       Retirer le TODO une fois complété.
# TODO: Supprimer le code et les commentaires superflux.
# TODO: Supprimer les TODO une fois complété.
