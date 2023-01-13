from ferme import Chat, Chien

def ajouter_animal(ferme):
    type_animal = input("----------Quel type d'animal souhaitez-vous ajouter (Chat/Chien) ? ----------")
    nom = input("----------Quel est le nom de l'animal ? ----------")
    age = input("----------Quel est l'âge de l'animal ? ----------")

    if type_animal == "Chat":
        animal = Chat(nom, age)
    elif type_animal == "Chien":
        animal = Chien(nom, age)
    else:
        print("----------Type d'animal non valide----------")
        return

    ferme.ajouter_animal(animal)
    print(f"{type_animal} {nom} est né")

def crier_animaux(ferme):
    ferme.crier()

def tuer_animal(ferme):
    nom = input("----------Quel est le nom de l'animal à tuer ? ----------")

    for animal in ferme.animaux:
        if animal.nom == nom:
            ferme.animaux.remove(animal)
            print(f"----------{type(animal).__name__} {nom} est mort----------")
            return
    print(f"----------Il n'y a pas d'animal nommé {nom} dans la ferme----------")

def afficher_nombre_animaux(ferme):
    print(f"----------Ma ferme a {len(ferme.animaux)} animaux----------")

def quitter_programme():
    print("----------Au revoir !----------")
    exit()
