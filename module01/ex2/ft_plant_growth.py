#!/usr/bin/env python3
class Plant:
    """
    Rule of this class is create same informotion about plant
    and also smae method like grow and ages,get_info
    """
    def __init__(self, name: str, height: int, ages: int):
        self.name = name
        self.height = height
        self.age = ages

    def grow(self):
        """
        Docstring for grow
        this funtion have a sole thing is increment
        hieght by one in avery call
        """
        self.height += 1

    def ages(self):
        """
        Docstring for ages
        this method id for increament age by one in each call
        """
        self.age += 1

    def get_info(self):
        """
        Docstring for get_info
        this is for show information like name and age and height
        """
        return f"{self.name}: {self.height}cm {self.age} days old"


if __name__ == "__main__":
    plant = Plant("Rose", 25, 30)
    height = plant.height
    print("=== Day 1 ===")
    print(plant.get_info())
    for x in range(6):
        plant.ages()
        plant.grow()
    print("=== Day 7 ===")
    height = plant.height - height
    print(plant.get_info())
    print(f"Growth this week: +{height}cm")
