# game_config.py
# Paramètres de l'environnement de jeu
TAILLE_CASE = 20  # Taille d'une case en pixels
NB_CASES = 10  # Nombre de cases sur un côté de la grille

# Paramètres visuels
COULEUR_SERPENT = (144, 238, 144)  # Vert clair
COULEUR_NOURRITURE = (255, 69, 0)  # Rouge orangé pour la pomme
POLICE_TAILLE = 12  # Taille de la police pour le texte affiché à l'écran
VISUALIZATION = True  # Activer ou désactiver la visualisation du jeu
DISPLAY_MODE = (
    "console"  # "full" pour l'interface graphique, "console" pour le mode console
)

# Récompenses et pénalités
REWARD_APPLE = 1  # Récompense pour manger une pomme
REWARD_MOVE = 0.1  # Récompense pour un déplacement valide (sans collision)
PENALTY_COLLISION = -5  # Pénalité pour collision avec soi-même ou les bords de l'écran
REWARD_CLOSE_FOOD = 1  # Récompense pour se rapprocher de la nourriture

# Paramètres de performance
FPS = 100  # Nombre d'images par seconde pour l'animation

# Paramètres de l'interface utilisateur
REAL_TIME_VISUALIZATION = (
    False  # Activer ou désactiver la visualisation en temps réel pendant l'entraînement
)
