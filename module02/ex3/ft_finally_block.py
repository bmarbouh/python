#!/usr/bin/env python3

def water_plants(plant_list: list):
    """Attempt to water a list of plants and ensure system cleanup."""
    try:
        print("Opening watering system")
        for item in plant_list:
            if not item:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {item}")
    except ValueError as v:
        print(f"Error: {v}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """Run test cases to demonstrate the try/except/finally flow."""
    print("Testing normal watering...")
    normal_list = ["tomato", "lettuce", "carrots"]
    water_plants(normal_list)
    print("Watering completed successfully!")
    print("")
    print("Testing with error...")
    error_list = ["tomato", None, "carrots"]
    water_plants(error_list)
    print("")
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print("")
    test_watering_system()
