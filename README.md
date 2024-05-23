Le code pendu.py implémente le jeu du pendu, permettant à l'utilisateur de deviner un mot choisi aléatoirement par le programme. Le code est ecrit avec des fonctions : 

Lecture des Mots
Fonction pour lire les mots à partir d'un fichier texte (mots_pendu.txt). Ce fichier contient une liste de mots, un par ligne. Si l'utilisateur ne spécifie pas de fichier, le fichier par défaut est utilisé + le mot à deviner est sélectionné aléatoirement à partir de la liste de mots fournie. Cela assure une variété de mots et rend chaque partie unique. 

Suppression des Accents
J'ai utilisé la normalisation Unicode pour convertir les lettres accentuées en leurs équivalents sans accents. Cela simplifie le jeu pour l'utilisateur, qui peut entrer des lettres sans se soucier des accents.

Affichage du Mot à Deviner
Le mot à deviner est affiché avec des underscores pour les lettres pas encore devinées. Cette méthode permet à l'utilisateur de visualiser facilement les progrès faits et les lettres restantes à deviner. Les lettres correctement devinées remplacent les underscores correspondants.

Interaction avec l'Utilisateur
Le jeu demande à l'utilisateur d'entrer une lettre à chaque tour. Cette interaction est simple et intuitive, facilitant l'expérience utilisateur. La lettre est convertie en minuscule.

Vérification des Lettres
Le programme vérifie si la lettre entrée par l'utilisateur fait partie du mot à deviner. Cette vérification est essentielle pour mettre à jour l'état du mot affiché et pour déterminer si l'utilisateur a gagné ou perdu.

BONUS
Lorsqu'il ne lui reste plus qu'une seule chance : une lettre qui n'est pas dans le mot et qui n'a pas encore été devinée est donnée. 

Boucle Principale du Jeu
La boucle principale du jeu gère le déroulement du jeu. Elle continue tant que l'utilisateur a des chances restantes. À chaque tour, le mot actuel et le nombre de chances restantes sont affichés, et l'utilisateur est invité à entrer une lettre. Si l'utilisateur devine correctement toutes les lettres du mot, le jeu se termine par une victoire. Si les chances s'épuisent, le jeu affiche le mot correct et se termine par une défaite. Après chaque partie, l'utilisateur peut choisir de rejouer ou de quitter.
