from collections.abc import Callable
from typing import Tuple, List


def heal(target: str, power: int) -> str:
    return f"Heal restores {target}'s Power {power} HP"


def attack(target: str, power: int) -> str:
    return f"Attack {target}'s for  {power} Damage"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> Tuple[str, str]:
        return (spell1(target, power), spell2(target, power))

    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def multiplied_spell(target: str, power: int):
        multiplied = power * multiplier
        return base_spell(target, multiplied)
    return multiplied_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional_spell(target: str, power: int):
        if condition(target, power):
            return spell(target, power)
        else:
            return "spell fizzeled"
    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence_spell(target: str, power: int) -> List[str]:
        return [s(target, power) for s in spells]
    return sequence_spell


def main() -> None:
    print("======  Testing spell combiner ====")
    combined_spells = spell_combiner(heal, attack)
    res1, res2 = combined_spells("Berber Goat", 100)
    print(f"spell 1 {res1} , spell 2 {res2}")

    print("\n ===== Testing  spell amplifier ======== ")
    amplified_spell = power_amplifier(attack, 10)
    print(amplified_spell('Berber goat', 10))
    print("original attack power  : 10 , amplified : 100 ")

    print("\n ======= Testing conditional caster ======")
    def is_strong(t, p): return p >= 20
    conditional = conditional_caster(is_strong, attack)
    print("test case 1 : condition is not satisfied :(")
    print(conditional('cat', 10))
    print("test case 2 : condition is  satisfied :)")
    print(conditional('lion', 50))

    print("\n Testing Spell sequence")
    spells = [heal, attack, heal]
    sequence = spell_sequence(spells)
    str_list = sequence("Berber Lion", 100)
    print(str_list)


if __name__ == "__main__":
    main()
