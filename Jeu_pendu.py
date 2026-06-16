from operator import indexOf
import random

mots_possibles = ["chocolat", "montagne", "ordinateur", "girafe", "aventure", "fantome", "volcan", "pirate", "bibliotheque", "arcenciel", "dragon", "horloge", "foret", "fusee", "mystere"]
lettres_essayees = []
vies = 7
mot_choisi = mots_possibles[random.randint(0, len(mots_possibles) - 1)]
mot_choisi_supp = list(mot_choisi)
mot_choisi = list(mot_choisi)
print(mot_choisi)
mot_devine = []
for letter in mot_choisi:
    mot_devine.append("_")

while vies > 0 and mot_choisi != mot_devine:
    print(f"\n Vies = {vies} \n ")
    print(f" {mot_devine} \n") #"" à enlever
    print(f"Lettres essayées = {lettres_essayees} \n")
    essai = input("Quelle lettre veux-tu essayer ? \n").strip().lower()
    if len(essai) != 1:
        print("Erreur : nombre de caractères attendus est mauvais \n")
    elif essai in lettres_essayees:
        print("Lettre déjà essayée \n")
    elif essai in mot_choisi:
        print(f"Bravo {essai} est bien dans le mot ! \n")
        for lettre in mot_choisi_supp: # plusieurs occurences à régler
            if lettre == essai:
                mot_devine[indexOf(mot_choisi_supp, lettre)] = essai ###### ici probleme occurence
                mot_choisi_supp[indexOf(mot_choisi_supp, lettre)] = "."
                print(mot_choisi)
        lettres_essayees.append(essai)
    elif essai not in mot_choisi:
        print(f"Dommage {essai} n'est pas dans le mot... \n")
        vies -= 1
        lettres_essayees.append(essai)
    else:
        print("Erreur : je ne comprends pas \n")

if vies == 0:
    print("Dommage, vous aurez plus de chance la prochaine fois... \n")
elif vies == 1:
    print(f"Bravo tu as trouvé le mot mystère avec {vies} vie restante \n")
else:
    print(f"Bravo tu as trouvé le mot mystère avec {vies} vies restantes \n")