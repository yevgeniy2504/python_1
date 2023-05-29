WEIGHT_LIMIT = 21

items_dict = {
    "lighter": 4,
    "boiler": 2,
    "knife": 3,
    "flashlight": 4,
    "hat": 1,
    "shirt": 2,
    "food": 4,
    "phone": 1,
    "jacket": 3,
    "water": 2,
    "gas": 2,
    "socks": 2,
    "tent": 6,
    "alcohol": 0.5,
    "first aid kit": 2,
    "map": 4,
    "compass": 2,
    "chess": 1,
    "hiking sticks": 4
}

permissible_items = {}
accumulate_weight = 0

for key, value in items_dict.items():
    if accumulate_weight + value < WEIGHT_LIMIT:
        permissible_items[key] = value
        accumulate_weight += value

print(permissible_items)

