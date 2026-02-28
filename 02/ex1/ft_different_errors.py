def test_error_types() -> None:
    print("Testing multiple errors together")
    try:
        10 / 0
        open("config.txt")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but programme continues")


def garden_operations() -> None:
    my_data = {"grapefruit": 1, "elxirFruit": 2}
    print("Testing ValueError...")
    try:
        int("err")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    print()
    print("Testing ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError as e:
        print(f"caugh ZeroDivisionError: {e}")
    print()
    print("Testing FileNotFoundError...")
    try:
        open("config.json")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    print()
    print("Testing KeyError...")
    try:
        my_data["auntie"]
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    print()


def main():
    garden_operations()
    test_error_types()


if __name__ == "__main__":
    main()
