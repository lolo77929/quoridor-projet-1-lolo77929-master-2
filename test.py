# -*- coding: utf-8 -*-
"""Module de test unitaire

Test unitaire pour les différents modules du jeu Quoridor.

Pour plus d'information sur le module pytest:
    https://docs.pytest.org/en/latest/

Examples:
    Exécution des tests:

    `> python test.py`

    =================================== test session starts ===================================
    Python 3.8.0, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- C:/Python38/python.exe
    cachedir: .pytest_cache
    rootdir: D:/Git/GLO1901H20
    plugins: requests-mock-1.7.0
    collected 2 items

    test.py::test_initialiser_partie_raise_runtime_error PASSED                         [ 50%]
    test.py::test_initialiser_partie_return_tuple PASSED                                [100%]

    ==================================== 2 passed in 0.16s ====================================
"""
import pytest
import api

def test_initialiser_partie_raise_runtime_error():
    """Test de soulèvement de l'erreur de la fonction initialiser_partie

    Test que la fonction soulève l'erreur RuntimeError lorsqu'on lui
    passe un paramètre invalide.

    Nous importons le module a l'intérieur de la fonction pour assurer
    que le test soit indépendant.
    """

    idul_invalide = "j"

    with pytest.raises(RuntimeError):
        api.initialiser_partie(idul_invalide)


def test_initialiser_partie_return_tuple():
    """Test du type de retour de la fonction initialiser_partie

    Test que la fonction retourne un tuple composé d'une string et d'un dictionnaire.

    Nous importons le module a l'intérieur de la fonction pour assurer
    que le test soit indépendant.
    """

    idul_valide = "josmi42"
    partie = api.initialiser_partie(idul_valide)

    assert isinstance(partie, tuple)
    assert isinstance(partie[0], str)
    assert isinstance(partie[1], dict)


# TODO: Dans ce fichier vous trouverez un exemple de (2) tests unitaires fonctionnels,
#       vous pouvez vous en inspirer si vous désirer en créer d'autre!
#       La création de test unitaire n'est pas demandé dans le Projet 1.
#       Plus d'information dans les liens en haut...

if __name__ == "__main__":
    # Appel de pytest en spécifiant le fichier à tester
    # Nous demandons aussi d'afficher plus de verbose avec l'option '-v'
    # Permet le lancement des test en exécutant directement le ficher
    # > python test.py
    pytest.main(['-v', 'test.py'])
