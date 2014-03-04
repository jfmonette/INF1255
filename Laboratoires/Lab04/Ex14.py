# -*- coding: utf-8 -*-
'''
Created on 2014-02-03

@author: moe
'''
from random import randint 
# Nous allons maintenant mettre en pratique l'ensemble des connaissances acquises jusqu'ici.
# Pour ce faire, nous construirons un jeu similaire à Battleship (http://en.wikipedia.org/wiki/Battleship_(game)).
# Premièrement, nous auront besoin d'un plateau de jeu.
#
# Créez une variable appelée 'plateau' et assignez lui une liste vide comme valeur.

# Nous voulons que notre plateau soit de format 5x5. En utilisant l'instruction "append", insérez
# 5 listes (ces listes représentent les lignes) au le plateau. Chacune des ses listes doit contenir
# 5 fois la valeur '0' (dans le cadre de notre jeu, ce '0' indiquera que la case est vide.

# Maintenant que nous avons un plateau de jeu de créé, regardons ce qu'il contient. Utilisez
# l'instruction print afin d'imprimer le contenu du plateau. Le résultat devrait ressembler à
# ceci : [0, 0, 0, 0, 0]
#	 [0, 0, 0, 0, 0]
#	 [0, 0, 0, 0, 0]
#	 [0, 0, 0, 0, 0]
#	 [0, 0, 0, 0, 0]

# Maintenant que nous avons un plateau de jeu complet, il faut maintenant y cacher un bateau.
# Notre de liste de liste correspond en fait à un tableau à deux dimensions. Nous aurons donc
# besoin de deux nombres afin de déterminer la position du bateau.
#
# Vous devez déclarez deux variables : ligne_du_bateau et colonne_du_bateau. De plus, utilisez
# l'instruction suivante pour les initialiser : nom_de_la_variable = randint(0, 5)

# Nous avons maintenant les coordonnées du bateau. Nous allons maintenant créer des variables
# permettant de stocker les coordonnées entrées par le joueur.
#
# Créez deux variables appelées : 'essai_ligne' et 'essai_colonne'.

# Créez maintenant une boucle while qui demande au joueur d'entrer un essai de coordonnées.
# Si cet essai correspond aux coordonnées du bateau, il faut afficher "Touché, coulé !"
# Sinon, il faut insérer la valeur 1 sur le plateau aux coordonnées entrées par le joueur
# et ensuite afficher le plateau puis redemander au joueur d'entrer de nouvelles coordonnées.
