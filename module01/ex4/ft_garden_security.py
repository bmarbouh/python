#!/usr/bin/env python3
class SecurePlant:
    """
    this created to make attribute protected and to init
    same information like name height and age and
    also have methods to helpe u set/get in a property
    """
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self._height = height
        self._age = age

    def get_height(self) -> int:
        """
        Docstring for get_height
        :return: height of plant
        :rtype: int
        """
        return self._height

    def get_age(self) -> int:
        """
        Docstring for get_age
        :param self: for get age
        :return: age of plant
        :rtype: int
        """
        return self._age

    def set_height(self, n_height: int) -> None:
        """
        Docstring for set_height
        use it to set a new height to plant and this height must be valid
        :param n_height: is a new height and to set it must be valid
        :type n_height: int
        """
        if n_height >= 0:
            self._height = n_height
            print(f"Height updated: {n_height}cm [OK]")
        else:
            print(
                f"Invalid operation attempted: height {n_height}cm [REJECTED]"
                )
            print("Security: Negative height rejected")

    def set_age(self, new_age: int) -> None:
        """
        Docstring for set_age
        use it to set new age to plant and this age
        must be valid else he show a error message
        :type new_age: int
        """
        if new_age >= 0:
            self._age = new_age
            print(f"Age updated: {new_age} days [OK]")
        else:
            print(
                f"Invalid operation attempted: age {new_age} days [REJECTED]"
                )
            print("Security: Negative age rejected")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    p = SecurePlant("Rose", 25, 365)
    print(f"Plant created: {p.name}")
    p.set_height(25)
    p.set_age(30)
    print()
    p.set_height(-5)
    print()
    print(f"Current plant: {p.name} ({p.get_height()}cm, {p.get_age()} days)")
