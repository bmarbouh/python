#!/usr/bin/env python3

def garden_operations():
    """Demonstrate common Python built-in exception types."""
    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    print("")
    try:
        print("Testing ZeroDivisionError...")
        10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    print("")
    try:
        print("Testing FileNotFoundError...")
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    print("")
    try:
        print("Testing KeyError...")
        key_error = {}
        key_error["missing_plant"]
    except KeyError as k:
        print(f"Caught KeyError: {k}")
    print("")
    try:
        print("Testing multiple errors together...")
        int("abc")
        10 / 0
        open("bilal.txt")
        {"name": "bilal"}
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    print("")


def test_error_types():
    """Execute the garden error demonstration suite."""
    garden_operations()
    print("All error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    print("")
    test_error_types()
