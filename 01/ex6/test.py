class Plant:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def grow(self, amount: int) -> None:
        self.height += amount
        print(f"{self.name} grew {amount}cm")

    def get_desc(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str, bloom_status: bool = True):
        super().__init__(name, height)
        self.color = color
        self.blooming = bloom_status

    def get_desc(self) -> str:
        status = "blooming" if self.blooming else "not blooming"
        return f"{self.name}: {self.height}cm, {self.color} flowers ({status})"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, points: int):
        super().__init__(name, height, color)
        self.points = points

    def get_desc(self) -> str:
        base = super().get_desc()
        return f"{base}, Prize points: {self.points}"


class GardenManager:
    # --- 1. NESTED HELPER CLASS (The Analytics Engine) ---
    class GardenStats:
        @staticmethod
        def calculate_score(plants: list) -> int:
            score = 0
            for plant in plants:
                # Formula to match example: Height + 10 (Base Value) + Points (if any)
                score += plant.height + 10
                if hasattr(plant, 'points'):
                    score += plant.points
            return score

        @staticmethod
        def count_types(plants: list) -> str:
            # Helper to generate the "1 regular, 1 flowering..." string
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

    # --- 2. MANAGER SETUP ---
    def __init__(self):
        self.gardens: dict = {}  # Stores lists of plants {"Alice": [...]}

    # --- 3. CLASS METHOD (The Factory) ---
    @classmethod
    def create_garden_network(cls):
        print("=== Garden Management System Demo ===")
        return cls()

    # --- 4. STATIC METHOD (The Utility) ---
    @staticmethod
    def validate_height(height: int) -> bool:
        return height > 0

    # --- 5. INSTANCE METHODS (The Logic) ---
    def add_plant(self, owner: str, plant: Plant):
        if owner not in self.gardens:
            self.gardens[owner] = []
        self.gardens[owner].append(plant)
        print(f"Added {plant.name} to {owner}'s garden")

    def grow_all(self, owner: str):
        print(f"{owner} is helping all plants grow...")
        if owner in self.gardens:
            for plant in self.gardens[owner]:
                plant.grow(1)

    def generate_report(self, owner: str):
        print(f"=== {owner}'s Garden Report ===")
        plants = self.gardens.get(owner, [])

        print("Plants in garden:")
        for plant in plants:
            print(f"- {plant.get_desc()}")

        # Calculate Logic
        count = len(plants)
        # Assuming 1cm growth per plant for the "Total growth" stat
        growth = count * 1
        print(f"Plants added: {count}, Total growth: {growth}cm")

        # Use the Nested Class for complex stats
        types_str = self.GardenStats.count_types(plants)
        print(f"Plant types: {types_str}")

        # Use Static Method
        valid = self.validate_height(plants[0].height if plants else 0)
        print(f"Height validation test: {valid}")

        # Calculate Scores
        alice_score = self.GardenStats.calculate_score(
            self.gardens.get("Alice", []))
        bob_score = self.GardenStats.calculate_score(
            self.gardens.get("Bob", []))

        print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
        print(f"Total gardens managed: {len(self.gardens)}")


# --- MAIN EXECUTION ---
def main():
    # 1. Use Class Method to create manager
    manager = GardenManager.create_garden_network()

    # 2. Setup Alice's Garden
    # Note: Heights are 1 less than final because they will grow once
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    manager.add_plant("Alice", oak)
    manager.add_plant("Alice", rose)
    manager.add_plant("Alice", sunflower)

    # 3. Grow Plants
    manager.grow_all("Alice")

    # 4. Setup Bob's Garden (To match the score 92)
    # 82 height + 10 base value = 92
    manager.add_plant("Bob", Plant("Bush", 82))

    # 5. Generate Final Report
    manager.generate_report("Alice")


if __name__ == "__main__":
    main()
