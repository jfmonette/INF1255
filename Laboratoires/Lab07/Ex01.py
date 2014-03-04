# -*- coding: utf-8 -*-
'''
Created on 2014-03-03

@author: moe
'''

'''
Cet exercice ne requiert aucune modification au code. Nous présentons ici la définition et l'utilisation des fonctions à
l'intérieur d'un programme. À titre de rappel, une fonction est utile lorsque nous souhaitons réutilisons la même portion de code
en utilisant d'autre valeurs (paramètres). Le code ci-dessous modèlise une facture de restaurant incluant les taxes et le pourboire.
Prenez le temps de comprendre la synthaxe et ensuite exécutez le code pour voir le résultat.
'''

"""Ajoute 5% de TPS à une facture."""
def tps(facture):
    facture *= 1.05
    return facture

"""Ajoute 9.975% de taxe à une facture."""
def tvq(facture):
    facture *= 1.09975
    return facture

    """Ajoute 15% de pourboire à une facture."""
def pourboire(facture):
    facture *= 0.15
    return facture
    
cout_du_repas = 100
cout_du_repas_avec_tps = tps(cout_du_repas)
cout_du_repas_avec_tvq = tps(cout_du_repas_avec_tps)
cout_du_repas_avec_pourboire = pourboire(cout_du_repas)

print "Coût du repas : %.2f $" % cout_du_repas
print "Après TPS : %.2f $" % cout_du_repas_avec_tps
print "Après TVQ : %.2f $" % cout_du_repas_avec_tvq
print "Avec pourboire : %.2f $" % (cout_du_repas_avec_tvq + cout_du_repas_avec_pourboire)