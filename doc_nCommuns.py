noms = []
# Charger les données du fichier
fichier = open("dico_nCommuns.txt", "r", encoding="utf-8")
for ligne in fichier:
    mots = ligne.strip().split(", ")
    if len(mots) == 4:
        nom_dict = {
            "masculin": mots[0],
            "féminin": mots[1],
            "pMasculin": mots[2],
            "pFéminin": mots[3]
        }
        noms.append(nom_dict)
# Afficher la liste des dictionnaires
for nom in noms:
    print(nom)
