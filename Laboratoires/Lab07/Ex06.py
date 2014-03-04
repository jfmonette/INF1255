# -*- coding: utf-8 -*-
'''
Created on 2014-03-04

@author: moe
'''

'''
Mettons en pratique ce que nous avons appris jusqu'ici.

Premièrement, créez une fonction nommée 'cube' qui s'attend à recevoir un 'nombre' comme paramètre. N'oubliez pas les parethèses et le':'.
Assurez-vous que cette fonction retourne nombre passé en paramètre à la puissance 3.

Définissez une deuxième fonction appelée 'divisible_par_trois' qui prend en paramètre à nouveau un 'nombre'. Si ce nombre est divisible
par 3, cette fonction doit retourner 'True', autrement elle doit retourner 'False'.

Définissez les fonctions 'cube' et 'divisible_par_trois' à partir de la ligne 19.
'''


nombre = 3
resultat_attendu = 9

if  cube(nombre) == resultat_attendu:
    print "La fonction 'cube' est correctement implémentée."
else :
    print "Vous devez revoir votre implémentation de la fonction 'cube'."

resultat_attendu = True
if  divisible_par_trois(nombre) == resultat_attendu:
    print "La fonction 'resultat_attendu' est correctement implémentée."
else :
    print "Vous devez revoir votre implémentation de la fonction 'resultat_attendu'."

