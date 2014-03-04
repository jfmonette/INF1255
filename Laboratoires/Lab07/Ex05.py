# -*- coding: utf-8 -*-
'''
Created on 2014-03-04

@author: moe
'''

'''
Nous avons vu que les fonctions peuvent effectuer, entre autres, des opérations arithmétiques. Toutefois, les fonctions peuvent
faire beaucoup plus. Par exemple, les fonctions peuvent appeler d'autres fonctions :

def multiplier_par_cinq(nombre):
    return nombre * 5

def multiplier_par_cinq_plus_sept(nombre):
    return multiplier_par_cinq(nombre) + 7

Regardons les deux fonctions ci-dessous : 'incrementer_de_un' et 'incrementer_de_un_et_multiplier_par_huit'.
Modifiez la fonction 'incrementer_de_un_et_multiplier_par_huit' afin qu'elle utilise la fonction 'incrementer_de_un' dans son calcul.
'''
def incrementer_de_un(nombre):
    return nombre + 1
    
def incrementer_de_un_et_multiplier_par_huit(nombre):
    return (nombre + 1) * 8 # Vous devez modifier cette ligne.

nombre = 10
print "Le nombre %d incrémenté de un est égale à %d." % (nombre, incrementer_de_un(nombre))
print "Le nombre %d incrémenté de un et multiplié par huit est égale à %d." % (nombre, incrementer_de_un_et_multiplier_par_huit(nombre))