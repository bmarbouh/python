#!/usr/bin/env python3
def check_temperature(temp_str: str):
    """Validate and check if temperature is within garden range."""
    try:
        n = int(temp_str)
        if 0 <= n <= 40:
            print(f"Temperature {n}°C is perfect for plants!")
        elif n < 0:
            print(f"Error: {n}°C is too cold for plants (min 0°C)")
        elif n > 40:
            print(f"Error: {n}°C is too hot for plants (max 40°C)")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input():
    """Run test cases for the temperature checker."""
    print("=== Garden Temperature Checker ===")
    print("\nTesting temperature: 25")
    check_temperature("25")

    print("\nTesting temperature: abc")
    check_temperature("abc")

    print("\nTesting temperature: 100")
    check_temperature("100")

    print("\nTesting temperature: -50")
    check_temperature("-50")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
