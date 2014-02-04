# -*- coding: utf-8 -*-
'''
Created on Jan 27, 2014

@author: moe
'''

votre_nom = raw_input('Quel est votre nom ?')
votre_age = input('Quel est votre âge ?')

# Complétez la chaîne de caractères suivante pour quelle affiche
# le contenu des variables déclarées ci-haut
print "Ah, bonjour " + votre_nom + " ! Vous avez " + str(votre_age) + " ans."

# Il existe d'autres façons d'imprimer des chaînes de caractères à
# l'écran.
print "Ah, bonjour %s ! Vous avez %s ans." % (votre_nom, votre_age)

# À votre tour maintenant d'utiliser cette nouvelle façon d'imprimer
# des chaînes de caractères
annee_de_naissance = 2014 - votre_age
print "Donc, si mes calculs sont bons, %s est votre année de naissance " % (annee_de_naissance)
# Prière de noter que ce calcul pourrait être inexacte car il ne tient pas compte de la 
# date de naissance. Nous reviendront probablement sur la manipulation des dates plus
# tard au cours de la session.