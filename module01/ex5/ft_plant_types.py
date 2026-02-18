#!/usr/bin/env python3
class Plant:
    """
    this is parent class have same info for a plant like age and height and age
    """
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """
    for Flower inhert attribute from Plant class and also have same
    method like bloom and attribute like color
    """
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """
        Docstring for bloom
        bloom is function use it to show Flower information
        """
        print(
            f"{self.name}(Flower): {self.height}cm, "
            f"{self.age} days, {self.color} color"
            )
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """
    for Tree also inhert attribute from Plant class and
    have an atribute like diameter and have one method
    """
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """
        Docstring for produce_shade
        this method he's for show information for Tree like age name ...
        """
        print(
            f"{self.name} (Tree): {self.height}cm, {self.age} days, "
            f"{self.trunk_diameter}cm diameter"
            )
        print(f"{self.name} provides 78 square meters of shade")


class Vegetable(Plant):
    """
    for Vegetable inhert method from plant and also have
    an atributes like season and nutrition
    """
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            harvest_season: str,
            nutrition: str
            ):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutrition = nutrition

    def display_nutrition(self):
        """
        Docstring for display_nutrition
        this function use it to displav vegetable information
        """
        print(
            f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
            f"{self.harvest_season} harvest"
            )
        print(f"{self.name}  is rich in {self.nutrition}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print()
    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    rose.bloom()
    print()
    oak.produce_shade()
    print()
    tomato.display_nutrition()
