import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    operations = {
        'add': operator.add,
        'multiply': operator.mul,
        'min': min,
        'max': max
    }
    if operation not in operations:
        raise ValueError("operation is unkown")
    return functools.reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire_spell = functools.partial(base_enchantment, 50, 'fire')
    ice_spell = functools.partial(base_enchantment, 100, 'ice')
    arcane_spell = functools.partial(base_enchantment, 60, 'arcane')
    return {
        'fire_spell': fire_spell,
        'ice_spell': ice_spell,
        'arcane_spell': arcane_spell
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def cast_spell(arg: Any) -> str:
        return "Unknown Spell"

    @cast_spell.register(int)
    def _(arg: int) -> str:
        return f"Damage spell: {arg} damage"

    @cast_spell.register(str)
    def _(arg: str) -> str:
        return f"Enchantment: {arg}"

    @cast_spell.register(list)
    def _(arg: list) -> str:
        return f"Multi-cast: {len(arg)} spells"

    return cast_spell


def main() -> None:
    print("/n ==== Testing Spell reducer ====")
    spells = [10, 20, 50]
    print(f"Testing multiplication {spell_reducer(spells, 'multiply')}")
    print(f"Testing addition {spell_reducer(spells, 'add')}")

    print("\n ==== Testing Partial enchanter ====")

    def base_enchantment(power: int, element: str, target: str):
        return f"{element} enchantment on {target} with {power} power"
    enchants = partial_enchanter(base_enchantment)
    print(enchants['fire_spell']('sword'))
    print(enchants['ice_spell']('GUN'))
    print(enchants['arcane_spell']('3okaz'))

    print("\n ==== Testing Memoized Fibonacci ==== ")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\n ==== Testing Spell Dispathcer =======")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher([1, 2, 3]))
    print(dispatcher(3.14))


if __name__ == "__main__":
    main()
