verbes_liste = {
    "Je": [],
    "Tu": [],
    "Il": [],
    "Elle": [],
    "On": [],
    "Nous": [],
    "Vous": [],
    "Ils": [],
    "Elles": []
}

# Charger les données du fichier
with open("dico_verbes.txt", "r", encoding="utf-8") as fichier:
    for ligne in fichier:
        mots = ligne.strip().split(", ")
        if len(mots) == 4:
            verbes_liste["Je"].append(mots[1])
            verbes_liste["Tu"].append(mots[2])
            verbes_liste["Il"].append(mots[3])
            verbes_liste["Elle"].append(mots[3])
            verbes_liste["On"].append(mots[3])
            verbes_liste["Nous"].append(mots[1] + "ons")
            verbes_liste["Vous"].append(mots[1] + "ez")
            verbes_liste["Ils"].append(mots[3] + "ent")
            verbes_liste["Elles"].append(mots[3] + "ent")

noms_liste = {
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
            noms_liste["masculin"].append(mots[0])
            noms_liste["feminin"].append(mots[1])
            noms_liste["pMasculin"].append(mots[2])
            noms_liste["pFeminin"].append(mots[3])