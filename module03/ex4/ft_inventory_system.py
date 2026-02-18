#!/usr/bin/env python3

data = {
    "players": {
        "alice": {
            "items": {
                "pixel_sword": 1,
                "code_bow": 1,
                "health_byte": 1,
                "quantum_ring": 3,
            },
            "total_value": 1875,
            "item_count": 6,
        },
        "bob": {
            "items": {
                "code_bow": 3,
                "pixel_sword": 2,
            },
            "total_value": 900,
            "item_count": 5,
        },
        "charlie": {
            "items": {
                "pixel_sword": 1,
                "code_bow": 1,
            },
            "total_value": 350,
            "item_count": 2,
        },
        "diana": {
            "items": {
                "code_bow": 3,
                "pixel_sword": 3,
                "health_byte": 3,
                "data_crystal": 3,
            },
            "total_value": 4125,
            "item_count": 12,
        },
    },
    "catalog": {
        "pixel_sword": {
            "type": "weapon",
            "value": 150,
            "rarity": "common",
        },
        "quantum_ring": {
            "type": "accessory",
            "value": 500,
            "rarity": "rare",
        },
        "health_byte": {
            "type": "consumable",
            "value": 25,
            "rarity": "common",
        },
        "data_crystal": {
            "type": "material",
            "value": 1000,
            "rarity": "legendary",
        },
        "code_bow": {
            "type": "weapon",
            "value": 200,
            "rarity": "uncommon",
        },
    },
}


def player_info(name: str):
    if name not in data['players']:
        print("player not found")
        return
    print(f"=== {name.capitalize()}'s Inventory ===")
    player_item = data['players'][name]['items']
    player_catalog = data['catalog']
    cate_count = {}
    category = ""
    for item in player_item:
        print(
            f"{item} ({player_catalog[item]['type']}, "
            f"{player_catalog[item]['rarity']}):"
            f" {player_item[item]}x @ {player_catalog[item]['value']} gold "
            f"each = {player_item[item] * player_catalog[item]['value']}"
            )
        if player_catalog[item]['type'] not in cate_count:
            cate_count[player_catalog[item]['type']] = player_item[item]
        else:
            cate_count[player_catalog[item]['type']] += player_item[item]
    print("")
    print(f"Inventory value: {data['players'][name]['total_value']}")
    print(f"Item count: {data['players'][name]['item_count']} items")
    category += "Categories:"
    first = True
    for c in cate_count:
        if not first:
            category += ','
        category += f" {c}({cate_count[c]})"
        first = False
    print(f"{category}")


def check_available(p_from: str, p_to: str, item: str, quantity: int):
    if p_from not in data['players']:
        print(f"{p_from} not found")
        return 0
    if p_to not in data['players']:
        print(f"{p_to} not found")
        return 0
    if item not in data['players'][p_from]['items']:
        print("item not found")
        return 0
    if data['players'][p_from]['items'][item] < quantity:
        print(f"{item}: {quantity} not availble")
        return 0
    return 1


def transaction(p_from: str, p_to: str, item: str, quantity: int):
    print(
        f"=== Transaction: {p_from} gives "
        f"{p_to} {quantity} {item} ==="
        )
    if check_available(p_from, p_to, item, quantity) == 0:
        print("Transaction Insuccessful!")
        return 0
    data['players'][p_from]['items'][item] -= quantity
    if item in data['players'][p_to]['items']:
        data['players'][p_to]['items'][item] += quantity
    else:
        data['players'][p_to]['items'][item] = quantity
    data['players'][p_from]['item_count'] -= quantity
    data['players'][p_to]['item_count'] += quantity
    data['players'][p_from]['total_value'] -= (
        data['catalog'][item]['value'] * quantity
        )
    data['players'][p_to]['total_value'] += (
        data['catalog'][item]['value'] * quantity
    )
    print("Transaction successful!")


def get_update(player1: str, player2: str, item: str):
    print("=== Updated Inventories ===")
    if not player1 or not player2:
        print("player not found")
        return
    print(f"{player1} {item}: {data['players'][player1]['items'][item]}")
    print(f"{player2} {item}: {data['players'][player2]['items'][item]}")


def analytics():
    most_item = 0
    most_gold = 0
    name_item = ""
    name_gold = ""
    print("=== Inventory Analytics ===")
    for player in data['players']:
        if most_item < data['players'][player]['item_count']:
            name_item = player
            most_item = data['players'][player]['item_count']
        if most_gold < data['players'][player]['total_value']:
            most_gold = data['players'][player]['total_value']
            name_gold = player
    print(f"Most valuable player: {name_gold} ({most_gold} gold)")
    print(f"Most items: {name_item} ({most_item} items)")
    str = ""
    catalog = data['catalog']
    first = True
    for item in catalog:
        rarity = catalog[item]['rarity']
        if rarity == 'rare' or rarity == 'legendary':
            if not first:
                str += f" ,{item}"
            else:
                str += f"{item}"
            first = False
    print(f"Rarest items: {str}")


if __name__ == "__main__":
    player1 = 'alice'
    player2 = 'bob'
    print("=== Player Inventory System ===")
    print("")
    player_info(player1)
    print("")
    transaction(player1, player2, 'pixel_sword', 1)
    print("")
    get_update(player1, player2, 'pixel_sword')
    print("")
    analytics()
