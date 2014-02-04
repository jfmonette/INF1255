# -*- coding: utf-8 -*-
'''
Created on Jan 27, 2014

@author: moe
'''
# Complétez les instructions if dans la fonction suivante afin quelle
# implémente la fonctionnalité plus grand ou égal à 8. Cette fonction
# doit retourner :
#  1 lorsque le nombre est plus grand que 8
#  0 lorsque le nombre est égale à 8
#  -1 lorsque le nombre est plus petit
 
def plus_grand_egal_8(un_nombre):
    if un_nombre > 8:
        return 1
    elif un_nombre == 8:
        return 0
    else:
        return -1

# Validation - Vous n'avez pas à modifier le code ci-bas.
if plus_grand_egal_8(7) == -1 and plus_grand_egal_8(9) == 1 and plus_grand_egal_8(8) == 0:
    print "Bravo ! Passez au prochain exercice."
else:
    print "Recommencez, votre implémentation n'est pas exacte."
