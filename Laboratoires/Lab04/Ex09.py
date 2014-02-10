# -*- coding: utf-8 -*-
'''
Created on 2014-02-03

@author: moe
'''
# L'instruction 'break' peut être utilisée afin de forcer la sortie d'une boucle. Il s'agit d'une
# autre façon de gérer le nombre de fois qu'une boucle s'exécutera.
#
# Nous reprenons ici l'exemple du dernier exercice. Toutefois, votre code doit utiliser la boucle
# afin d'inspecter la contenu du dictionnaire. Lorsque l'entrée du dictionnaire correspond au contenu
# de la variable 'ville_recherchee', vous devez imprimer l'entrée du dictionnaire puis forcer l'arrêt
# de la boucle à l'aide d'un 'break'. 

villes = {1: "Montréal", 2: "Laval", 3: "Longueil"}
ville_recherchee = "Laval"

for ville in villes:
	# Votre code va ici
	if villes[ville] == ville_recherchee:
		print villes[ville]
		break
