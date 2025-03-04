noms = [
    {"masculin": "ami", "féminin": "amie", "pluriel_m": "amis", "pluriel_f": "amies"},
    {"masculin": "chat", "féminin": "chatte", "pluriel_m": "chats", "pluriel_f": "chattes"},
    {"masculin": "chien", "féminin": "chienne", "pluriel_m": "chiens", "pluriel_f": "chiennes"},
    {"masculin": "acteur", "féminin": "actrice", "pluriel_m": "acteurs", "pluriel_f": "actrices"},
    {"masculin": "danseur", "féminin": "danseuse", "pluriel_m": "danseurs", "pluriel_f": "danseuses"},
    {"masculin": "lion", "féminin": "lionne", "pluriel_m": "lions", "pluriel_f": "lionnes"},
    {"masculin": "docteur", "féminin": "docteure", "pluriel_m": "docteurs", "pluriel_f": "docteures"},
    {"masculin": "maître", "féminin": "maîtresse", "pluriel_m": "maîtres", "pluriel_f": "maîtresses"},
    {"masculin": "roi", "féminin": "reine", "pluriel_m": "rois", "pluriel_f": "reines"},
    {"masculin": "vendeur", "féminin": "vendeuse", "pluriel_m": "vendeurs", "pluriel_f": "vendeuses"},
]

# Exemple d'affichage
for nom in noms:
    print(f"{nom['masculin']} / {nom['féminin']} / {nom['pluriel_m']} / {nom['pluriel_f']}")
