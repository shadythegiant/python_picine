def recursive_helper(current_day: int, final_day: int) -> None:
    if current_day > final_day:
        print("Harvest time!")
        return
    print(f"Day {current_day}")
    recursive_helper(current_day + 1, final_day)


def ft_count_harvest_recursive():
    day_to_harvest = int(input("Days until harvest: "))
    recursive_helper(1, day_to_harvest)
