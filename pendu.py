import random
import unicodedata


def lire_mots_fichier(fichier='mots_pendu.txt'):
    with open('mots_pendu.txt', 'r') as fichier:
        mots = fichier.read()
    return mots

def supprimer_accents(mot):
    return ''.join(c for c in unicodedata.normalize('NFD', mot) if unicodedata.category(c) != 'Mn')

def choisir_mot(mots):
    return random.choice(mots)


def afficher_mot(mot, lettres_devinees):
    return ' '.join([lettre if lettre in lettres_devinees else '_' for lettre in mot])

def demander_lettre():
    return input("Devinez une lettre: ").lower()

def verifier_lettre(mot, lettre):
    return lettre in mot


def jeu_pendu():
    mots = lire_mots_fichier()
    mot = choisir_mot(mots)
    mot_sans_accents = supprimer_accents(mot)

    lettres_devinees = set()
    chances = 6

    while chances > 0:
        print(f"\nMot à deviner: {afficher_mot(mot_sans_accents, lettres_devinees)}")
        print(f"Chances restantes: {chances}")

        lettre = demander_lettre()

        if verifier_lettre(mot_sans_accents, lettre):
            lettres_devinees.add(lettre)
            if all(l in lettres_devinees for l in mot_sans_accents):
                print(f"Félicitations ! Vous avez deviné le mot : {mot}")
                break
        else:
            chances -= 1

        if chances == 0:
            print(f"Dommage ! Vous avez perdu. Le mot était : {mot}")

    rejouer = input("Voulez-vous rejouer ? (o/n): ").lower()
    if rejouer == 'o':
        jeu_pendu()


if __name__ == "__main__":
    jeu_pendu()