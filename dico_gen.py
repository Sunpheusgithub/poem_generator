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

with open("dico_verbes.txt", "r", encoding="utf-8") as fichier:
    for ligne in fichier:
        mots = ligne.strip().split(", ")
        if len(mots) == 7:
            verbes_liste["Je"].append(mots[1]) 
            verbes_liste["Tu"].append(mots[2])  
            verbes_liste["Il"].append(mots[3])  
            verbes_liste["Elle"].append(mots[3])  
            verbes_liste["On"].append(mots[3])  
            verbes_liste["Nous"].append(mots[4])  
            verbes_liste["Vous"].append(mots[5]) 
            verbes_liste["Ils"].append(mots[6])  
            verbes_liste["Elles"].append(mots[6])  

print(verbes_liste)

noms_liste = {
    "masculin": [],
    "feminin": [],
    "pMasculin": [],
    "pFeminin": [],
    "phonetique_masculin": [],
    "phonetique_feminin": [],
    "phonetique_pMasculin": [],
    "phonetique_pFeminin": [],
    "theme": []
}

liste_themes = ["nature","amour","vie","sentiments","emotions","beauté","musique","animaux","art"] # ajouter des themes / ajuster

with open("dico_nCommuns.txt", "r", encoding="utf-8") as fichier:
    for ligne in fichier:
        mots = ligne.strip().split(", ")
        if len(mots) == 8:  
            noms_liste["masculin"].append(mots[0])
            noms_liste["feminin"].append(mots[1])
            noms_liste["pMasculin"].append(mots[2])
            noms_liste["pFeminin"].append(mots[3])
            noms_liste["phonetique_masculin"].append(mots[4])
            noms_liste["phonetique_feminin"].append(mots[5])
            noms_liste["phonetique_pMasculin"].append(mots[6])
            noms_liste["phonetique_pFeminin"].append(mots[7])
            #noms_liste["theme"].append(mots[8])
            #if mots[8] not in liste_themes:
            #   liste_themes.append(mots[8])

            # TODO ajouter themes dans dico_nCommuns.txt

print(noms_liste)