class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def is_Plant_Wilting(wilting: bool) -> None:
    if wilting:
        raise PlantError("the tomato plant is wilting")


def water_levels(level: int) -> None:
    if level < 5:
        raise WaterError("Not enough water in the tank")


def main() -> None:
    print("=== Custome Garden Error Demo ===")
    print("testing PlantError...")
    try:
        is_Plant_Wilting(True)
    except (PlantError) as e:
        print(f"Caught PlantError: {e}")
    print()
    print("testing WaterError...")
    try:
        water_levels(3)
    except (WaterError) as e:
        print(f"caught WaterError: {e}")
    print()
    print("Testing all garden Errors")
    for action in [lambda: is_Plant_Wilting(True),
                   lambda: water_levels(2)]:
        try:
            action()
        except GardenError as e:
            print(f"Caught a GardenError: {e}")
    print()
    print("all custom error types work correctly")


if __name__ == "__main__":
    main()
