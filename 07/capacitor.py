from ex1 import HealingCreatureFactory, TransformCreatureFactory
from typing import cast
from ex1.capabilities import HealCapability, TransformCapability


def test_healing_creature(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")

    # Test Base
    print("base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(cast(HealCapability, base).heal())

    # Test Evolved
    print("evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    # Targeting 'itself and others' as per the PDF output example
    print(cast(HealCapability, base).heal("itself and others"))


def test_transforming_creature(factory: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")

    # Test Base
    print("base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(cast(TransformCapability, base).transform())
    print(base.attack())
    print(cast(TransformCapability, base).revert())

    # Test Evolved
    print("evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(cast(TransformCapability, evolved).transform())
    print(evolved.attack())
    print(cast(TransformCapability, evolved).revert())


if __name__ == "__main__":
    heal_fact = HealingCreatureFactory()
    transform_fact = TransformCreatureFactory()

    test_healing_creature(heal_fact)
    test_transforming_creature(transform_fact)
