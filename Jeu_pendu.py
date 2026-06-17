import random  # permet de générer des choix aléatoires

mots_possibles = ["abeille", "cabaret", "capable", "changer", "chemine", "costume", "courage", "eclipse", "famille", "girafon", "horizon", "journal", "lumiere", "machine", "mystere", "oiseaux", "panneau", "silence", "banquet", "barrage", "branche", "contact", "lecture", "paysage", "planete", "poisson", "symbole", "travail", "village", "fenetre"]
lettres_essayees = []
vies = 7
mot_choisi = random.choice(mots_possibles)
mot_choisi = list(mot_choisi)
mot_devine = ["_"] * len(mot_choisi)

while vies > 0 and "_" in mot_devine:  # boucle principale du jeu
    print(f"\n Vies = {vies} \n ")
    print(" ".join(mot_devine) + "\n")
    print("Lettres essayées : " + ", ".join(lettres_essayees) + "\n")
    essai = input("Quelle lettre veux-tu essayer ? ").strip().lower()  # saisie de la lettre proposée par le joueur
    if len(essai) != 1:  # vérifie que l'utilisateur entre bien une seule lettre
        print("Erreur : le nombre de caractères attendus est mauvais \n")
    elif essai in lettres_essayees:  # vérifie si la lettre a déjà été proposée
        print("Lettre déjà essayée \n")
    elif essai in mot_choisi:  # vérifie si la lettre est présente dans le mot à deviner
        print(f"Bravo {essai} est bien dans le mot ! \n")
        for i, lettre in enumerate(mot_choisi):
            if lettre == essai:
                mot_devine[i] = essai
        lettres_essayees.append(essai)
    elif essai not in mot_choisi:  # cas où la lettre n'est pas dans le mot
        print(f"Dommage {essai} n'est pas dans le mot... \n")
        vies -= 1
        lettres_essayees.append(essai)
    else:
        print("Erreur : je ne comprends pas \n")

if vies == 0:
    print(f"Dommage, le mot était : {''.join(mot_choisi)}\n")
elif vies == 1:
    print(f"Bravo, le mot mystère était bien {''.join(mot_choisi)}. Il te restait {vies} vie restante \n")   
else:
    print(f"Bravo, le mot mystère était bien {''.join(mot_choisi)}. Il te restait {vies} vies restantes \n")
    
