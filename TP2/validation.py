# -*- coding: utf-8 -*-
import lieux
import contribuables

def valideNN(un_nombre):
    return est_un_entier(un_nombre) and est_exclusivement_positif(un_nombre)

def est_un_entier(un_nombre):
    return isinstance(un_nombre, int)

def est_exclusivement_positif(un_nombre):
    return un_nombre > 0

def valideNom(un_nom):
    return un_nom.isalpha() and len(un_nom) >= 2

def valideMontant(un_nombre):
    return isinstance(un_nombre, float) or isinstance(un_nombre, int)

def valideCodePostal(un_code_postal):
    return un_code_postal in lieux.villes

def validePays(un_code_pays):
    return un_code_pays in lieux.pays

def valideRevenu(une_liste):
    return est_une_liste_de_revenus(une_liste) and sont_des_revenus_valides(une_liste)

def est_une_liste_de_revenus(une_liste):
    return type(une_liste) is list and contient_seulement_des_revenus(une_liste)

def contient_seulement_des_revenus(une_liste):
    contient_seulement_des_revenus = True
    for une_entree in une_liste:
        if not est_un_revenu(une_entree):
            contient_seulement_des_revenus = False
            break
    return contient_seulement_des_revenus

def est_un_revenu(une_entree):
    return len(une_entree) == 2 and "Pays" in une_entree and "Brut" in une_entree

def sont_des_revenus_valides(une_liste_de_revenus):
    tous_les_revenus_sont_valides = True
    for un_revenu in une_liste_de_revenus:
        if  not est_un_revenu_valide(un_revenu):
            tous_les_revenus_sont_valides = False
            break
    return tous_les_revenus_sont_valides

def est_un_revenu_valide(un_revenu):
    return validePays(un_revenu["Pays"]) and valideMontant(un_revenu["Brut"])

def valideContribuable(un_contribuable):
    return valideNN(un_contribuable["NN"]) and \
           valideNom(un_contribuable["Nom"]) and \
           valideCodePostal(un_contribuable["CodePostal"]) and \
           valideRevenu(un_contribuable["Revenu"])

def listeContribuablesValides(une_liste_de_contribuables):
    contribuables_valides = []
    for un_contribuable in une_liste_de_contribuables:
        if valideContribuable(un_contribuable):
            contribuables_valides.append(un_contribuable)
    return contribuables_valides
