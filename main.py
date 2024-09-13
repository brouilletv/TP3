import random as r

def new_monster(force_adversaire, numero_adversaire, niveau_vie, numero_combat, nombre_victoires, nombre_defaites, nombre_victoires_consecutives):
    numero_adversaire += 1
    force_adversaire = r.randint(1,5)
    print("Vous tombez face à face avec un adversaire de difficulté :", force_adversaire)
    option(force_adversaire, numero_adversaire, niveau_vie, numero_combat, nombre_victoires, nombre_defaites, nombre_victoires_consecutives)

def option(force_adversaire, numero_adversaire, niveau_vie, numero_combat, nombre_victoires, nombre_defaites, nombre_victoires_consecutives):
    x = int(input("Que voulez-vous faire ? \n1- Combattre cet adversaire \n2- Contourner cet adversaire et aller ouvrir une autre porte \n3- Afficher les règles du jeu \n4- Quitter la partie"))
    if x == 1:
        combattre(force_adversaire, numero_adversaire, niveau_vie, numero_combat, nombre_victoires, nombre_defaites, nombre_victoires_consecutives)
    elif x == 2:
        niveau_vie -= 1
        if niveau_vie < 1:
            print("La partie est terminée, vous avez vaincu", nombre_victoires, "monstre(s).")
            y = input("rejouer? y/n")
            if y == "y":
                new_monster(0, 0, 20, 0, 0, 0, 0)
            else:
                quit("Merci et au revoir...")
        else:
            new_monster(force_adversaire, numero_adversaire, niveau_vie, numero_combat, nombre_victoires, nombre_defaites, nombre_victoires_consecutives)
    elif x == 3:
        print("\nPour réussir un combat, il faut que la valeur du dé lancé soit \nsupérieure à la force de l’adversaire.  Dans ce cas, le niveau \nde vie de l’usager est augmenté de la force de l’adversaire. \nUne défaite a lieu lorsque la valeur du dé lancé par l’usager \nest inférieure ou égale à la force de l’adversaire.  Dans ce \ncas, le niveau de vie de l’usager est diminué de \nla force de l’adversaire. \n \nLa partie se termine lorsque les points de vie de l’usager \ntombent sous 0. \n \nL’usager peut combattre ou éviter chaque adversaire, dans le \ncas de l’évitement, il y a une pénalité de 1 point de vie. \n")
        option(force_adversaire, numero_adversaire, niveau_vie, numero_combat, nombre_victoires, nombre_defaites, nombre_victoires_consecutives)
    else:
        quit("Merci et au revoir...")

def combattre(force_adversaire, numero_adversaire, niveau_vie, numero_combat, nombre_victoires, nombre_defaites, nombre_victoires_consecutives):
    numero_combat += 1
    score_dé = r.randint(1,6)
    print("Lancer du dé :", score_dé)
    if score_dé <= force_adversaire:
        niveau_vie -= force_adversaire
        nombre_defaites += 1
        combat_statut = "défaite"
        print("Dernier combat", combat_statut)
        if niveau_vie < 1:
            print("La partie est terminée, vous avez vaincu", nombre_victoires,"monstre(s).")
            y = input("rejouer? y/n")
            if y == "y":
                new_monster(0,0,20,0,0,0,0)
            else:
                quit("Merci et au revoir...")
    else:
        niveau_vie += force_adversaire
        nombre_victoires += 1
        combat_statut = "victoire"
        print("Dernier combat", combat_statut)
        nombre_victoires_consecutives += 1
        print("Niveau de vie:", niveau_vie,"\nNombre de victoires consécutives:", nombre_victoires_consecutives)
        new_monster(force_adversaire, numero_adversaire, niveau_vie, numero_combat, nombre_victoires, nombre_defaites, nombre_victoires_consecutives)
    print("Adversaire :", numero_adversaire, "\nForce de l’adversaire :", force_adversaire,"\nNiveau de vie de l’usager :", niveau_vie, "\nCombat", numero_combat, ":", nombre_victoires, "vs",nombre_defaites)
    x = input("")
    combattre(force_adversaire, numero_adversaire, niveau_vie, numero_combat, nombre_victoires, nombre_defaites, nombre_victoires_consecutives)

new_monster(0,0,20,0,0,0,0)