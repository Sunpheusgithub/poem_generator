verbe_liste = {
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
            verbe_liste["Je"].append(mots[1])
            verbe_liste["Tu"].append(mots[2])
            verbe_liste["Il"].append(mots[3])
            verbe_liste["Elle"].append(mots[3])
            verbe_liste["On"].append(mots[3])
            verbe_liste["Nous"].append(mots[1] + "ons")
            verbe_liste["Vous"].append(mots[1] + "ez")
            verbe_liste["Ils"].append(mots[3] + "ent")
            verbe_liste["Elles"].append(mots[3] + "ent")

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