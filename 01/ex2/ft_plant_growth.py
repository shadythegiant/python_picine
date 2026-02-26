class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age
        self.last_growth: int = 0

    def get_info(self) -> None:
        print(f"{self.name.capitalize()}: {self.height}cm, "
              f"{self.age} days old")

    def grow(self, growth_amount: int) -> None:
        self.height += growth_amount
        self.last_growth = growth_amount

    def age_one_day(self) -> None:
        self.age += 1


def main() -> None:
    print("=== Day 1 ===")
    rose = Plant("Rose", 25, 30)
    rose.get_info()
    for day in range(1, 8):
        rose.grow(1)
        rose.age_one_day()
    print("=== Day 7 ===")
    rose.get_info()
    print(f"Growth this week: +{rose.height - 25}cm")


if __name__ == "__main__":
    main()
