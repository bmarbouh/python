

def validate_ingredients(ingredients: str) -> str:
    valid = ["fire", "water", "earth","air"]
    parts = ingredients.split(" ")
    for item in parts:
        if item not in valid:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"