# -*- coding: utf-8 -*-
'''
Created on 2014-02-03

@author: moe
'''
# Une autre façon d'effectuer des boucles est l'utilisation de l'instruction for.
# Le code ci-dessous montre comment itérer au travers des éléments d'une liste.
#
# Modifiez le code ci-dessous afin d'afficher les nombre par leur valeur sous forme
# de chaîne de caractères. (ex : 5 --> cinq)

print "Python qui compte..."

liste_de_nombres = range(5)
dictionnaire_de_nombres = {1:"Un", 2:"Deux", 3:"Trois", 4:"Quatre", 5:"Cinq"}

for un_nombre in liste_de_nombres:
    print dictionnaire_de_nombres[un_nombre]
