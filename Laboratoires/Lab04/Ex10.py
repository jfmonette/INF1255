# -*- coding: utf-8 -*-
'''
Created on 2014-02-03

@author: moe
'''
# Dans un exercice précédant, nous avons vu la boucle 'while'. L'exécution de cette boucle dépend de la
# condition qui lui est rattachée. (Ex: while count < 10)
#
# Selon la condition que l'on choisie, il se peut que cette boucle ne s'exécute pas du tout. Une bonne façon
# de forcer la boucle à s'exécuter au moins une fois est de mettre comme condition du 'while' la valeur True
# et d'utiliser l'instruction 'break' afin de contrôler l'arrêt de la boucle.
#
# La boucle ci-dessous ne s'exécutera pas dans l'état où elle est. Utilisez l'astuce du while-true-break 
# afin de forcer la boucle à s'exécuter au moins une fois.

count = 10

while count < 10
	print count
	count += 1
