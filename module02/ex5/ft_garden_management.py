#!/usr/bin/env python3

class GardenError(Exception):
    """Base class for all garden management exceptions."""
    pass


class PlantError(GardenError):
    """Exception raised for plant-related errors."""
    pass


class WaterError(GardenError):
    """Exception raised for water-related errors."""
    pass


class GardenManager():
    """Manages garden operations including adding,
    watering, and health checks."""

    def __init__(self):
        """Initialize the garden manager with an empty list of plants."""
        self.plants = []

    def add_plant(self, name: str):
        """Add a new plant to the garden after validation."""
        if not name:
            raise PlantError("Plant name cannot be empty!")
        self.plants.append(name)
        print(f"Added {name} successfully")

    def water_all(self):
        """Simulate watering all plants with a guaranteed cleanup phase."""
        try:
            print("Opening watering system")
            for item in self.plants:
                print(f"Watering {item} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_helthy(self, name: str, water_level: int, sunlight: int):
        """Check plant health parameters and raise custom garden errors."""
        if water_level < 1:
            raise WaterError(f"Water level {water_level} is too low (min 1)")
        elif water_level > 10:
            raise WaterError(f"Water level {water_level} is too high (max 10)")
        elif sunlight < 2:
            raise PlantError(f"Sunlight hours {sunlight} is too low (min 2)")
        elif sunlight > 12:
            raise PlantError(f"Sunlight hours {sunlight} is too high (max 12)")
        print(f"{name}: healthy (water: {water_level}, sun: {sunlight})")


if __name__ == "__main__":
    manager = GardenManager()
    print("=== Garden Management System ===")
    print("")
    print("Adding plants to garden...")
    try:
        manager.add_plant("tomato")
        manager.add_plant("lettuce")
        manager.add_plant("")
    except PlantError as p:
        print(f"Error adding plant: {p}")
    print("")
    print("Watering plants...")
    manager.water_all()
    print("")
    print("Checking plant health...")
    try:
        manager.check_helthy("tomato", 5, 8)
        manager.check_helthy("lettuce", 15, 8)
    except WaterError as p:
        print(f"Error checking lettuce: {p}")
    print("")
    print("Testing error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as w:
        print(f"Caught GardenError: {w}")
        print("System recovered and continuing...")
    print("")
    print("Garden management system test complete!")
