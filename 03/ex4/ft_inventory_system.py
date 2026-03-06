import sys


def main() -> None:
    inventory = dict()
    if len(sys.argv) < 2:
        print("Error: No arguments provided")
        print("Correct form: item:quantity (for example: potion:3)")
        return
    try:
        for arg in sys.argv[1:]:
            if ':' in arg:
                parts = arg.split(':')
                key = parts[0]
                value = int(parts[1])
                inventory.update({key: value})
            else:
                raise ValueError(arg)
    except ValueError:
        print("Error: Invalid argument: {arg}")
        print("Correct form: item:quantity (for example: potion:3)")
        return
    print()
    print("=== Inventory System Analysis ===")
    item_count = 0
    for v in inventory.values():
        item_count += v
    unique_types = len(inventory.keys())
    print(f"Total items in inventory:{item_count}")
    print(f"Unique item types:{unique_types}")
    print()
    print("=== Current Inventory ===")
    for item in inventory.items():
        units = "units" if item[1] > 1 else "unit"
        percentage = (item[1] * 100) / item_count
        print(f"{item[0]}: {item[1]} {units}({percentage:.1f}%)")
    print()
    print("=== Inventory Statistics ===")
    max_val = max(inventory.values())
    max_key = max(inventory, key=inventory.get)
    min_val = min(inventory.values())
    min_key = min(inventory, key=inventory.get)
    units = "units" if min_val > 1 else "unit"
    print(f"Most abundant: {max_key}({max_val} units)")
    print(f"Least abundant:{min_key}({min_val} {units})")
    print()
    print("=== Item Categories ===")
    scarce_dict = dict()
    moderate_dict = dict()
    for k, v in inventory.items():
        if v >= 5:
            moderate_dict.update({k: v})
        else:
            scarce_dict.update({k: v})
    print(f"Moderate: {moderate_dict}")
    print(f"Scarce:   {scarce_dict}")
    print()
    print("=== Management Suggestions ===")
    needed_items = list()
    for k, v in scarce_dict.items():
        if v <= 1:
            needed_items.append(k)
        else:
            pass

    print(f"Restock needed: {needed_items}")
    print()
    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary Value: {list(inventory.values())}")
    lookup_query = "True" if inventory.get('sword', 0) > 1 else "False"
    print(f"Sample lookup - 'sword' in inventory: {lookup_query}")


if __name__ == "__main__":
    main()
