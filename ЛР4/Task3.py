class Zooshop:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def get_most_expensive_breed(self):
        if not self.animals:
            return None
        most_expensive_animal = max(self.animals, key=lambda animal: animal.cost)
        return most_expensive_animal.breed

class Animal:
    def __init__(self, breed, cost):
        self.breed = breed
        self.cost = cost

    def move(self):
        pass

class Fish(Animal):
    def move(self):
        return "Swimming"

class Bird(Animal):
    def move(self):
        return "Flying"

zooshop = Zooshop()

fish1 = Fish("Goldfish", 10)
fish2 = Fish("Guppy", 5)
bird1 = Bird("Parrot", 50)
bird2 = Bird("Canary", 20)

zooshop.add_animal(fish1)
zooshop.add_animal(fish2)
zooshop.add_animal(bird1)
zooshop.add_animal(bird2)

most_expensive_breed = zooshop.get_most_expensive_breed()
if most_expensive_breed:
    print("Most expensive breed:", most_expensive_breed)
else:
    print("No animals in the zooshop")

filename = "zooshop.txt"
with open(filename, "w") as file:
    for animal in zooshop.animals:
        file.write(f"Breed: {animal.breed}, Cost: {animal.cost}\n")
