# Quoridor - Partie 1

<img src="https://python.gel.ulaval.ca/media/notebook/quoridor.png" style="display: block; margin-left: auto; margin-right: auto;" alt="Quoridor" width="50%" height="auto">

## Objectifs

Pour ce projet, vous allez réaliser un premier programme qui interagit avec la **ligne de commande** et qui accède à **Internet**. Vous allez aussi vous familiariser avec la logistique des projets, c'est-à-dire installer sur votre ordinateur un environnement de développement [VS Code](https://code.visualstudio.com/) et vous initier à un logiciel de gestion des révisions [Git](https://git-scm.com/).

## Prérequis

- [Git](https://git-scm.com/downloads/)
- [Python pour macOS](https://www.python.org/downloads/), [Python pour Windows](https://www.microsoft.com/fr-ca/p/python-38/9mssztt1n39l)
- [VS Code](https://code.visualstudio.com/download/)

## Extension VS Code

Voici la liste des extensions **VS Code** que nous vous conseillons d'ajouter à votre configuration:

- Python (&thinsp;celui de Microsoft&thinsp;)
- GitLens - Git supercharged
- Bracket Pair Colorizer
- Indent-Rainbow
- autoDocstring
- Live Share (*Pour le dépannage en ligne*)
- Live Share Extension Pack (*Pour le dépannage en ligne*)

Pour **autoDocstring**, allez ensuite dans la barre de menu en haut à gauche et ensuite dans `Fichier -> Préférences -> Paramètres`, dans la barre de recherche apparaissant dans la fenêtre chercher `Auto Docstring`.
Vous devriez voir un menu déroulant en dessous de **Docstring Format**, choisissez l'option `google`.

## Commandes utile

Afficher l'aide&thinsp;:

``` bash
> python3 main.py --help
```

Démarrer une partie&thinsp;:

``` bash
> python3 main.py votre_idul
```

Lancer le module de test&thinsp;:

``` bash
> python3 test.py
```

*NOTE&thinsp;: Pour lancer le module de test, vous aurez besoin d'installer le module externe `pytest`.*

Installer un module externe **Python**&thinsp;:

``` bash
> pip3 install nom_du_module
```

Créer un bundle&thinsp;:

``` bash
> git bundle create quoridor.bundle HEAD master
```

Vérifier que le bundle a été créé avec succès&thinsp;:

``` bash
> git bundle verify quoridor.bundle
```

Unbundler un bundle&thinsp;:

``` bash
> git clone quoridor.bundle
```

## Liens utile

- [Aide-mémoire Github Git](https://github.github.com/training-kit/downloads/fr/github-git-cheat-sheet.pdf)
- [Documentation Pytest](https://docs.pytest.org/en/latest/) [&thinsp;en anglais&thinsp;]
