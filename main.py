class Animal:
    all_animals = []

    def __init__(self, name, weight, food, extract):
        self.name = name
        self.weight = weight
        self.food = food
        self.extract = extract
        self.all_animals.append(self)

    def eat(self, food):
        self.weight += food
        print(f'{self.name} накормлен')
        print(f'Вес {self.name} {round(self.weight, 1)} кг.')


class GiveEggs(Animal):
    def collect_eggs(self, count):
        print(f'{self.name} снесла {count} яйцо')


class Goose(GiveEggs):
    voice = 'Га-га-га'


class Chicken(GiveEggs):
    voice = 'Ко-ко-ко'


class Duck(GiveEggs):
    voice = 'Кря-кря-кря'


class GiveMilk(Animal):
    def milking(self, volume):
        print(f'{self.name} дала {volume} литра(ов) молока')
        self.weight -= volume
        print(f'Вес {self.name} {round(self.weight, 1)} кг.')


class Cow(GiveMilk):
    voice = 'Му-му-му'


class Goat(GiveMilk):
    voice = 'Ме-ме-ме'


class GiveWool(Animal):
    def haircut(self, value):
        print(f'{self.name} дала {value} кг. шерсти')
        self.weight -= value
        print(f'Вес {self.name} {round(self.weight, 1)} кг.')


class Sheep(GiveWool):
    voice = 'Бе-бе-бе'


goose_1 = Goose('Серый', 5, 1, 2)
goose_2 = Goose('Белый', 4, 1.3, 1)

cow_1 = Cow('Манька', 100, 10, 5)

sheep_1 = Sheep('Барашек', 50, 3, 1.5)
sheep_2 = Sheep('Кудрявый', 55, 3.5, 2)

chicken_1 = Chicken('Ко-Ко', 2, 0.5, 3)
chicken_2 = Chicken('Кукареку', 1.5, 0.7, 2)

goat_1 = Goat('Рога', 25, 3.2, 1)
goat_2 = Goat('Копыта', 22, 2.9, 1.3)

duck_1 = Duck('Кряква', 3, 1.2, 2)

for animal in Animal.all_animals:
    print(animal.voice)
    if isinstance(animal, Animal):
        animal.eat(animal.food)
    if isinstance(animal, GiveEggs):
        animal.collect_eggs(animal.extract)
        print()
    if isinstance(animal, GiveMilk):
        animal.milking(animal.extract)
        print()
    if isinstance(animal, GiveWool):
        animal.haircut(animal.extract)
        print()