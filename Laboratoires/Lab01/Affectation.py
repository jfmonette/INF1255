'''
Created on Jan 14, 2014

@author: moe
'''
import math

# Carre
dimensionCote = 10
perimetre = dimensionCote * 4
aire =  dimensionCote ** 2
print "Carre"
print "Dimension cote : ", dimensionCote
print "Perimetre : ", perimetre
print "Aire : ", aire
print

# Carre avec demande d'input
dimensionCote = input("Quelle est la dimension d'un cote du carre ?")
perimetre = dimensionCote * 4
aire =  dimensionCote ** 2
print "Carre"
print "Dimension cote : ", dimensionCote
print "Perimetre : ", perimetre
print "Aire : ", aire
print

# Rectangle
dimensionPetitCote = 10
dimensionGrandCote = 20
perimetre = (dimensionPetitCote + dimensionGrandCote)  * 2
aire =  dimensionPetitCote * dimensionGrandCote
print "Rectangle"
print "Dimension petit cote : ", dimensionPetitCote
print "Dimension grand cote : ", dimensionGrandCote
print "Perimetre : ", perimetre
print "Aire : ", aire
print 

# Boni : Triangle equilateral
dimensionCote = 10
perimetre = dimensionCote * 3
aire = (dimensionCote ** 2) * (math.sqrt(3) / 4)
print "Triangle equilateral"
print "Dimension cote : ", dimensionCote
print "Perimetre : ", perimetre
print "Aire : ", aire



