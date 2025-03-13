import random
from typing import List

def generateur_de_poeme(structure: str, syllabes: int, theme: str, rimes: List[str]) -> None:
    """
    Génère un poème en fonction de la structure, du nombre de syllabes, du thème et des rimes.
    """
    # POÈME FINAL EST UNE LISTE, QU'ON DÉPLIERA À LA FIN, C'EST PLUS PRATIQUE
    poeme_final = []
    # ON TRAITE LA STRUCTURE, EN AJUSTANT LA TAILLE DU POÈME AVEC UNE FONCTION AUXILIAIRE
    taille = structure_traitement(structure)
    # ON FORME LE POÈME, EN FONCTION DE LA TAILLE ET DU THÈME, AINSI QUE DES SYLLABES ET DES RIMES
    for i in range(len(taille)):
        if taille[i] != 0:
            for j in range(taille[i]):
                # ON ÉCRIT LE VERS EN PRENANT EN COMPTE TOUT CE QU'IL FAUT PRENDRE EN COMPTE
                poeme_final.append(ecrire_le_vers(syllabes, theme, rimes))
        elif taille[i] == 0:
            poeme_final.append("")
    afficher_poeme(poeme_final)

def structure_traitement(structure: str) -> List[int]:
    """
    Traite la structure du poème et retourne une liste représentant la taille de chaque strophe.
    """
    # LA TAILLE FINALE EST FORMÉE COMME CECI: SI ON A UN 4, ALORS C'EST UN QUATRAIN, ET SI IL Y A UN 0, C'EST QU'ON SAUTE UNE LIGNE
    taille_finale = []
    if structure == "sonnet":
        taille_finale = [4, 0, 4, 0, 3, 0, 3]
    elif structure == "rondeau":
        taille_finale = [3, 0, 3, 0, 3]
    elif structure == "haïku":
        taille_finale = [random.randint(2, 3)]
    elif structure == "prose":
        taille_finale = [random.randint(1, 5), random.randint(1, 5), random.randint(1, 5)]
    return taille_finale

def ecrire_le_vers(syllabes: int, theme: str, rimes: List[str]) -> str:
    """
    Écrit un vers en fonction du nombre de syllabes, du thème et des rimes.
    """
    sujet_liste = ["Je", "Tu", "Il", "Elle", "Nous", "Vous", "Ils", "Elles", "Elouan", "Riwal", "Ferdinand", "Enzo", "Gaël"]
    sujet_liste_prenom = ["Elouan", "Riwal", "Ferdinand", "Enzo", "Gaël"]
    verbe_liste = {
        "Je": ["mange", "parle", "sens", "touche", "ressens", "rêve", "tape"],
        "Tu": ["manges", "parles", "sens", "touches", "ressens", "rêves", "tapes"],
        "Il": ["mange", "parle", "sens", "touche", "ressens", "rêve", "tape"],
        "Elle": ["mange", "parle", "sens", "touche", "ressens", "rêve", "tape"],
        "On": ["mange", "parle", "sens", "touche", "ressens", "rêve", "tape"],
        "Nous": ["mangeons", "parlons", "sentons", "touchons", "ressentons", "rêvons", "tapons"],
        "Vous": ["mangez", "parlez", "sentez", "touchez", "ressentez", "rêvez", "tapez"],
        "Ils": ["mangent", "parlent", "sentent", "touchent", "ressentent", "rêvent", "tapent"],
        "Elles": ["mangent", "parlent", "sentent", "touchent", "ressentent", "rêvent", "tapent"]
    }
    determinant_liste_singulier_masculin = ["le", "un"]
    determinant_liste_singulier_feminin = ["la", "une"]
    determinant_liste_pluriel = ["des", "tes", "les", "mes"]

    # Choisir un sujet aléatoire
    sujet = random.choice(sujet_liste)
    sujet_a_utiliser = prenom_vers_il(sujet, sujet_liste_prenom)

    # Choisir un verbe aléatoire en lien avec le sujet
    verbe = random.choice(verbe_liste[sujet_a_utiliser])

    # Déterminer si la suite sera au singulier ou au pluriel, et féminin ou masculin
    sing_ou_plur = random.choice(["singulier", "pluriel"])
    femin_ou_masc = random.choice(["masculin", "feminin"])

    # Choisir un déterminant approprié
    determinant = random.choice(determinant_liste_singulier_masculin)
    if femin_ou_masc == "feminin":
        determinant = random.choice(determinant_liste_singulier_feminin)
    if sing_ou_plur == "pluriel":
        determinant = random.choice(determinant_liste_pluriel)

    # Choisir un nom adapté au déterminant et au thème
    nom = choisir_nom(theme, sing_ou_plur, femin_ou_masc)

    # Remplacer le déterminant par "l'" si le nom commence par une voyelle
    if nom[0] in ["a", "e", "y", "u", "i", "o"] and determinant in ["la", "le"]:
        determinant = "l'"

    # Construire le vers avec des espaces entre les mots
    vers = f"{sujet} {verbe} {determinant} {nom}"
    return vers

def prenom_vers_il(sujet: str, sujet_liste_prenom: List[str]) -> str:
    """
    Remplace un prénom par "Il" si le sujet est un prénom.
    """
    return "Il" if sujet in sujet_liste_prenom else sujet

def choisir_nom(theme: str, sing_ou_plur: str, femin_ou_masc: str) -> str:
    """
    Choisit un nom en fonction du thème, du nombre et du genre.
    """
    sujet_nature = {
        "singulier": {
            "1": {"masculin": ["lion", "vent", "champs"], "feminin": ["lionne", "fleur", "feuille", "mer", "roche", "champs", "pluie"]},
            "2": {"masculin": ["ami", "soleil", "nuage", "chemin", "orage", "bouleau"], "feminin": ["amie", "banane", "mangrove"]},
            "3": {"masculin": ["papillon", "arbuste", "abyssal", "tournesol", "écureuil", "chèvrefeuille"], "feminin": ["canopée", "léoparde"]}
        },
        "pluriel": {
            "1": ["lions", "lionnes", "fleurs", "feuilles", "vents", "mers", "roches", "champs", "pluies"],
            "2": ["amies", "amis", "soleils", "nuages", "bananes", "chemins", "orages", "bouleaux", "mangroves"],
            "3": ["papillons", "arbustes", "océaniques", "tournesols", "écureuils", "chèvrefeuilles", "canopées"]
        }
    }
    if theme == "nature":
        if sing_ou_plur == "pluriel":
            return random.choice(sujet_nature["pluriel"][random.choice(["1", "2", "3"])])
        else:
            return random.choice(sujet_nature["singulier"][random.choice(["1", "2", "3"])][femin_ou_masc])
    return ""

def afficher_poeme(poeme: List[str]) -> None:
    """
    Affiche le poème vers par vers.
    """
    for vers in poeme:
        print(vers)

# Exemple d'utilisation
generateur_de_poeme("sonnet", 2, "nature", ["A", "B"])
