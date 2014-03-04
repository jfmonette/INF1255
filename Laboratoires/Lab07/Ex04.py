# -*- coding: utf-8 -*-
'''
Created on 2014-03-03

@author: moe
'''

'''
Réexaminons la première qui définissait la fonction puissance_deux dans l'exercice précédent :

def puissance_deux(n):
n est un paramètre de 'puissance_deux'. Un paramètre agit comme un nom de variable qui est passé à la fonction comme un paramètre.
Dans l'exemple précédent, nous avons appelé la fonction 'puissance_deux' avec comme paramètre 'nombre'. Dans ce cas-ci, le paramètre
nombre contenait la valeur 10. Une fonction peut contenir autant de paramètre que l'on veut. Toutefois, lorsque l'on appelle la fonction,
il faut généralement passé un nombre définit de paramètres.

Dans le code ci-dessous, observez la fonction 'puissance'. Elle s'attend à recevoir deux paramètres: un nombre et son exposant. Son 
intention est retourner le résultat d'un nombre mis à la puissance d'un exposant. Cette fonction est présentement brisée puisque ses
paramètres sont manquants.

Vous devez remplacer les '___' par les paramètres 'nombre' et 'exposant' et ensuite appeler la fonction puissance avec les paramètres
nombre et puissance étant égaux à 37 et 4 respectivement.
'''

def puissance(___, ___):  # Ajoutez vos paramètres ici.
    resultat = nombre**exposant
    return resultat

nombre = # Ajoutez la valeur de 'nombre' ici.
exposant = # Ajoutez la veleur de 'exposant' ici.
resultat = puissance(___, ___)  # Ajoutez vos arguments ici.
print "Le nombre %d exposant %d est égale à %d." % (nombre, exposant, resultat)