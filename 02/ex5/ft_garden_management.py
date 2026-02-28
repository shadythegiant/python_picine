class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(
            self,
            name: str,
            water_level: int,
            sunlight_hours: int
    ) -> None:
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager:
    def __init__(self):
        self.garden: list[Plant] = []

    def check_name(self, plant_name: str) -> None:
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")

    def check_water_level(self, water_level: int) -> None:
        if water_level < 1:
            raise WaterError(f"Water level {water_level} is too low (min 1)")
        if water_level > 10:
            raise WaterError(f"Water level {water_level} is too high (max 10)")

    def check_sunlight(self, sunlight_hours: int) -> None:
        if sunlight_hours < 2:
            raise PlantError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)")
        if sunlight_hours > 12:
            raise PlantError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)")

    def add_plant(
            self,
            name: str,
            water_level: int,
            sunlight_hours: int
    ) -> None:
        try:
            self.check_name(name)
            plant = Plant(name, water_level, sunlight_hours)
            self.garden.append(plant)
            print(f"Added {name} successfuly")
        except GardenError as e:
            print(f"Error Adding Plant : {e}")

    def water_plants(self, water_level: int) -> None:
        if water_level < 2:
            raise WaterError("Not Enough water in the tanks")
        print("Watering Plants")
        sys_open = False
        try:
            print("Opening Watering system")
            sys_open = True
            for plant in self.garden:
                if not isinstance(plant, Plant):
                    raise PlantError(f"Cannot water {plant} - invalid plant!")
                print(f"Watering {plant.name} - Success")
        except GardenError as e:
            print(f"Error watering Plant : {e}")
        finally:
            if sys_open:
                print("Closing Watering system (cleanup)")

    def check_health(self) -> None:
        print("Checking plant health...")
        for plant in self.garden:
            try:
                self.check_name(plant.name)
                self.check_water_level(plant.water_level)
                self.check_sunlight(plant.sunlight_hours)
                print(f"{plant.name} healthy"
                      f" (water {plant.water_level} "
                      f"sun:{plant.sunlight_hours})")
            except GardenError as e:
                print(f"Error checking {plant.name} : {e}")


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    print()
    manager = GardenManager()
    print("Adding Plants to garden")
    manager.add_plant("tomato", 5, 8)
    manager.add_plant("lettuce", 10, 12)
    manager.add_plant("", 5, 3)
    print()
    try:
        manager.water_plants(2)
    except WaterError as e:
        print(f"Caugh Garden Error : {e}")
    print()

    manager.check_health()
    print()

    print("Testing error recovery...")
    try:
        manager.water_plants(1)
    except WaterError as e:
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...")
    print()
    print("Garden management system test complete!")


def main() -> None:
    test_garden_management()


if __name__ == "__main__":
    main()
