import random
from typing import List
from dico_gen import verbes_liste
from dico_gen import noms_liste

def generateur_de_poeme(structure: str, syllabes: int, theme: str, rimes: List[str]) -> None:
    """
    Génère un poème en fonction de la structure, du nombre de syllabes, du thème et des rimes.
    """
    # Poème final est une liste, qu'on affichera à la fin
    poeme_final = []
    # On traite la structure, en ajustant la taille du poème avec une fonction auxiliaire
    taille = structure_traitement(structure)
    # On forme le poème, en fonction de la taille et du thème, ainsi que des syllabes et des rimes
    for i in range(len(taille)):
        if taille[i] != 0:
            for j in range(taille[i]):
                # On écrit le vers en prenant en compte tout ce qu'il faut prendre en compte
                vers = ecrire_le_vers(syllabes, theme, rimes)
                print(count_syllables(vers),vers)
                while count_syllables(vers) != syllabes:  # Assurer que le vers correspond au nombre de syllabes
                    vers = ecrire_le_vers(syllabes, theme, rimes)
                poeme_final.append(vers)
        else:
            poeme_final.append("")  # Ligne vide pour la séparation des strophes
    afficher_poeme(poeme_final)

def structure_traitement(structure: str) -> List[int]:
    """
    Traite la structure du poème et retourne une liste représentant la taille de chaque strophe.
    """
    # La taille finale est formée comme ceci: si on a un 4, alors c'est un quatrain, et si il y a un 0, c'est qu'on saute une ligne
    taille_finale = []
    if structure == "sonnet":
        taille_finale = [4, 0, 4, 0, 3, 0, 3]
    elif structure == "rondeau":
        taille_finale = [3, 0, 3, 0, 3]
    elif structure == "haïku":
        taille_finale = [3, 5, 3]  # Structure traditionnelle du haïku
    elif structure == "prose":
        taille_finale = [random.randint(1, 5) for i in range(3)]  # Nombre aléatoire de lignes
    return taille_finale

def ecrire_le_vers(syllabes: int, theme: str, rimes: List[str]) -> str:
    """
    Écrit un vers en fonction du nombre de syllabes, du thème et des rimes.
    """
    sujet_liste = ["Je", "Tu", "Il", "Elle", "Nous", "Vous", "Ils", "Elles", "Elouan", "Riwal", "Ferdinand", "Enzo", "Gaël"]
    sujet_liste_prenom = ["Elouan", "Riwal", "Ferdinand", "Enzo", "Gaël"]

    # Choisir un sujet aléatoire
    sujet = random.choice(sujet_liste)
    sujet_a_utiliser = prenom_vers_il(sujet, sujet_liste_prenom)

    # Choisir un verbe aléatoire en lien avec le sujet
    verbe = random.choice(verbes_liste[sujet_a_utiliser])

    # Déterminer si la suite sera au singulier ou au pluriel, et féminin ou masculin
    sing_ou_plur = random.choice(["singulier", "pluriel"])
    femin_ou_masc = random.choice(["masculin", "feminin"])

    # Choisir un déterminant approprié
    determinant = choisir_determinant(sing_ou_plur, femin_ou_masc)

    # Choisir un nom adapté au déterminant et au thème
    nom = choisir_nom(theme, sing_ou_plur, femin_ou_masc)

    # Remplacer le déterminant par "l'" si le nom commence par une voyelle
    if nom[0] in ["a", "e", "y", "u", "i", "o"]:
        determinant = "l'"

    # Construire le vers avec des espaces entre les mots
    vers = f"{sujet} {verbe} {determinant} {nom}"
    return vers

def choisir_determinant(sing_ou_plur: str, femin_ou_masc: str) -> str:
    """
    Choisit un déterminant en fonction du nombre et du genre.
    """
    if sing_ou_plur == "pluriel":
        return random.choice(["des", "tes", "les", "mes"])
    elif femin_ou_masc == "masculin":
        return random.choice(["le", "un"])
    else:
        return random.choice(["la", "une"])

def prenom_vers_il(sujet: str, sujet_liste_prenom: List[str]) -> str:
    """
    Remplace un prénom par "Il" si le sujet est un prénom.
    """
    return "Il" if sujet in sujet_liste_prenom else sujet

def choisir_nom(theme: str, sing_ou_plur: str, femin_ou_masc: str) -> str:
    """
    Choisit un nom en fonction du thème, du nombre et du genre.
    """
    if theme == "nature":
        if sing_ou_plur == "pluriel":
            key = f"p{femin_ou_masc.capitalize()}"
            if key in noms_liste:
                return random.choice(noms_liste[key])
            else:
                raise KeyError(f"Clé '{key}' non trouvée dans le dictionnaire des noms.")
        else:
            key = femin_ou_masc
            if key in noms_liste:
                return random.choice(noms_liste[key])
            else:
                raise KeyError(f"Clé '{key}' non trouvée dans le dictionnaire des noms.")
    return ""

def count_syllables(vers: str) -> int:
    """
    Compte le nombre de syllabes dans un vers. 
    """
    voyelles = "AEIOUYaeiouy"
    if vers[0] in voyelles :
        count = 1
    else : 
        count = 0
    for i in range(len(vers)-1) :
        if vers[i] in voyelles and vers[i+1] not in voyelles:  #ne pas compter les doublons de voyelles
            if vers[i+1] == " " or i == len(vers)-2 :
                if vers[i] not in "eE" :
                    count += 1
                elif f'{vers[i-1]}{vers[i]}' not in ["ES","es"]:
                    count += 1
                elif f'{vers[i-1]}{vers[i]}' in ["LE","Le","le"] or f'{vers[i-2]}{vers[i-1]}{vers[i]}' not in ["LES","Les","les"]:
                    count += 1
            else :
                count += 1
    return count

def afficher_poeme(poeme: List[str]) -> None:
    """
    Affiche le poème vers par vers.
    """
    for vers in poeme:
        print(vers)

# Exemples d'utilisation
print("Exemple 1 : Sonnet")
generateur_de_poeme("sonnet", 8, "nature", ["A", "B"])

print("\nExemple 2 : Rondeau")
generateur_de_poeme("rondeau", 6, "nature", ["A", "B"])

print("\nExemple 3 : Haïku")
generateur_de_poeme("haïku", 5, "nature", ["A", "B"])

print("\nExemple 4 : Prose")
generateur_de_poeme("prose", 7, "nature", ["A", "B"])