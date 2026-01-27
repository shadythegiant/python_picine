class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age


class Flower(Plant):
    def __init__(
        self, name: str, height: int, age: int, color: str, bloom: str
    ) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self.bloom: str = bloom

    def bloom(self) -> None:
        print(f"{self.name} is blooming!")

    def get_info(self) -> str:
        return (f"{self.name} (Flower): {self.height}cm, {self.age} days, "
                f"{self.color.lower()} color\n"
                f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(
        self, name: str, height: int, age: int, trunk_diameter: int
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> int:
        return int(self.height * self.trunk_diameter / 100)

    def get_info(self) -> str:
        shade_area = self.produce_shade()
        return (f"{self.name} (Tree): {self.height}cm, {self.age} days, "
                f"{self.trunk_diameter}cm diameter\n"
                f"{self.name} provides {shade_area} square meters of shade")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str,
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value

    def get_info(self) -> str:
        return (f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
                f"{self.harvest_season.lower()} harvest\n"
                f"{self.name} is rich in {self.nutritional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 25, 30, "Red", "Spring")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("Tomato", 80, 90, "Summer", "Vitamin C")
    plants = [rose, oak, tomato]
    for plant in plants:
        print(plant.get_info())
        print()


if __name__ == "__main__":
    main()
