import time
import functools
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Spell completed in {duration:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get('power')
            if power is None:
                for arg in args:
                    if isinstance(arg, int):
                        power = arg
                        break

            if power is not None and power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"

        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        "Spell failed, retrying..."
                        f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return name.replace(" ", "").isalpha()

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("=== Testing spell timer... ===")

    @spell_timer
    def fireball():
        time.sleep(0.101)
        return "Result: Fireball cast!"
    print(fireball())
    print("\n=== Testing retrying spell... ===")
    fail_count = 0

    @retry_spell(3)
    def unstable_spell():
        global fail_count
        fail_count += 1
        if fail_count <= 3:
            raise ValueError("Fizzle!")
        return "Waaaaaaagh spelled !"
    print(unstable_spell())

    print("\n=== Testing MageGuild... ===")
    print(MageGuild.validate_mage_name("Gandalf The Grey"))
    print(MageGuild.validate_mage_name("A1"))

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))
