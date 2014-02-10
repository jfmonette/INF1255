# -*- coding: utf-8 -*-
'''
Created on 2014-02-03

@author: moe
'''
# Dans cet exercices, vous n'avez pas à modifier de code. Observez le code et soyez attentif aux commentaires.
# Revenons maintenant aux boucles. Il est possible d'imbriquer une boucle à l'intérieur d'une autre boucle.
# Dans l'exemple ci-dessous, nous utilisons des boucles imbriquées afin d'afficher le contenu d'une liste
# de listes.

echiquier = [["a1","b1","c1","d1","e1","f1","g1","h1"], 
	     ["a2","b2","c2","d2","e2","f2","g2","h2"],
	     ["a3","b3","c3","d3","e3","f3","g3","h3"],
	     ["a4","b4","c4","d4","e4","f4","g4","h4"],
	     ["a5","b5","c5","d5","e5","f5","g5","h5"],
	     ["a6","b6","c6","d6","e6","f6","g6","h6"],
	     ["a7","b7","c7","d7","e7","f7","g7","h7"],
	     ["a8","b8","c8","d8","e8","f8","g8","h8"]]

for ligne in echiquier:
	for colonne in ligne:
		print colonne

# Il est aussi possible d'imbriquer des boucles 'while' de la même façon. Le code ici bas produira exactement
# la même sortie que le code d'en-haut. Vous remarquerez sans doute qu'il est beaucoup élégant et plus lisible
# d'utiliser des boucles for quand vient le temps de manipuler des listes de listes.
nombre_de_lignes = len(echiquier)
i = 0

while i < nombre_de_lignes:
	nombre_de_colonnes = len(echiquier[i])
	j = 0
	while j < nombre_de_colonnes:
		print echiquier[i][j]
		j += 1
	i += 1

