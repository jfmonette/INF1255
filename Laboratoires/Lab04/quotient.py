dividende = raw_input("Entrez le dividende :")
diviseur = raw_input("Entrez le diviseur :")

while True:
	try:
		dividende = float(dividende)
		diviseur = float(diviseur)
		print dividende // diviseur
		break
	except:
		print "Il y a eu une erreur"
		dividende = raw_input("Entrez le dividende :")
		diviseur = raw_input("Entrez le diviseur :")

