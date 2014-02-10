# -*- coding: utf-8 -*-
'''
Created on 2014-02-02

@author: moe
'''
# Pour cet exercice, vous devez créer un jeu semblable à celui du dernier exercice.
# Le code ci-dessous génère un nombre aléatoire entre 1 et 10. Vous devez permettre
# à l'utilisateur de votre programme de deviner à trois reprises le nombre qui a
# été généré. 
#
# Si l'utilisateur devine le nombre pigé, vous devez afficher :
# "Bravo, vous avez deviné le nombre qui a été pigé !" et ensuite cesser l'exécution
# du programme en utilisant l'instruction break.
#
# S'ils ne devinent pas correctement le nombre pigé en trois essais, l'instruction
# else de la boucle while devra afficher "Vous avez perdu."
#
# N'oubliez pas de mettre à jour le nombre d'essais restants :-)

import random

print "Bienvenue à la loterie interactive de l'UQAM !"
print "Un nombre aléatoire entre 1 et 10 sera pigé."
print "Vous avez trois essais pour tenter de deviner quel est ce nombre."
print "-----------------------------------------------------------------"

nombre_aleatoire = random.randint(1, 10)
essais_restants = 3
nombre_choisi = None
# Créer votre jeu ici.
