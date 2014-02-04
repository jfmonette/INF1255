# -*- coding: utf-8 -*-
'''
Created on Jan 27, 2014

@author: moe
'''
# Veuillez noter que cet exercice a été complétement modifié car son ancienne
# version n'était pas tout à fait fonctionnelle.
#
# Les opérateurs ne sont pas seulement évalués de la gauche vers la droite.
# Comme pour les opérateurs arithmétiques, il existe un ordre d'évaluation
# des opérateurs booléens. Ils sont évalués selon l'ordre suivant :
# 1-not
# 2-and
# 3-or
# Vous devez exécuter ce fichier puis répondre soit
# par True ou False. Mettez vous dans la peau de l'interpréteur de Python
# et entrez la valeur qui serait retournée.
#
# Vous n'avez pas à modifier ce code.

enonces = ["False or not True and True",
           "False and not True or True",
           "True and not (False or False)",
           "not not True or False and not True",
           "False or not (True and True)"]

parsed_item = None
for item in enonces:
    print item
    exec ("parsed_item = " + item)
    if parsed_item != input():
        print "L'évaluation de l'expression ", item, "aurait dû retourner", parsed_item