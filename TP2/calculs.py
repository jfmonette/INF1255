# -*- coding: utf-8 -*-
import contribuables

def brutTotal(un_contribuable):
    return sum(retourner_liste_de_montants_bruts(un_contribuable["Revenu"]))

def retourner_liste_de_montants_bruts(une_liste_de_revenus):
    montants_bruts = []
    for un_revenu in une_liste_de_revenus:
        montants_bruts.append(un_revenu["Brut"])
    return montants_bruts

def brutCa(un_contribuable):
    revenus_canadiens = retourner_liste_de_revenus_canadiens(un_contribuable["Revenu"])
    return brutTotal(revenus_canadiens))

def retourner_liste_de_revenus_canadiens(une_liste_de_revenus):
    revenus_canadiens = []
    for un_revenu in une_liste_de_revenus:
        if un_revenu["Pays"] == "ca":
            revenus_canadiens.append(un_revenu)
    return revenus_canadiens

def brutImposable(un_contribuable):
    brut_imposable = 0
    brut_total = brutTotal(un_contribuable)
    if brut_total > 6800:
        brut_imposable = brut_total - brutCa(un_contribuable)
    return brut_imposable

def calculImpot(un_contribuable):
    un_contribuable["Impot"] = brutImposable(un_contribuable) * 0.35

def calculBalance(un_contribuable):
    un_contribuable["Balance"] = un_contribuable["Impot"] - un_contribuable["Prelevements"]

def impotsEtBalances(une_liste_de_contribuables):
    for un_contribuable in une_liste_de_contribuables:
        calculImpot(un_contribuable)
        calculBalance(un_contribuable)
