# -*- coding: utf-8 -*-
'''
Created on Jan 27, 2014

@author: moe
'''
# Rappel des comparateurs :
# égalité : =
# non-égalité : !=
# plus petit que : <
# plus petit ou égal à : <=
# plus grand que : >
# plus grand ou égal à : >=
#
# Vous devez exécuter ce fichier puis répondre soit
# par True ou False. Mettez vous dans la peau de l'interpréteur de Python
# et entrez la valeur qui serait retournée.
#
# Vous n'avez pas à modifier ce code.

reponses = {"17 < 118 % 100":False,
            "100 == 33 * 3 + 1":False,
            "19 <= 2**4": False,
            "-22 >= -18": True,
            "99 != 98 + 1": True
            }

bonnes_reponses = 0

for key in reponses:
    print key
    resultat = None
    exec("resultat = " + key)
    if resultat == input():
        bonnes_reponses =+ 1
    else:
        print "Le résultat de l'évaluation de l'expression %s devrait être %s" % (key, resultat)
        print "Vous avez plutôt indiqué ", reponses[key]