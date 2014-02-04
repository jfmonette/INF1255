# -*- coding: utf-8 -*-
'''
Created on Jan 27, 2014

@author: moe
'''
# À partir des exemples d'opérateurs de comparaison de l'exercice Ex04,
# créez vos propres expressions selon ce qui vous est demandé. Vous devez
# utiliser au moins trois opérateurs différents.

# Dois être True
bool_un = 1 == 1

# Dois être False
bool_deux = 30 > 100

# Dois être True
bool_trois = 2**2 == 4

# Dois être False
bool_quatre = 4 >= 5

# Dois être True
bool_cinq = 12 + 5 == 17

# Exécutez maintenant votre code pour effectuer la validation.


# Validation - Vous n'avez rien à modifier ici.
resultats = [True, False, True, False, True]
expressionsToutesValides = True
if resultats[0] != bool_un:
    print 'Votre première expression n\'est pas valide.'
    expressionsToutesValides = False
if resultats[1] != bool_deux:
    print 'Votre deuxième expression n\'est pas valide.'
    expressionsToutesValides = False
if resultats[2] != bool_trois:
    print 'Votre troisième expression n\'est pas valide.'
    expressionsToutesValides = False
if resultats[3] != bool_quatre:
    print 'Votre quatrième expression n\'est pas valide.'
    expressionsToutesValides = False
if resultats[4] != bool_cinq:
    print 'Votre cinquième expression n\'est pas valide.'
    expressionsToutesValides = False
if expressionsToutesValides == True:
    print 'Bravo ! Vous pouvez maintenant passer au prochain exercice.'
