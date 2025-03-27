verbes_liste = {
    "Je": [],
    "Tu": [],
    "Il": [],
    "Elle": [],
    "On": [],
    "Nous": [],
    "Vous": [],
    "Ils": [],  # Partagé avec Elles
    "Elles": []  # Partagé avec Ils
}

# Charger les données du fichier
with open("dico_verbes.txt", "r", encoding="utf-8") as fichier:
    for ligne in fichier:
        mots = ligne.strip().split(", ")
        if len(mots) == 7:  # Vérifie que la ligne contient 7 colonnes
            verbes_liste["Je"].append(mots[1])  # 1ère personne du singulier
            verbes_liste["Tu"].append(mots[2])  # 2ème personne du singulier
            verbes_liste["Il"].append(mots[3])  # 3ème personne du singulier (masculin)
            verbes_liste["Elle"].append(mots[3])  # 3ème personne du singulier (féminin)
            verbes_liste["On"].append(mots[3])  # 3ème personne du singulier (neutre)
            verbes_liste["Nous"].append(mots[4])  # 1ère personne du pluriel
            verbes_liste["Vous"].append(mots[5])  # 2ème personne du pluriel
            verbes_liste["Ils"].append(mots[6])  # 3ème personne du pluriel (partagé)
            verbes_liste["Elles"].append(mots[6])  # 3ème personne du pluriel (partagé)

print(verbes_liste)

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
        if len(mots) == 4:  # Vérifie que la ligne contient 4 colonnes
            noms_liste["masculin"].append(mots[0])
            noms_liste["feminin"].append(mots[1])
            noms_liste["pMasculin"].append(mots[2])
            noms_liste["pFeminin"].append(mots[3])