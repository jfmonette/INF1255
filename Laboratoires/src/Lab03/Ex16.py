# -*- coding: utf-8 -*-
'''
Created on Jan 28, 2014

@author: moe
'''
# Dans cet exercice, vous devrez créer votre propre package contenu deux modules.
# En vous basant sur les modules du package uqam, vous devez créer un package nommé
# finance contenant deux modules, soit : personnelles et publiques.
#
# Le code suivant est présentement brisé, lorsque vous aurez créé le package et ses
# modules, il pourra être exécuté.
from finance import *

finance_personnelles = personnelles.Personnelles()
finance_personnelles.investissement = 100

finance_publiques = publiques.Publiques()
finance_publiques.budget = 1000000000

print "Finances personnelles : ", finance_personnelles.investissement, "$"
print "Finances publiques : ", finance_publiques.budget, "$"
print "Félicitations ! Vous pouvez maintenant aller faire l'exercice supplémentaire\
        proposé par le prof."