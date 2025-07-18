class Animal:
    def __init__(self, name, species, hunger=1, mood="Голодное"):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.mood = mood

    def make_sound(self):
        pass

    def feed(self):
        self.hunger += 1
        print(f"{self.name} поел. Очки настроения: {self.hunger}")
        self.check_mood()

    def play(self):
        self.hunger += 1
        print(f"{self.name} играет. Очки настроения: {self.hunger}")
        self.check_mood()

    def sleep(self):
        self.hunger += 1
        print(f"{self.name} уснул. Очки настроения: {self.hunger}")
        self.check_mood()

    def check_mood(self):
        if self.hunger >= 3:
            self.mood = "Счастливое"
        elif self.hunger == 2:
            self.mood = "Спокойное"
        elif self.hunger == 1:
            self.mood = "Голодное"
        else:
            self.mood = "Раздраженное"

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, species="Пёс", hunger=1)

    def make_sound(self):
        return "Гав!"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, species="Кот", hunger=0)

    def make_sound(self):
        return "Мяу!"

# Example usage
my_dog = Dog("Бобик")
my_cat = Cat("Пушок")

# Print info about the dog
print(my_dog.name)        # Output: Бобик
print(my_dog.species)     # Output: Пёс
print(my_dog.make_sound())# Output: Гав!
print(f"{my_dog.name} настроение: {my_dog.mood}") # Output: Бобик настроение: Голодное
my_dog.feed()             # Output: Бобик поел. Очки настроения: 2
my_dog.play()             # Output: Бобик играет. Очки настроения: 3
print(f"{my_dog.name} настроение: {my_dog.mood}") # Output: Бобик настроение: Счастливое

# Print info about the cat
print(my_cat.name)        # Output: Пушок
print(my_cat.species)     # Output: Кот
print(my_cat.make_sound())# Output: Мяу!
print(f"{my_cat.name} настроение: {my_cat.mood}") # Output: Пушок настроение: Голодное
my_cat.feed()             # Output: Пушок поел. Очки настроения: 1
my_cat.sleep()            # Output: Пушок уснул. Очки настроения: 2
print(f"{my_cat.name} настроение: {my_cat.mood}") # Output: Пушок настроение: Спокойное
