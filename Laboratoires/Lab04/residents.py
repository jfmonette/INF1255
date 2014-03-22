residents= []
for i in range(2):
	residents.append({"prenom":raw_input("prenom"),
			  "nom":raw_input("nom")})
print residents

for resident in residents:
	print resident["prenom"]
	print resident["nom"]

'''
codes = ["H3A 3Z1","H2A 1L1", "H8T 3N1","H2A 5T1","H1B 8Q7"]

for resident in residents:
	code_postal = raw_input("Entrez un code postal")
	while True:
		if code_postal in codes:
			resident.update({"code postal":code_postal})
			break
		else:
			code_postal = raw_input("Entrez un code postal")

codeRecherche = raw_input("Code Postal")
for resident in residents:
	if resident["code postal"] == codeRecherche:
		print resident
'''
