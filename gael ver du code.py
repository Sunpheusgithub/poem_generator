import random

def generateur_de_poeme(structure:str,syllabes:int,theme:str,rimes:list):
    #POEME FINAL EST UNE LISTE, QU'ON DEPLIERA A LA FIN, C'EST PLUS PRATIQUE
    poeme_final = []
    #ON TRAITE LA STRUCTURE, EN AJUSTANT LA TAILLE DU POEME AVEC UNE FONCTION AUXIALIAIRE
    taille = structure_traitement(structure)
    #ON FORME LE POEME, EN FONCTION DE LA TAILLE ET DU THEME, AINSI QUE DES SYLLABES ET DES RIMES
    for i in range(len(taille)):
        if taille[i] != 0:
            for j in range(taille[i]):
                #ON ECRIS LE VERS EN PRENANT EN COMPTE TT CE QU'IL FAUT PRENDRE EN COMPTE
                poeme_final.append(ecrire_le_vers(syllabes,theme,rimes))
        elif taille[i] == 0:
            poeme_final.append("")
    afficher_poeme(poeme_final)

def structure_traitement(structure:str) -> list:
    #LA TAILLE FINALE EST FORMée COMME CECI: SI ON A UN 4, ALORS C'EST UN QUATRAIN, ET SI IL Y A UN 0, C'EST QU'ON SAUTE UNE LIGNE
    taille_finale = []
    if structure == "sonnet":
        taille_finale = [4,0,4,0,3,0,3]
    elif structure == "rondeau":
        taille_finale = [3,0,3,0,3]
    elif structure == "haïku":
        taille_finale = [random.randint(2,3)]
    elif structure == "prose":
        taille_finale = [random.randint(1,5),random.randint(1,5),random.randint(1,5)]
    return taille_finale

def ecrire_le_vers(syllabes:str,theme:str,rimes:str) -> str:
    vers = ""
    sujet = ""
    verbe = ""
    determinant = ""
    nom = ""
    adjectif = ""
    sujet_liste = ["Je","Tu","Il","Elle","Nous","Vous","Ils","Elles","Elouan","Riwal","Ferdinand","Enzo","Gaël"]
    sujet_liste_prenom = ["Elouan","Riwal","Ferdinand","Enzo","Gaël"]
    verbe_liste = {"Je":["mange","parle","sens","touche","ressens","rêve","tape"],
                   "Tu":["manges","parles","sens","touches","ressens","rêves","tapes"],
                   "Il":["mange","parle","sens","touche","ressens","rêve","tape"],
                   "Elle":["mange","parle","sens","touche","ressens","rêve","tape"],
                   "On":["mange","parle","sens","touche","ressens","rêve","tape"],
                   "Nous":["mangeons","parlons","sentons","touchons","ressentons","rêvons","tapons"],
                   "Vous":["mangez","parlez","sentez","touchez","ressentez","rêvez","tapez"],
                   "Ils":["mangent","parlent","sentent","touchent","ressentent","rêvent","tapent"],
                   "Elles":["mangent","parlent","sentent","touchent","ressentent","rêvent","tapent"]}
    determinant_liste_singulier = ["le","la","me","ma","un","une"]
    determinant_liste_pluriel = ["des","tes","les","mes"]
    sujet_nature = {"singulier":{"1":["lion","lionne","fleur","feuille","vent","mer","roche","champs","pluie"],
                           "2":["amie","ami","soleil","nuage","banane","chemin","orage","bouleau","mangrove"],
                           "3":["papillon","arbuste","océanique","tournesol","écureui","chèvrefeuille","canopée"]},
              "pluriel":{"1":["lions","lionnes","fleurs","feuilles","vents","mers","roches","champs","pluies"],
                           "2":["amies","amis","soleils","nuages","bananes","chemins","orages","bouleaux","mangroves"],
                           "3":["papillons","arbustes","océaniques","tournesols","écureuils","chèvrefeuilles","canopées"]}}
    adjectif_nature = {"singulier":{"1":["vaste","riche","doux","frais","brut","sec"],
                           "2":["vivant","moullié","sauvage","paisible","joyeux","fleuri","brillant","humide"],
                           "3":["végétal","naturel","exotique","lumineux","magnifique","aromatique","écologique"]},
              "pluriel":{"1":["vastes","riches","doux","frais","bruts","secs"]},
                           "2":["vivants","moulliés","sauvages","paisibles","joyeux","fleuris","brillants","humides"],
                           "3":["végétals","naturels","exotiques","lumineux","magnifiques","aromatiques","écologiques"]}
    phrase = [sujet,verbe,determinant,nom,adjectif]
    #ON DECIDE EN ALEATOIRE LE SUJET
    sujet = random.choice(sujet_liste)
    #ON CREE UNE FONCTION QUI DIT QUE ELOUANN, RIWALL ET TT VALENT PAREIL QUE "Il"
    sujet_a_utiliser = prenom_vers_il(sujet,sujet_liste_prenom)
    vers = sujet
    #ON CHOISIT UN VERBE ALEATOIRE, EN LIEN AVEC LE SUJET
    verbe = random.choice(verbe_liste[sujet_a_utiliser])
    vers = vers+" "+verbe
    #ON CHOISIT SI LA SUITE VA ETRE AU SINGULIER OU AU PLURIEL
    sing_ou_plur = random.choice(["singulier","pluriel"])
    determinant = random.choice(determinant_liste_singulier)
    if sing_ou_plur == "pluriel":
        determinant = random.choice(determinant_liste_pluriel)
    vers = vers+" "+determinant
    #ON CHOISIT UN NOM ADAPTE AU DETERMINANT ET AU THEME
    nom = choisir_nom(theme,sing_ou_plur)
    vers = vers+" "+nom
    return vers

def prenom_vers_il(sujet:str,sujet_liste_prenom:list) -> str:
    sujet_retourne = sujet
    if sujet in sujet_liste_prenom:
        sujet_retourne = "Il"
    return sujet_retourne

def choisir_nom(theme:str,sing_ou_plur:str) -> str:
    nom = ""
    sujet_nature = {"singulier":{"1":["lion","lionne","fleur","feuille","vent","mer","roche","champs","pluie"],
                           "2":["amie","ami","soleil","nuage","banane","chemin","orage","bouleau","mangrove"],
                           "3":["papillon","arbuste","océanique","tournesol","écureuil","chèvrefeuille","canopée"]},
              "pluriel":{"1":["lions","lionnes","fleurs","feuilles","vents","mers","roches","champs","pluies"],
                           "2":["amies","amis","soleils","nuages","bananes","chemins","orages","bouleaux","mangroves"],
                           "3":["papillons","arbustes","océaniques","tournesols","écureuils","chèvrefeuilles","canopées"]}}
    if theme == "nature":
        nom = random.choice(sujet_nature["singulier"][random.choice(["1","2","3"])])
        if sing_ou_plur == "pluriel":
            nom = random.choice(sujet_nature["pluriel"][random.choice(["1","2","3"])])
    return nom

def afficher_poeme(poeme:list):
    #ON DEPLIE LA LISTE, EN AFFICHANT VERS PAR VERS DU POEME
    for i in range(len(poeme)):
        print(poeme[i])

generateur_de_poeme("sonnet",2,"nature",["A","B"])
