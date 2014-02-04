# -*- coding: utf-8 -*-
'''
Created on 2014-02-04

@author: moe
'''
# Révision portant sur la structure "dictionnaire" en vue du premier lab noté.

# Créer un dictionnaire vide
dictionnaire = {}

# Créer un dictionnaire déjà initialisé
dictionnaire = {1:"Jean",
                2:"Roger",
                3:"Pierre"}

# Vider complètement un dictionnaire
dictionnaire = {} # équivalent à créer une nouvelle dictionnaire vide

# Ajout/Mise à jour d'éléments dans un dictionnaire
dictionnaire.update({1:"Jean"})
dictionnaire.update({2:"Roger"})
dictionnaire.update({2:"Georges"}) # L'entrée 2:"Roger" se fait ici écraser par l'entrée 2:"Georges"
dictionnaire[3] = "Pierre" # Une autre façon d'ajouter la valeur "Pierre" ayant comme clé 3 dans le dictionnaire

# Enlever des éléments d'une dictionnaire
del(dictionnaire[1]) # enlève l'élément ayant comme clé la valeur 1 dans le dictionnaire
del(dictionnaire[2]) # enlève l'élément ayant comme clé la valeur 2 dans le dictionnaire
del(dictionnaire[3]) # enlève l'élément ayant comme clé la valeur 3 dans le dictionnaire

# Ajouter des variables dans une dictionnaire
variable_un = {1:"Jean"}
variable_deux = {2:"Roger"}
variable_trois = {3:"Georges"}
dictionnaire.update(variable_un)
dictionnaire.update(variable_deux)
dictionnaire.update(variable_trois)

# Accéder à un élément de la dictionnaire
print dictionnaire[1] # Imprime la valeur ayant comme clé 1 dans le dictionnaire
print dictionnaire # Imprime l dictionnaire en entier