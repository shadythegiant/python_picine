from typing import List, Tuple
from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
)

Opponent = Tuple[CreatureFactory, BattleStrategy]


def run_tournament(
    name: str, display_str: str, opponents: List[Opponent]
) -> None:
    print(name)
    print(display_str)
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                print("* Battle *")

                fighter1 = opponents[i][0].create_base()
                strategy1 = opponents[i][1]

                fighter2 = opponents[j][0].create_base()
                strategy2 = opponents[j][1]

                print(fighter1.describe())
                print("VS.")
                print(fighter2.describe())
                print("now fight!")

                strategy1.act(fighter1)
                strategy2.act(fighter2)

    except InvalidStrategyError as e:
        print(f"Battle error, aborting tournament: {e}")


if __name__ == "__main__":
    flame_fact = FlameFactory()
    aqua_fact = AquaFactory()
    heal_fact = HealingCreatureFactory()
    transform_fact = TransformCreatureFactory()

    normal_strat = NormalStrategy()
    aggressive_strat = AggressiveStrategy()
    defensive_strat = DefensiveStrategy()

    run_tournament(
        "Tournament 0 (basic)",
        "[ (Flameling+Normal), (Healing+Defensive) ]",
        [(flame_fact, normal_strat), (heal_fact, defensive_strat)]
    )

    run_tournament(
        "Tournament 1 (error)",
        "[ (Flameling+Aggressive), (Healing+Defensive) ]",
        [(flame_fact, aggressive_strat), (heal_fact, defensive_strat)]
    )

    run_tournament(
        "Tournament 2 (multiple)",
        "[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]",
        [(aqua_fact, normal_strat), (heal_fact, defensive_strat),
         (transform_fact, aggressive_strat)]
    )
