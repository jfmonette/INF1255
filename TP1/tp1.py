'''
Created on 2014-03-11

@author: moe
'''
'''
Created on 2014-03-11

@author: fk891479
'''
codes_postaux_valides = [{"id":1000, "ville":"Bruxelles"},
                         {"id":3000, "ville":"Anvers"},
                         {"id":4000, "ville":"Liege"}]

def demander_informations_un_contribuable():
    nn = input("NN ?")
    nom = raw_input("Nom ?")
    prenom = raw_input("Prenom ?")
    brut = input("Brut ?")
    prelevement = input("Prelevement ?")
    code_postal = demander_un_code_postal_valide()
    
    return {"NN":nn, "Nom":nom, "Prenom":prenom, "Brut":brut,
            "Prelevement": prelevement, "Code postal":code_postal}

def demander_un_code_postal_valide():
    code_postal = input("Code postal ?")
    while not est_un_code_postal_valide(code_postal):
        code_postal = input("Code postal ?")
    
    return code_postal

def est_un_code_postal_valide(un_code_postal):
    est_valide = False
    for code_postal_valide in codes_postaux_valides:
        if un_code_postal == code_postal_valide["id"]:
            est_valide = True    

    return est_valide

def demander_informations_plusieurs_contribuables():
    contribuables = []
    continuer = True
    while continuer:
        contribuables.append(demander_informations_un_contribuable())
        continuer = input("Continuer ?")
    
    return contribuables         

def retourner_impot_a_partir_du_revenu(revenu):
    impot_a_payer = 0
    if revenu > 6800:
        impot_a_payer = revenu * 0.35
    
    return impot_a_payer

def afficher_informations_un_contribuable(contribuable):
    print contribuable["NN"]
    print contribuable["Prenom"]
    print contribuable["Nom"]
    print contribuable["Brut"]
    print contribuable["Prelevement"]
    print contribuable["Code postal"]
    print contribuable["Impot"]
    print contribuable["Balance"]

def calculer_impot_plusieurs_contribuables(liste_de_contribuables):
    for contribuable in liste_de_contribuables:
        impot_a_payer = retourner_impot_a_partir_du_revenu(contribuable["Brut"])
        contribuable["Impot"] = impot_a_payer

# Avant d'appeler cette fonction, il faut appeler la
# fonction calculer_impot_plusieurs_contribuables
def calculer_balance_plusieurs_contribuables(liste_de_contribuables):
    for contribuable in liste_de_contribuables:
        contribuable["Balance"] = contribuable["Prelevement"] - contribuable["Impot"]

def afficher_information_plusieurs_contribuables(liste_de_contribuables):
    for contribuable in liste_de_contribuables:
        afficher_informations_un_contribuable(contribuable)
        
contribuables = demander_informations_plusieurs_contribuables()
calculer_impot_plusieurs_contribuables(contribuables)
calculer_balance_plusieurs_contribuables(contribuables)
afficher_information_plusieurs_contribuables(contribuables)