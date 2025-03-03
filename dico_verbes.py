verbes = []
# Charger les données du fichier
fichier = open("./Verbes.txt", "r", encoding="utf-8")
for ligne in fichier:
    mots = ligne.strip().split(", ")
    if len(mots) == 4:
        verbe_dict = {
            "infinitif": mots[0],
            "present1": mots[1],
            "present2": mots[2],
            "present3": mots[3]
        }
        verbes.append(verbe_dict)
# Afficher la liste des dictionnaires
for verbe in verbes:
    print(verbe)