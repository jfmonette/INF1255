# -*- coding: utf-8 -*-
'''
Created on Jan 28, 2014

@author: moe
'''
# Lorsque l'on commence à créer des programmes de plus grandes envergure, la quantité de
# code augmente inévitablement. Afin de diviser les différentes parties de notre code
# de façon cohérente et logique, python offre la possibilité d'utiliser les packages pour
# découper/diviser/organiser notre code. Dans cet exercice, vous devrez importer le module 
# etudiant se trouvant dans le package uqam afin que le code ci-dessous puisse s'exécuter. 
#
# Le code suivant est brisé, vous devez le réparer en important le module uqam.etudiant. 
# La syntaxe pour importer un module est la suivante : import <nom_du_package.nom_du_module>
import uqam.etudiant

eleve = uqam.etudiant.Etudiant()
eleve.nom = "Monette"
eleve.prenom = "Jean-François"
print eleve.prenom, eleve.nom
