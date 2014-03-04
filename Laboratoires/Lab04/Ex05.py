# -*- coding: utf-8 -*-
'''
Created on 2014-02-02

@author: moe
'''
# Tout comme l'instruction if, l'instruction while peut aussi être utilisée avec
# l'instruction else. Le bloc de code rattaché à l'instruction else sera automatiquement
# exécuté dès que la condition du while sera fausse.
#
# Observez le code ci-dessous, puis exécutez le afin de jouer à la loterie de
# l'UQAM. N'accordez pas d'importance à l'instruction random.randint() pour
# l'instant. Vous n'avez pas à modifier le code ci-dessous.
import random

print "Bienvenue à la loterie de l'UQAM !"
print "Des nombres, entre 1 et 10, seront pigés au hasard."
print "Voyons combien de d'essais sont nécessaires pour obtenir un 5 !"

nombre_essais = 0
nombre_qui_a_ete_pige = None

while nombre_qui_a_ete_pige != 5:
    nombre_qui_a_ete_pige = random.randint(1, 10)
    print nombre_qui_a_ete_pige
    nombre_essais += 1
else:
    print "Il a fallu", nombre_essais, "d\'essais avant qu\'un \'5\' soit pigé!"
