# -*- coding: utf-8 -*-
'''
Created on 2014-02-03

@author: moe
'''
# Il est aussi possible d'itérer au travers les entrées d'un dictionnaire.
# Mais qu'obtient-on en itérant au travers les entrées d'un dictionnaire :
# ses clés ? ses valeurs ? un mal de tête ?
#
# La réponse : ses clés. Il est toutefois facile, à partir d'une clé, d'obtenir la
# valeur qui lui est associée grâce à la syntaxe suivante :
# nom_du_dictionnaire[nom_de_la_clé]
#
# Complétez le code ci-dessous afin d'afficher, sur une ligne différente, toutes
# les clés du dictionnaire, suivi d'un espace, puis finalement la valeur rattachée
# à cette clé. Exemple : 1 Montréal
#			 2 Laval
#			 3 Longueil

villes = {1: "Montréal", 2: "Laval", 3: "Longueil"}

for ville in villes:
	print ville, " ", villes[ville] # Votre code va ici
