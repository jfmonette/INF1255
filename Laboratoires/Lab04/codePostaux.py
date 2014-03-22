codes = ["H3A 3Z1","H2A 1L1", "H8T 3N1","H2A 5T1","H1B 8Q7"]
print "Codes valides:", codes

codeSaisi = raw_input("ENtrez un code postal : ")

while codeSaisi not in codes:
	codeSaisi = raw_input("ENtrez un code postal : ")

print codeSaisi
