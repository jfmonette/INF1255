# -*- coding: utf-8 -*-
'''
Created on Jan 27, 2014

@author: moe
'''
# Veuillez noter que cet exercice a été complétement modifié car son ancienne
# version n'était pas tout à fait fonctionnelle.
#
# L'opérateur not retourne True lorsque l'expression est fausse et False lorsque
# l'expression est vraie. Vous devez exécuter ce fichier puis répondre soit
# par True ou False. Mettez vous dans la peau de l'interpréteur de Python
# et entrez la valeur qui serait retournée.
#
# Vous n'avez pas à modifier ce code.

enonces = ["not True",
           "not 3**4 < 4**3",
           "not 10 % 3 <=  10 % 2",
           "not 3**2 + 4**2 != 5**2",
           "not not False"]

parsed_item = None
for item in enonces:
    print item
    exec ("parsed_item = " + item)
    if parsed_item != input():
        print "L'évaluation de l'expression ", item, "aurait dû retourner", parsed_item