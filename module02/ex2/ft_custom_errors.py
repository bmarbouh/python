#!/usr/bin/env python3

class GardenError(Exception):
    """Base exception for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception raised for plant-specific problems."""
    pass


class WaterError(GardenError):
    """Exception raised for watering system issues."""
    pass


def test_plant():
    """Simulate a plant error by raising PlantError."""
    raise PlantError("The tomato plant is wilting!")


def test_water():
    """Simulate a water error by raising WaterError."""
    raise WaterError("Not enough water in the tank!")


def create_error():
    """Demonstrate catching specific and general garden errors."""
    try:
        print("Testing PlantError...")
        test_plant()
    except PlantError as pe:
        print(f"Caught PlantError: {pe}")
    print("")
    try:
        print("Testing WaterError...")
        test_water()
    except WaterError as wa:
        print(f"Caught WaterError: {wa}")
    print("")
    for func in [test_plant, test_water]:
        try:
            func()
        except GardenError as ge:
            print(f"Caught a garden error: {ge}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print("")
    create_error()
    print("")
    print("All custom error types work correctly!")
