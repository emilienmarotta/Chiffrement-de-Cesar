
### <<<  Chiffrement de César  >>> ###
# Version 1.0

""" Fonctions """

def input_texte_clair():
	texte_clair = str(input("\nTexte a chiffrer (seulement des caracteres sans accent) : ")).upper()
	return texte_clair

def input_texte_chiffre():
	texte_chiffre = str(input("\nTexte a dechiffrer : ")).upper()
	return texte_chiffre

def input_cle():
	cle = int(input("\nCle de chiffrement / dechiffrement (nombre) : "))
	return cle

def choix_mode():
	mode = ""
	while mode != "1" and mode != "2":
		mode = input("\nMode (saisissez le numero du mode) :\n1 - Chiffrer\n2 - Dechiffrer\n>>> ")	
	return mode

def fonction_chiffrement(lettre):
	if cle >= 0:
		lettre = 65 + ((lettre + cle - 91) % 26) # Revenir au début de l'alphabet si la clé est trop grande
	else: 
		lettre = 65 + ((lettre + cle - 65) % 26) # Revenir à la fin de l'alphabet si la clé est trop petite
	return lettre

def fonction_dechiffrement(lettre): 
	if cle >= 0:
		lettre = 65 + ((lettre - cle - 91) % 26) # Chemin inverse
	else:
		lettre = 65 + ((lettre - cle - 65) % 26) # Chemin inverse 
	return lettre

def conversion_chiffrement(lettre): 
	lettre_code_ascii = ord(lettre) # Conversion caractère -> code ASCII
	lettre_chiffree = fonction_chiffrement(lettre_code_ascii) # Chiffrement de la lettre
	lettre_caractere_chiffree = chr(lettre_chiffree) # Conversion code ASCII -> caractère
	return lettre_caractere_chiffree

def conversion_dechiffrement(lettre):
	lettre_code_ascii = ord(lettre) # Conversion caractère -> code ASCII
	lettre_dechiffree = fonction_dechiffrement(lettre_code_ascii) # Déchiffrement de la lettre
	lettre_caractere_dechiffree = chr(lettre_dechiffree) # Conversion code ASCII -> caractère
	return lettre_caractere_dechiffree

def algo_chiffrement(texte_clair):
	texte_chiffre = "" # Déclaration chaîne de caractères chiffrée
	for lettre in texte_clair: 
		if lettre != " ":
			lettre_chiffree = conversion_chiffrement(lettre)
			texte_chiffre += lettre_chiffree
		elif lettre == " ": 
			texte_chiffre += " "
	return texte_chiffre

def algo_dechiffrement(texte_chiffre):
	texte_dechiffre = "" # Déclaration chaîne de caractères déchiffrée
	for lettre in texte_chiffre: 
		if lettre != " ":
			lettre_dechiffree = conversion_dechiffrement(lettre)
			texte_dechiffre += lettre_dechiffree
		elif lettre == " ": 
			texte_dechiffre += " "
	return texte_dechiffre


### Déclaration de variables

texte_clair = "" 
texte_chiffre = ""
cle = 0
texte_dechiffre = ""

###


""" Instructions """

mode = choix_mode() # Choix du mode - Chiffrer (1) ou déchiffrer (2)

if mode == "1":
	texte_clair = input_texte_clair() # Saisie du texte à chiffrer
	cle = input_cle() # Saisie de la clé de chiffrement
	texte_chiffre = algo_chiffrement(texte_clair) # Récupération du texte chiffré dans une variable	
	print(texte_chiffre)
else:
	texte_chiffre = input_texte_chiffre() # Saisie du message à déchiffrer
	cle = input_cle() # Saisie de la clé de déchiffrement (doit être identique à la clé de chiffrement car chiffrement symétrique)
	texte_dechiffre = algo_dechiffrement(texte_chiffre) # Récupération du texte déchiffré dans une variable
	print(texte_dechiffre)


""" Fin du programme """

