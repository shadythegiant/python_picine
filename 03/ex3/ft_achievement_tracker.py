def main():
    print("=== Achievement Tracker System ===")

    alice_achievements = {
        'First Blood',
        'Unstoppable',
        'Baron Slayer',
        'Visionary',
        'Level10'
    }
    bob_achievements = {
        'First Blood',
        'Dragon Slayer',
        'Pentakill',
        'Visionary'}
    charlie_achievements = {
        'Dragon Slayer',
        'Unstoppable',
        'Baron Slayer',
        'Sharpshooter',
        'Visionary'}
    print(f"Player alice achievements:{alice_achievements}")
    print(f"Player bob achievements:{bob_achievements}")
    print(f"Player charlie achievements:{charlie_achievements}")
    print()
    print("\n=== Achievement Analytics ===")
    all_acheivments = (
        alice_achievements |
        bob_achievements |
        charlie_achievements
    )
    print(f"All unique achievements: {all_acheivments}")
    print(f"Total unique achievements: {len(all_acheivments)}")
    print()
    common = (alice_achievements & bob_achievements & charlie_achievements)
    print(f"Common to all players: {common}")
    players = [alice_achievements, bob_achievements, charlie_achievements]
    rare_achievement = set()
    rare_count = []
    for achievement in alice_achievements:
        count = 0
        for player in players:
            if achievement in player:
                count += 1
        if count == 1:
            rare_count.append(player)
            rare_achievement.add(achievement)
    print(
        f"Rare achievement ({len(rare_count)} Player): {rare_achievement}")
    print()
    alice_vs_bob_common = alice_achievements & bob_achievements
    print(f"Alice vs Bob common: {alice_vs_bob_common}")

    alice_unique = alice_achievements - bob_achievements
    print()
    print(f"Alice unique: {alice_unique}")

    bob_unique = bob_achievements - alice_achievements
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    main()
