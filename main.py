"""
un jeu de combat
projet fait par: Vincent Brouillet
groupe: 405
"""

import random as r


def new_monster(numero_adversaire, niveau_vie, numero_combat, nombre_victoires, nombre_defaites,
                nombre_victoires_consecutives, boss, room_adversaire):
    # pour mettre en théorie plusieur adversaire par étage
    if room_adversaire == 0:
        boss += 1
        print("vous avez fini un étage")
        room_adversaire = r.randint(1, 3)
    else:
        room_adversaire -= 1
    # pour mettre un boss a chaque 3 victoire
    if boss == 3:
        force_adversaire = r.randint(9, 11)
        print(f"Vous tombez face à face avec un boss de difficulté :{force_adversaire}")
    else:
        force_adversaire = r.randint(1, 9)
        print(f"Vous tombez face à face avec un adversaire de difficulté :{force_adversaire}")
    option(force_adversaire, numero_adversaire, niveau_vie, numero_combat, nombre_victoires, nombre_defaites,
           nombre_victoires_consecutives, boss, room_adversaire)


def option(force_adversaire, numero_adversaire, niveau_vie, numero_combat, nombre_victoires, nombre_defaites,
           nombre_victoires_consecutives, boss, room_adversaire):
    choix = int(input(
                  f"Que voulez-vous faire ? "
                  f"\n1- Combattre cet adversaire "
                  f"\n2- Contourner cet adversaire et aller ouvrir une autre porte"
                  f"\n3- Afficher les règles du jeu "
                  f"\n4- Quitter la partie"))
    if choix == 1:
        combattre(force_adversaire, numero_adversaire, niveau_vie, numero_combat, nombre_victoires, nombre_defaites,
                  nombre_victoires_consecutives, boss, room_adversaire)
    elif choix == 2:
        niveau_vie -= 1
        # si niveau de vie trop bas il meurt
        if niveau_vie < 1:
            print(f"La partie est terminée, vous avez vaincu {nombre_victoires} monstre(s).")
            rejouer = input("rejouer? y/n")
            if rejouer == "y":
                new_monster(0, 20, 0, 0, 0, 0, 0, 0)
            else:
                quit("Merci et au revoir...")
        else:
            print(f"Adversaire :{numero_adversaire} \nForce de l’adversaire :{force_adversaire} "
                  f"\nNiveau de vie de l’usager :{niveau_vie} \nCombat {numero_combat} : {nombre_victoires} vs",
                  {nombre_defaites})
            new_monster(numero_adversaire, niveau_vie, numero_combat, nombre_victoires,
                        nombre_defaites, nombre_victoires_consecutives, boss, room_adversaire)
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
               nombre_victoires_consecutives, boss, room_adversaire)
    else:
        quit("Merci et au revoir...")


def combattre(force_adversaire, numero_adversaire, niveau_vie, numero_combat, nombre_victoires, nombre_defaites,
              nombre_victoires_consecutives, boss, room_adversaire):
    numero_adversaire += 1
    numero_combat += 1
    score_de1 = r.randint(1, 6)
    score_de2 = r.randint(1, 6)
    print(f"Lancer des dé : {score_de1} {score_de2}")
    # defaite
    if score_de1 + score_de2 <= force_adversaire:
        niveau_vie -= force_adversaire
        nombre_defaites += 1
        combat_statut = "défaite"
        print(f"Dernier combat {combat_statut}")
        if niveau_vie < 1:
            print("XXXXXXXXXXXXXXXXXXXXXXXXX")
            print(f"La partie est terminée, vous avez vaincu {nombre_victoires} monstre(s).")
            y = input("rejouer? y/n")
            if y == "y":
                new_monster(0, 20, 0, 0, 0, 0, 0, r.randint(1, 3))
            else:
                quit("Merci et au revoir...")
        else:
            nombre_victoires_consecutives = 0
            new_monster(numero_adversaire, niveau_vie, numero_combat, nombre_victoires, nombre_defaites,
                        nombre_victoires_consecutives, boss, room_adversaire)

    # victoire
    else:
        niveau_vie += force_adversaire
        nombre_victoires += 1
        combat_statut = "victoire"
        print(f"Dernier combat {combat_statut}")
        nombre_victoires_consecutives += 1
        print(f"Niveau de vie: {niveau_vie} \nNombre de victoires consécutives: {nombre_victoires_consecutives}")
        new_monster(numero_adversaire, niveau_vie, numero_combat, nombre_victoires, nombre_defaites,
                    nombre_victoires_consecutives, boss, room_adversaire)
    print(f"Adversaire : {numero_adversaire} \nForce de l’adversaire : {force_adversaire}",
          f"\nNiveau de vie de l’usager : {niveau_vie} \nCombat {numero_combat} : {nombre_victoires} vs",
          f"{nombre_defaites}")


new_monster(0, 20, 0, 0, 0, 0, 0, r.randint(1, 3))
