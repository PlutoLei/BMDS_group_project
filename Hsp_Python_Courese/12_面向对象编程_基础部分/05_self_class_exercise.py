class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def compare_to(self, other):
        return self.name == other.name and self.age == other.age


Tom = Person("Tom", 18)
Tim = Person("Tim", 19)
print(Tom.compare_to(Tim))
