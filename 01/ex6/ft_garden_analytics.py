class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self, amount: int) -> None:
        self.height += amount
        print(f"{self.name} grew {amount}cm")

    def get_info(self) -> str:
        return f"{self.name} {self.height}cm"


class FloweringPlant(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        color: str,
        blooming: bool = True,
    ) -> None:
        super().__init__(name, height)
        self.color: str = color
        self.blooming: bool = blooming

    def get_info(self) -> str:
        status = "blooming" if self.blooming else "not blooming"
        base = super().get_info()
        return f"{base}, {self.color} flowers ({status})"


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name: str,
        height: int,
        color: str,
        points: int,
    ) -> None:
        super().__init__(name, height,  color)
        self.points: int = points

    def get_info(self) -> str:
        base = super().get_info()
        return f"{base}, Prize points :{self.points} "


class GardenManager:
    class GardenStats:
        @staticmethod
        def calculate_score(plants: list) -> int:
            total_score = 0
            for plant in plants:
                if hasattr(plant, "points"):
                    total_score += plant.points
            return total_score

        @staticmethod
        def calculate_types(plants: list) -> str:
            regular = 0
            flowering = 0
            prize = 0
            for p in plants:
                if isinstance(p, PrizeFlower):
                    prize += 1
                elif isinstance(p, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return (
                f"{regular} regular, {flowering} flowering, "
                f"{prize} prize flowers"
            )

    # Manager setup :
    def __init__(self):
        self.gardens: dict = {}

    @classmethod
    def create_garden_network(cls):
        print("=== Garden Management System Demo ===")
        return cls()

    @staticmethod
    def validate_height(height: int) -> bool:
        return height > 0

    def add_plant(self, owner: str, plant: Plant) -> None:
        if owner not in self.gardens:
            self.gardens[owner] = []
        self.gardens[owner].append(plant)
        print(f"Added {plant.name} to {owner}'s garden")

    def grow_all(self, owner: str):
        print(f"=== {owner}'s Garden Report ===")
        if owner in self.gardens:
            for plant in self.gardens[owner]:
                plant.grow(1)

    def generate_report(self, owner: str):
        print(f"=== {owner}'s Garden Report ===")
        plants = self.gardens.get(owner, [])
        print("Plants in garden:")
        for plant in plants:
            print(f"- {plant.get_info()}")
        count = len(plants)
        # assuming 1cm of growth
        growth = count * 1
        print(f"Plants added: {count}, Total growth: {growth}cm")
        # types
        types_str = self.GardenStats.calculate_types(plants)
        print(f"Plant types: {types_str}")
        valid_height = self.validate_height(plants[0].height if plants else 0)
        print(f"Height validation test: {valid_height}")
        alice_score = self.GardenStats.calculate_score(
            self.gardens.get("Alice", []))
        bob_score = self.GardenStats.calculate_score(
            self.gardens.get("Bob", []))
        print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
        print(f"Total gardens managed: {len(self.gardens)}")


def main():
    manager = GardenManager.create_garden_network()
    # setting up alice garden
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    # adding plants to the manager

    manager.add_plant("Alice", oak)
    manager.add_plant("Alice", rose)
    manager.add_plant("Alice", sunflower)
    manager.grow_all("Alice")

    manager.add_plant("Bob", Plant("Bush", 82))

    manager.generate_report("Alice")


if __name__ == "__main__":
    main()
