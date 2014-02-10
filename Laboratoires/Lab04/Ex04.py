# -*- coding: utf-8 -*-
'''
Created on 2014-02-01

@author: moe
'''
# Une boucle peut s'exécuter à l'infini si elle possède une condition qui
# ne peut jamais devenir fausse ou si la logique à l'intérieur de la boucle
# ne permet pas à la condiftion de devenir fausse.
#
# La boucle ci=dessous est une boucle infinie. Réparez la avant de lancer
# l'exécution de ce programme.
count = 0

while count <=10:
    print count
    count += 1
