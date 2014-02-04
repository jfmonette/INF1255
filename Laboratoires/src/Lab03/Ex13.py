# -*- coding: utf-8 -*-
'''
Created on Jan 27, 2014

@author: moe
'''
# Créer une structure de contrôle If comportant 
# -and, or ou not
# -un comparateur : ==, !=, <, >, <=, >=
# -if, elif, else
# Cette structure doit utiliser les trois variables définies par 
# la fonction questionnaire et doit implémenter l'algorithme suivant :
#
# VALEUR DE RETOUR = False
# SI nom = "Monsieur T"
#   SI sexe = "M"
#     SI age > 60
#        VALEUR DE RETOUR = True
#     FIN SI
#   FIN SI
# FIN SI
# RETOURNER VALEUR DE RETOUR
# soit : nom, sexe et age.
#
# Une fois l'implémentation  terminée, exécutez le programme et assurez vous que la
# valeur True s'affiche à la console.
def questionnaire(nom, sexe, age):
    valeur_de_retour = False
    if nom == "Monsieur T":
        if sexe == "M":
            if age > 60:
                valeur_de_retour = True
    return valeur_de_retour

print questionnaire("Monsieur T", "M", 61)
