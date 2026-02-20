#!/usr/bin/env python3

data = {
    "alice": [
        "first_blood",
        "pixel_perfect",
        "speed_runner",
        "first_blood",
        "first_blood",
    ],
    "bob": [
        "level_master",
        "boss_hunter",
        "treasure_seeker",
        "level_master",
        "level_master",
    ],
    "charlie": [
        "treasure_seeker",
        "boss_hunter",
        "combo_king",
        "first_blood",
        "boss_hunter",
        "first_blood",
        "boss_hunter",
        "first_blood",
    ],
    "diana": [
        "first_blood",
        "combo_king",
        "level_master",
        "treasure_seeker",
        "speed_runner",
        "combo_king",
        "combo_king",
        "level_master",
    ],
    "eve": [
        "level_master",
        "treasure_seeker",
        "first_blood",
        "treasure_seeker",
        "first_blood",
        "treasure_seeker",
    ],
    "frank": [
        "explorer",
        "boss_hunter",
        "first_blood",
        "explorer",
        "explorer",
        "first_blood",
        "boss_hunter",
    ],
}


def player_achievements(data: dict):
    for player in data:
        player_set = set(data[player])
        print(f"Player {player} achievements: {player_set}")


def player_analystics(data: dict):
    all_unique = set()
    for player in data:
        player_set = set(data[player])
        all_unique = all_unique.union(player_set)
    print(f"All unique achievements: {all_unique}")
    print(f"Total unique achievements: {len(all_unique)}")


def common_player(data: dict):
    common = set()
    for p in data:
        common = common.union(set(data[p]))
    for player in data:
        player_set = set(data[player])
        common = common.intersection(player_set)
    if not common:
        print("Have no common with player")
    else:
        print(f"Common to all players: {common}")


def rare_achievments(data: list):
    all_rare = set()
    for player in data:
        current = set(data[player])
        others = set()
        for other in data:
            if player != other:
                others = others.union(set(data[other]))
        unique = current.difference(others)
        all_rare = all_rare.union(unique)
    print(f"Rare achievements (1 player): {all_rare}")


def player_to_player(player1: str, player2: str, data: dict):
    common = set(data[player1]).intersection(set(data[player2]))
    if not common:
        print(f"{player1} vs {player2} common: No common")
    else:
        print(f"{player1} vs {player2} common: {common}")
    print(
        f"{player1} unique: "
        f"{set(data[player1]).difference(set(data[player2]))}"
        )
    print(
        f"{player2} unique: "
        f"{set(data[player2]).difference(set(data[player1]))}"
        )


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print("")
    player_achievements(data)
    print("")
    print("=== Achievement Analytics ===")
    player_analystics(data)
    print("")
    common_player(data)
    rare_achievments(data)
    print("")
    player_to_player("alice", "bob", data)
