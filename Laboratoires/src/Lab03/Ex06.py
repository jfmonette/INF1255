# -*- coding: utf-8 -*-
'''
Created on Jan 27, 2014

@author: moe
'''
# Veuillez noter que cet exercice a été complétement modifié car son ancienne
# version n'était pas tout à fait fonctionnelle.
#
# L'opérateur and retourne True lorsque les expressions des deux côtés de
# l'opérateur sont vraies. Sinon, il retourne False. Vous devez exécuter ce 
# fichier puis répondre soit par True ou False. Mettez vous dans la peau de 
# l'interpréteur de Python et entrez la valeur qui serait retournée.
#
# Vous n'avez pas à modifier ce code.

enonces = ["False and False",
           "-(-(-(-2))) == -2 and 4 >= 16**0.5",
           "19 % 4 != 300 / 10 / 10 and False",
           "-(1**2) < 2**0 and 10 % 10 <= 20 -10 *2",
           "True and True"]

parsed_item = None
for item in enonces:
    print item
    exec ("parsed_item = " + item)
    if parsed_item != input():
        print "L'évaluation de l'expression ", item, "aurait dû retourner", parsed_item