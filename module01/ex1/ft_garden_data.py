#!/usr/bin/env python3
class Plant:
    """
    this class is for create same atribute to descripe a plant
    and a sole methode to show this information
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show_info(self) -> None:
        """
        this function use it to show same information
        """
        print(f"{self.name}: {self.height}cm {self.age} days old")


if __name__ == "__main__":
    plant_one = Plant("Rose", 25, 30)
    plant_two = Plant("Sunflower", 80, 45)
    plant_three = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    plant_one.show_info()
    plant_two.show_info()
    plant_three.show_info()
