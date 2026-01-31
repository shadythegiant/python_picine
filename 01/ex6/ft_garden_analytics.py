class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self, amount: int) -> None:
        self.height += amount
        print(f"{self.name} grew {self.height}cm")

    def get_info(self) -> None:
        return f"{self.name} {self.height}cm"


class FloweringPlant(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        color: str,
        blooming: bool,
    ) -> None:
        super().__init__(name, height)
        self.color: str = color
        self.blooming: bool = blooming

    def get_info(self):
        status = "blooming" if {self.blooming} else "not blooming"
        return f"{self.name}: {self.height}cm, {self.color} flowers ({status})"


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str,
        points: int,
    ) -> None:
        super().__init__(name, height, age, color)
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
            return f"{regular} regular, {flowering} flowering, {prize} prize flowers"
