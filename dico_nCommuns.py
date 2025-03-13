noms = {
    "masculin": [],
    "feminin": [],
    "pMasculin": [],
    "pFeminin": []
}

# Charger les données du fichier
with open("dico_nCommuns.txt", "r", encoding="utf-8") as fichier:
    for ligne in fichier:
        mots = ligne.strip().split(", ")
        if len(mots) == 4:
            noms["masculin"].append(mots[0])
            noms["feminin"].append(mots[1])
            noms["pMasculin"].append(mots[2])
            noms["pFeminin"].append(mots[3])