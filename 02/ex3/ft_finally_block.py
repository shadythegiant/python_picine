class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class Plant:
    def __init__(self, name: str):
        self.name = name


def water_plants(plant_list: list):
    sys_open: bool = False
    try:
        print("Opening Water Systems")
        sys_open = True
        for plant in plant_list:
            if not isinstance(plant, Plant):
                raise PlantError(
                    f"Error: cannot water {plant} - Invalid plant")
            print(f"Watering {plant.name}")
    except PlantError as e:
        print(f"Error: {e}")
    finally:
        if sys_open:
            print("Closing watering system (cleanup)")
        sys_open = False


def test_watering_system() -> None:
    print()
    plants = [
        Plant("Rose"),
        Plant("cactus"),
        Plant("Daisy")
    ]

    invalid_Plants = [
        None
    ]
    print("Testing normal watering...")
    water_plants(plants)
    print("Watering completed successfully")
    print()
    print("Testing with errors")
    water_plants(invalid_Plants)
    print()
    print("Cleanup always happens, even with errors!")


def main() -> None:
    print("=== Garden Watering System ===")
    test_watering_system()


if __name__ == "__main__":
    main()
