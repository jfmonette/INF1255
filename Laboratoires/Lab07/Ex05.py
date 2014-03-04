# -*- coding: utf-8 -*-
'''
Created on 2014-03-04

@author: moe
'''

'''
Nous avons vu que les fonctions peuvent effectuer, entre autres, des opérations arithmétiques. Toutefois, les fonctions peuvent
faire beaucoup plus. Par exemple, les fonctions peuvent appeler d'autres fonctions :

def fois_cinq(nombre):
    return nombre * 5

def fois_cinq_plus_sept(nombre):
    return fois_cinq(nombre) + 7

Regardons les deux fonctions ci-dessous : 'incremente_de_un' et 'incremente_de_un_et_multiplie_par_huit'.
Modifiez la fonction 'incremente_de_un_et_multiplie_par_huit' afin qu'elle utilise la fonction 'incremente_de_un' dans son calcul.
'''
def incremente_de_un(nombre):
    return nombre + 1
    
def incremente_de_un_et_multiplie_par_huit(nombre):
    return nombre + 2 # Vous devez modifier cette ligne.

nombre = 10
print "Le nombre %d incrémenté de un et multiplié par huit est égale à %d." % (nombre, incremente_de_un(nombre), incremente_de_un_et_multiplie_par_huit(nombre))