#!/usr/bin/env python3
class Plant:
    """
    this calss have only 3 attribute to discrape a plant and have no methods
    """
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    all = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]
    print("=== Plant Factory Output ===")
    for x in all:
        print(f"Created: {x.name} ({x.height}cm, {x.age} days)")
    print()
    print(f"Total plants created: {len(all)}")
