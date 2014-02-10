# -*- coding: utf-8 -*-
'''
Created on 2014-02-03

@author: moe
'''
# Python offre une instruction qui est semblable au 'break' : l'instruction 'continue'.
# Contrairement au 'break', l'instruction 'continue ne force pas l'arrêt complet de la boucle
# mais la force simplement à faire une nouvelle itération.  
#
# Dans le code ci-dessous, vous remarquerez que le 'continue' remplace en quelque sorte
# la présence d'un 'else'. 

for nombre in range(0,30):
	if nombre % 3 == 0:
		print "Le nombre", nombre, "est divisible par trois"
		continue	
	print "Le nombre", nombre, "n'est pas divisible par trois"

# À votre tour maintenant de mettre en pratique cette approche. Transformez la boucle ci-bas afin
# d'éliminer l'utilisation du 'else' grâce à l'instruction 'continue'

for nombre in range(0,30):
        if nombre % 2 == 0:
                print "Le nombre", nombre, "est pair."
	else:
		print "Le nombre", nombre, "est impair."

