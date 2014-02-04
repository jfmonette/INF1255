# -*- coding: utf-8 -*-
'''
Created on 2014-02-04

@author: moe
'''
# Révision portant sur la structure "liste" en vue du premier lab noté.

# Créer une liste vide
liste = []

# Créer une liste déjà initialisée
liste = [1, 2, 3]

# Vider complètement une liste
liste = [] # équivalent à créer une nouvelle liste vide

# Ajout d'éléments dans une liste
liste.append(1)
liste.append(2)

# Enlever des éléments d'une liste
del(liste[0]) # enlève l'élément se trouvant à la position 0 dans la liste
liste.remove(2) # enlève l'élément ayant la valeur 2 dans la liste

# Ajouter des variables dans une liste
variable_un = "bonjour"
variable_deux = "gentil"
variable_trois = "python"
liste.append(variable_un)
liste.append(variable_deux)
liste.append(variable_trois)

# Accéder à un élément de la liste
print liste[0] # Imprime l'élément se trouvant à la position 0 dans la liste
print liste # Imprime la liste en entier