# -*- coding: utf-8 -*-
'''
Created on 2014-02-01

@author: moe
'''
# La boucle while est souvent utilisée pour valider des données entrées par
# un utilisateur. Par exemple, si l'on demande à l'utilisateur d'entrer Oui
# ou Non et que celui-ci répond par une chiffre, notre programme devrait lui
# demander à nouveau d'entrer une réponse valide.
#
# Remplissez le condition de cette boucle afin que l'utilisateur soit obligé
# de répondre par Oui ou Non
choix = raw_input("Aimez-vous les serpents ? (Oui/Non)")

while choix not in ["Oui", "Non"]:
    choix = raw_input("Aimez-vous les serpents ? (Oui/Non)")
