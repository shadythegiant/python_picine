from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(inital_power: int) -> Callable:
    def power_accumlator(add_power: int) -> int:
        nonlocal inital_power
        inital_power += add_power
        return inital_power
    return power_accumlator


def enchantmen_factory(enchantment_type: str) -> Callable:
    def enchanted_description(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchanted_description


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")

    return {
        'store': store,
        'recall': recall
    }


def main() -> None:
    print("=== Testing mage counter ====")
    mage1 = mage_counter()
    mage2 = mage_counter()
    print(f"mage1 first call {mage1()}")
    print(f"mage1 second call {mage1()}")
    print(f"mage2 first call {mage2()}")

    print("\n ==== Testing Spell accumlator ====")
    acc = spell_accumulator(100)
    print(f"Base 100, add 20 {acc(20)}")
    print(f"Base 100, add 30 {acc(30)}")
    print(f"Base 100, add 40 {acc(40)}")

    print("\n === Testing enchantment factory ===")
    flaming = enchantmen_factory('Flaming')
    frozen = enchantmen_factory('Frozen')

    print(f"{flaming('Sword')}")
    print(f"{frozen('Shield')}")

    print("\n === Testing memory vault ===")
    vault = memory_vault()
    vault2 = memory_vault()
    vault['store']('secret', 30)
    print(f"recall 'secret' {vault['recall']('secret')}")
    print("testing an invalid key")
    print(f"recall 'unkown' {vault['recall']('unkown')}")
    print("recalling secrets using vault2")
    print(f"recall 'secrets' from vault2 {vault2['recall']('secret')} ")


if __name__ == "__main__":
    main()
