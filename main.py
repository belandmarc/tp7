import random


def jeu_devine_nombre():
    argent = 100
    continuer = True

    print("Bienvenue dans le jeu de devinette !")
    print("Tu commences avec 100$. Devine un nombre entre 1 et 50.")
    print("Tu perds 10$ à chaque mauvaise réponse.")
    print("Si tu trouves la bonne réponse, tu gagnes 50$.")
    print("Si tu trouves en 3 essais ou moins, tu gagnes 200$ !")
    print("Tu auras un indice à chaque tentative.\n")

    while continuer and argent > 0:
        nombre_a_deviner = random.randint(1, 50)
        essais = 0
        trouve = False

        while argent > 0 and not trouve:
            try:
                guess = int(input("Entre un nombre entre 1 et 50 : "))
            except ValueError:
                print("Entre un nombre valide.")
                continue

            essais += 1
            if guess == nombre_a_deviner:
                if essais <= 3:
                    print(f"Bravo ! Tu as deviné en {essais} essai(s) ! Tu gagnes 200$.")
                    argent += 200
                else:
                    print(f"Bonne réponse ! Tu gagnes 50$.")
                    argent += 50
                trouve = True
            else:
                argent -= 10
                if argent <= 0:
                    print("Mauvaise réponse. Tu n’as plus d’argent.")
                    break
                if guess < nombre_a_deviner:
                    print(f"Plus GRAND ! Il te reste {argent}$.")
                else:
                    print(f"Plus PETIT ! Il te reste {argent}$.")

        print(f"Ton solde est maintenant de {argent}$.\n")
        if argent <= 0:
            print("Jeu terminé. Tu n’as plus d’argent.")
            break

        choix = input("Veux-tu rejouer ? (o/n) : ").lower()
        if choix != 'o':
            continuer = False
            print("Merci d’avoir joué !")


jeu_devine_nombre()
