class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def cri(self):
        pass

class Chat(Animal):
    def cri(self):
        return "Miaou"

class Chien(Animal):
    def cri(self):
        return "Ouaf"

class Ferme:
    def __init__(self):
        self.animaux = []

    def ajouter_animal(self, animal):
        self.animaux.append(animal)

    def crier(self):
        for animal in self.animaux:
            print(animal.cri())

    def __str__(self):
        return f"Ferme avec {len(self.animaux)} animaux"