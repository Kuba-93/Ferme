from ferme import Ferme, Animal, Chat, Chien
from utils import ajouter_animal, crier_animaux, tuer_animal, afficher_nombre_animaux, quitter_programme

if __name__ == "__main__":
    ferme = Ferme()
    options = {
        1: ajouter_animal,
        2: crier_animaux,
        3: tuer_animal,
        4: afficher_nombre_animaux,
        5: quitter_programme
    }

    while True:
        print("1. Ajouter un animal")
        print("2. Lancer le cri de tous les animaux de la ferme")
        print("3. Tuer un animal")
        print("4. Afficher le nombre d'animaux dans la ferme")
        print("5. Quitter le programme")

        choix = input("----------Que souhaitez-vous faire ? ----------")

        if not choix.isnumeric() or int(choix) not in options:
            print("----------Choix non valide----------")
            continue

        options[int(choix)](ferme)
