# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# -У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# -Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.
#
# Доработайте задачу 5.
# -Вынесите общие свойства и методы классов в класс
# Животное.
# -Остальные классы наследуйте от него.
# -Убедитесь, что в созданные ранее классы внесены правки.


class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def move(self):
        print(f"{self.name} обитает в {self.habitat}.")


class Fish(Animal):
    def __init__(self, name, size, habitat):
        super().__init__(name, habitat)
        self.size = size

    def swim(self):
        print(f"{self.name} является {self.habitat} и имеет {self.size} вес.")


class Bird(Animal):
    def __init__(self, name, wingspan, diet, habitat):
        super().__init__(name, habitat)
        self.wingspan = wingspan
        self.diet = diet

    def fly(self):
        print(f"{self.name} достигает {self.wingspan} и ест {self.diet}.")


class Mammal(Animal):
    def __init__(self, name, weight, habitat):
        super().__init__(name, habitat)
        self.weight = weight

    def move(self):
        super().move()
        print(f"{self.name} весит {self.weight}.")


# Example usage
fish1 = Fish("Лосось", "крупный", "пресноводный")
fish1.swim()


bird1 = Bird("Орел", "70 сантиметров", "мясо", "небо")
bird1.fly()

mammal1 = Mammal("Лев", "200 кг", "Саванна")
mammal1.move()
