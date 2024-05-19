# Snake AI Project

## Description

Ce projet implémente une intelligence artificielle pour jouer au jeu Snake en utilisant l'algorithme de recherche A*. Le projet est développé en Python et utilise la bibliothèque Pygame pour l'affichage graphique. L'IA utilise A* pour trouver le chemin optimal vers la nourriture tout en évitant les obstacles (le corps du serpent et les murs).

## Prérequis

- Python 3.6 ou plus
- Pygame
- Numpy

## Installation

1. Clonez le dépôt sur votre machine locale :

    ```bash
    git clone https://github.com/votre-utilisateur/snake-ai.git
    cd snake-ai
    ```

2. Installez les dépendances requises :

    ```bash
    pip install -r requirements.txt
    ```

## Utilisation

### Mode Graphique

Pour exécuter le jeu en mode graphique (Pygame), utilisez la commande suivante :

```bash
python3 main.py full
```

### Mode Console

Pour exécuter le jeu en mode console (sans interface graphique), utilisez la commande suivante :

```bash
python3 main.py console
```

### Strucutre du projet:

```
.
├── ai.py                # Contient l'implémentation de l'algorithme A*
├── game.py              # Contient la logique du jeu Snake
├── game_config.py       # Contient les paramètres de configuration du jeu
├── main.py              # Point d'entrée du projet
├── requirements.txt     # Liste des dépendances du projet
└── README.md            # Ce fichier
```
`main.py`
Le fichier principal qui initialise et exécute le jeu. Il détermine le mode d'affichage (graphique ou console) en fonction des arguments de la ligne de commande.

`game.py`
Contient la classe SnakeGame qui gère la logique du jeu, y compris le mouvement du serpent, la génération de nourriture, la détection des collisions et l'affichage graphique (si activé).

`ai.py`
Contient l'implémentation de l'algorithme A* utilisé par l'IA pour trouver le chemin optimal vers la nourriture.

`game_config.py`
Contient les paramètres de configuration du jeu tels que la taille de la grille, les couleurs du serpent et de la nourriture, les récompenses et les pénalités, ainsi que les paramètres de performance.

### Paramètres de configuration

Le fichier game_config.py contient plusieurs paramètres que vous pouvez ajuster pour modifier le comportement du jeu et de l'IA :

- TAILLE_CASE : Taille d'une case en pixels.
- NB_CASES : Nombre de cases sur un côté de la grille.
- COULEUR_SERPENT : Couleur du serpent.
- COULEUR_NOURRITURE : Couleur de la nourriture.
- POLICE_TAILLE : Taille de la police pour le texte affiché à l'écran.
- REWARD_APPLE : Récompense pour manger une pomme.
- REWARD_MOVE : Récompense pour un déplacement valide.
- PENALTY_COLLISION : Pénalité pour collision avec soi-même ou les bords de l'écran.
- REWARD_CLOSE_FOOD : Récompense pour se rapprocher de la nourriture.
- FPS : Nombre d'images par seconde pour l'animation.
- REAL_TIME_VISUALIZATION : Activer ou désactiver la visualisation en temps réel pendant l'entraînement.
- DISPLAY_MODE : "full" pour l'interface graphique, "console" pour le mode console.

### Journalisation

Le projet utilise le module de journalisation intégré de Python pour enregistrer les informations de débogage, d'information, d'avertissement et d'erreur. Vous pouvez personnaliser les paramètres de journalisation dans le fichier main.py.

## Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus d'informations.
```
Assurez-vous d'adapter les parties spécifiques telles que l'URL du dépôt GitHub et les détails de la licence en fonction de votre projet. Ce `README.md` fournit une description claire du projet, des instructions d'installation et d'utilisation, ainsi qu'une explication de la structure du projet et des paramètres de configuration.
```