# -*- coding: utf-8 -*-
'''
Created on Jan 27, 2014

@author: moe
'''
# Veuillez noter que cet exercice a été complétement modifié car son ancienne
# version n'était pas tout à fait fonctionnelle.
#
# L'opérateur or retourne True lorsque l'une des expressions des deux côtés de
# l'opérateur est vraie. Sinon, il retourne False. Vous devez exécuter ce fichier
# puis répondre soit par True ou False. Mettez vous dans la peau de l'interpréteur
# de Python et entrez la valeur qui serait retournée.
#
# Vous n'avez pas à modifier ce code.

enonces = ["2**3 == 108 % 100 or 'Bonheur' == 'Argent'",
           "True or False",
           "100**0.5 >= 50 or False",
           "True or True",
           "1**100 == 100**1 or 3 * 2 * 1 != 3 + 2 + 1"]

parsed_item = None
for item in enonces:
    print item
    exec ("parsed_item = " + item)
    if parsed_item != input():
        print "L'évaluation de l'expression ", item, "aurait dû retourner", parsed_item