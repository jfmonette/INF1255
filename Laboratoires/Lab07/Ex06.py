# -*- coding: utf-8 -*-
'''
Created on 2014-03-04

@author: moe
'''

'''
Mettons en pratique ce que nous avons appris jusqu'ici.

Premièrement, créez une fonction nommée 'elever_au_cube' qui s'attend à recevoir un 'nombre' comme paramètre. N'oubliez pas les parethèses et le':'.
Assurez-vous que cette fonction retourne nombre passé en paramètre à la puissance 3.

Définissez une deuxième fonction appelée 'est_divisible_par_trois' qui prend en paramètre à nouveau un 'nombre'. Si ce nombre est divisible
par 3, cette fonction doit retourner 'True', autrement elle doit retourner 'False'.

Définissez les fonctions 'elever_au_cube' et 'est_divisible_par_trois' à partir de la ligne 19.

Exécutez votre code et regardez les résultats.
'''


nombre = 3
resultat_attendu = 9

if  elever_au_cube(nombre) == resultat_attendu:
    print "La fonction 'elever_au_cube' est correctement implémentée."
else :
    print "Vous devez revoir votre implémentation de la fonction 'elever_au_cube'."

resultat_attendu = True
if  est_divisible_par_trois(nombre) == resultat_attendu:
    print "La fonction 'resultat_attendu' est correctement implémentée."
else :
    print "Vous devez revoir votre implémentation de la fonction 'resultat_attendu'."

