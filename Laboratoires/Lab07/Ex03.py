# -*- coding: utf-8 -*-
'''
Created on 2014-03-03

@author: moe
'''

'''
Après avoir définit une fonction, elle doit être appelée afin d'être exécutée.
Dans l'exercice précédent, l'instruction BonjourMonde() demandait au programme de trouver la fonction appelée 'BonjourMonde'
et d'exécuter les instructions se trouvant à l'intérieur.

Nous avons créé la fonction 'puissance_deux'. Appelez la avec le paramètre nombre (placez le paramètre entre les parenthèse de 
puissance_deux() sur la ligne 23.
'''

"""Retourne la puissance deux d'un nombre."""
def puissance_deux(nombre):
    puissance_deux = nombre**2
    return puissance_deux

nombre = 10
puissance_deux = # Votre code
print "Le nombre %d au carré est égale à %d." % (nombre, puissance_deux)
