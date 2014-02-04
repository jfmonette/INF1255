# -*- coding: utf-8 -*-
'''
Created on Jan 27, 2014

@author: moe
'''
# Complétez les instructions if dans la fonction suivante afin quelle
# implémente la fonctionnalité plus grand que 8.
 
def plus_grand_8(un_nombre):
    if un_nombre > 8: 
        return True
    else:
        return False

# Validation - Vous n'avez pas à modifier le code ci-bas.
if plus_grand_8(7) == False and plus_grand_8(9) == True:
    print "Bravo ! Passez au prochain exercice."
else:
    print "Recommencez, votre implémentation n'est pas exacte."
