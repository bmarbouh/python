#!/usr/bin/env python3
import math


def calc_distance(start_position: tuple, second_position: tuple):
    x1, y1, z1 = start_position
    x2, y2, z2 = second_position
    calc = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(
        f"Distance between {start_position} and {second_position}: {calc:.2f}"
        )


def main():
    start_position = (0, 0, 0)
    player_position1 = (10, 20, 5)
    print(f"Position created: {player_position1}")
    calc_distance(start_position, player_position1)
    print("")
    try:
        valid_str_position = "3,4,0".split(",")
        valid_list = list()
        for item in valid_str_position:
            valid_list.append(int(item))
        valid_tuple = tuple(valid_list)
        print('Parsing coordinates: "3,4,0"')
        print(f"Parsed position: {valid_tuple}")
        calc_distance(start_position, valid_tuple)
        print("")
        not_str_position = "abc,def,ghi"
        print(f'Parsing invalid coordinates: "{not_str_position}"')
        invalid_list = not_str_position.split(",")
        error_position = list()
        for item in invalid_list:
            error_position.append(int(item))
    except ValueError as v:
        print(f"Error parsing coordinates: {v}")
        print(f'Error details - Type: ValueError, Args: ("{v}",)')
    print("")
    print("Unpacking demonstration:")
    x, y, z = valid_tuple
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("")
    main()
