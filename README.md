# Projet 3 - Mac Gyver

-----------

## Description
<<<<<<< HEAD

Imaginer un labyrinthe 2D dans lequel MacGyver aurait été enfermé. La sortie est surveillée par un garde du corps dont la coiffure ferait pâlir Tina Turner. Pour le distraire, il vous faut réunir les éléments suivants (dispersés dans le labyrinthe) : une aiguille, un petit tube en plastique et de l'éther. Ils permettront à MacGyver de créer une seringue et d'endormir le garde pour s'échapper du labyrinthe.

### Fonctionnalités

=======
Imaginer un labyrinthe 2D dans lequel MacGyver aurait été enfermé. La sortie est surveillée par un garde du corps dont la coiffure ferait pâlir Tina Turner. Pour le distraire, il vous faut réunir les éléments suivants (dispersés dans le labyrinthe) : une aiguille, un petit tube en plastique et de l'éther. Ils permettront à MacGyver de créer une seringue et d'endormir le garde pour s'échapper du labyrinthe.

### Fonctionnalités
>>>>>>> 805cc7d3c7bfa5ac0f5c87bc24f4170cab128358
1. Il n'y a qu'un seul niveau.
2. La structure (départ, emplacement des murs, arrivée), devra être enregistrée dans un fichier pour la modifier facilement au besoin.
3. MacGyver sera contrôlé par les touches directionnelles du clavier.
4. Les objets seront répartis aléatoirement dans le labyrinthe et changeront d’emplacement si l'utilisateur ferme le jeu et le relance.
5. La fenêtre du jeu sera un carré pouvant afficher 15 sprites sur la longueur. MacGyver devra donc se déplacer de case en case, avec 15 cases sur la longueur de la fenêtre !
6. Il récupèrera un objet simplement en se déplaçant dessus.
7. Le programme s'arrête uniquement si MacGyver a bien récupéré tous les objets et trouvé la sortie du labyrinthe.
8. S'il n'a pas tous les objets et qu'il se présente devant le garde, il meurt (la vie est cruelle pour les héros).
9. Le programme sera standalone, c'est-à-dire qu'il pourra être exécuté sur n'importe quel ordinateur.

---------------

## Release beta 1.0 - 08/05/2020

**Cette version beta permet déjà un fonctionnement du jeu en version graphique** :
* Import et utilisation du module pygame
* Génération d'une carte en fonction d'un fichier
* Insertion aléatoire des outils nécessaire à la réussite
* Possibilité de déplacer le personnage dans le labyrinthe
* Possiblité pour le personnage de récupérer les objets mais les objets s'inversent à la récupération
* Sortie du labyrinthe avec contrôle sur le nombre d'objet récupéré pour la victoire
* Ecran de victoire ou de défaite

**Reste à faire :**
* Probleme sur les classes à répartir dans plusieurs fichiers
* Probleme sur la récupération des outils, lorsqu'un outil est pris il peut s'inverser avec un autre outil présent dans le labyrinthe => *piste de travail sur l'insertion d'une liste*
* Fonction main() trop importante nécessité de diviser la boucle de jeu en deux boucles : 1/ boucle ecran d'accueil et boucle labyrinthe
