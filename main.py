"""
projet fait par: Vincent Brouillet
groupe: 405
un jeu de combat
"""

import random as r


def new_monster(numero_adversaire, niveau_vie, numero_combat, nombre_victoires, nombre_defaites,
                nombre_victoires_consecutives):

    numero_adversaire += 1
    force_adversaire = r.randint(1, 5)
    print(f"Vous tombez face à face avec un adversaire de difficulté :{force_adversaire}")
    option(force_adversaire, numero_adversaire, niveau_vie, numero_combat, nombre_victoires, nombre_defaites,
           nombre_victoires_consecutives)


def option(force_adversaire, numero_adversaire, niveau_vie, numero_combat, nombre_victoires, nombre_defaites,
           nombre_victoires_consecutives):
    choix = int(input(
                  "Que voulez-vous faire ? "
                  "\n1- Combattre cet adversaire "
                  "\n2- Contourner cet adversaire et aller ouvrir une autre porte"
                  " \n3- Afficher les règles du jeu "
                  "\n4- Quitter la partie"))
    if choix == 1:
        combattre(force_adversaire, numero_adversaire, niveau_vie, numero_combat, nombre_victoires, nombre_defaites,
                  nombre_victoires_consecutives)
    elif choix == 2:
        niveau_vie -= 1
        # si niveau de vie trop bas il meurt
        if niveau_vie < 1:
            print(f"La partie est terminée, vous avez vaincu {nombre_victoires} monstre(s).")
            rejouer = input("rejouer? y/n")
            if rejouer == "y":
                new_monster(0, 20, 0, 0, 0, 0)
            else:
                quit("Merci et au revoir...")
        else:
            print(f"Adversaire :{numero_adversaire} \nForce de l’adversaire :{force_adversaire} "
                  f"\nNiveau de vie de l’usager :{niveau_vie} \nCombat {numero_combat} : {nombre_victoires} vs",
                  {nombre_defaites})
            new_monster(numero_adversaire, niveau_vie, numero_combat, nombre_victoires,
                        nombre_defaites, nombre_victoires_consecutives)
    elif choix == 3:
        print(f"\nPour réussir un combat, il faut que la valeur du dé lancé soit "
              f"\nsupérieure à la force de l’adversaire.  Dans ce cas, le niveau "
              f"\nde vie de l’usager est augmenté de la force de l’adversaire. "
              f"\nUne défaite a lieu lorsque la valeur du dé lancé par l’usager "
              f"\nest inférieure ou égale à la force de l’adversaire.  Dans ce "
              f"\ncas, le niveau de vie de l’usager est diminué de "
              f"\nla force de l’adversaire. "
              f"\n \nLa partie se termine lorsque les points de vie de l’usager "
              f"\ntombent sous 0. "
              f"\n \nL’usager peut combattre ou éviter chaque adversaire, dans le "
              f"\ncas de l’évitement, il y a une pénalité de 1 point de vie. \n")
        option(force_adversaire, numero_adversaire, niveau_vie, numero_combat, nombre_victoires, nombre_defaites,
               nombre_victoires_consecutives)
    else:
        quit("Merci et au revoir...")


def combattre(force_adversaire, numero_adversaire, niveau_vie, numero_combat, nombre_victoires, nombre_defaites,
              nombre_victoires_consecutives):
    numero_combat += 1
    score_de = r.randint(1, 6)
    print(f"Lancer du dé : {score_de}")
    # defaite
    if score_de <= force_adversaire:
        niveau_vie -= force_adversaire
        nombre_defaites += 1
        combat_statut = "défaite"
        print(f"Dernier combat {combat_statut}")
        if niveau_vie < 1:
            print(f"La partie est terminée, vous avez vaincu {nombre_victoires} monstre(s).")
            y = input("rejouer? y/n")
            if y == "y":
                new_monster(0, 20, 0, 0, 0, 0)
            else:
                quit("Merci et au revoir...")
    # victoire
    else:
        niveau_vie += force_adversaire
        nombre_victoires += 1
        combat_statut = "victoire"
        print(f"Dernier combat {combat_statut}")
        nombre_victoires_consecutives += 1
        print(f"Niveau de vie: {niveau_vie} \nNombre de victoires consécutives: {nombre_victoires_consecutives}")
        new_monster(numero_adversaire, niveau_vie, numero_combat, nombre_victoires, nombre_defaites,
                    nombre_victoires_consecutives)
    print(f"Adversaire : {numero_adversaire} \nForce de l’adversaire : {force_adversaire}",
          f"\nNiveau de vie de l’usager : {niveau_vie} \nCombat {numero_combat} : {nombre_victoires} vs",
          f"{nombre_defaites}")
    new_monster(numero_adversaire, niveau_vie, numero_combat, nombre_victoires, nombre_defaites,
                nombre_victoires_consecutives)


new_monster(0, 20, 0, 0, 0, 0)
