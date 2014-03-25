# -*- coding: UTF-8 -*-

class Etudiants:
    def __init__(self, un_chemin_de_fichier):
        self.chemin_du_fichier = un_chemin_de_fichier
        self.liste_etudiants = []
        self.construire_etudiants()

    def construire_etudiants(self):
        fichier = open(self.chemin_du_fichier, "r")
        for une_ligne in fichier:
            self.liste_etudiants.append(self.construire_un_etudiant(une_ligne))
        fichier.close()
    
    def construire_un_etudiant(self, une_ligne):
        etudiant = {} 
        valeurs = une_ligne.split(",")
        etudiant["Nom"] = valeurs[0]
        etudiant["Prénom"] = valeurs[1]
        etudiant["Code permanent"] = valeurs[2]
        return etudiant

etudiants = Etudiants("etudiants.txt")
print etudiants.liste_etudiants
