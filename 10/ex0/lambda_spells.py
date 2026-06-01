def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f" * {x} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0}
    max_power = max(mages, key=lambda x: x['power'])['power']
    min_power = min(mages, key=lambda x: x['power'])['power']
    avg_power = round(sum(map(lambda x: x['power'], mages)) / len(mages), 2)
    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power
    }


def main() -> None:
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
        {'name': 'Old Wand', 'power': 15, 'type': 'weapon'}
    ]

    mages = [
        {'name': 'A', 'power': 100, 'element': 'Fire'},
        {'name': 'B', 'power': 80, 'element': 'Water'},
        {'name': 'C', 'power': 120, 'element': 'Earth'},
    ]

    spells = ['fireball', 'heal', 'shield']

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    if len(sorted_artifacts) >= 2:
        print(
            f"{sorted_artifacts[0]['name']}({sorted_artifacts[0]['power']}"
            f"power) comes before {sorted_artifacts[1]['name']}"
            f"({sorted_artifacts[1]['power']} power)")

    print("\nTesting spell transformer...")
    for s in spell_transformer(spells):
        print(s)

    print("\nTesting power filter (min 90)...")
    print(power_filter(mages, 90))

    print("\nTesting mage stats...")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
