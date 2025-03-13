noms = {
    "masculin": [],
    "féminin": [],
    "pMasculin": [],
    "pFéminin": []
}

# Charger les données du fichier
with open("dico_nCommuns.txt", "r", encoding="utf-8") as fichier:
    for ligne in fichier:
        mots = ligne.strip().split(", ")
        if len(mots) == 4:
            noms["masculin"].append(mots[0])
            noms["féminin"].append(mots[1])
            noms["pMasculin"].append(mots[2])
            noms["pFéminin"].append(mots[3])

# Afficher la liste des noms par genre et nombre
for genre, liste_noms in noms.items():
    print(f"{genre}: {liste_noms}")
