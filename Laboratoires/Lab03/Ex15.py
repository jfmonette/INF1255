# -*- coding: utf-8 -*-
'''
Created on Jan 28, 2014

@author: moe
'''
# Dans cet exercice, vous devrez importer l'ensemble des modules se trouvant dans le
# package uqam afin que le code ci-dessous puisse s'exécuter.
# 
# Le code suivant est brisé, vous devez le réparer en important l'ensemble des modules
# du package uqam. La syntaxe pour importer tous les modules est la suivante :
# from <nom_du_package> import *
from uqam import *

eleve = etudiant.Etudiant()
eleve.nom = "Monette"
eleve.prenom = "Jean-François"
print eleve.prenom, eleve.nom

enseignant = enseignant.Enseignant()
enseignant.nom = "Tsheke"
enseignant.prenom = "Johnny"
print enseignant.prenom, enseignant.nom

# Allez voir le contenu du fichier uqam.__init__.py pour voir comment l'importation de
# tous les modules est rendue possible.
