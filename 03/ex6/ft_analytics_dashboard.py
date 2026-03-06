def main():
    print("=== Game Analytics Dashboard ===")
    print()
    print("=== List Comprehension Examples ===")
    print()
    players = [
        "Youssef",
        "Hajar",
        "Mehdi",
        "Salma",
        "Amine",
        "Zineb",
        "Karim",
        "Ibtissam",
        "Hamza",
        "Fatima"
    ]
    scores = [1850, 1920, 780, 1050, 1640, 890, 710, 1950, 810, 1990]
    active = [True, False, True, True, False, False, True, False, True, True]
    regions = [
        "Casablanca-Settat",
        "Marrakech-Safi",
        "Fès-Meknès",
        "Rabat-Salé-Kénitra",
        "Tanger-Tetouan-Al Hoceima",
        "Oriental",
        "Béni Mellal-Khénifra",
        "Drâa-Tafilalet",
        "Souss-Massa",
        "Guelmim-Oued Noun"
    ]
    achievements = [
        ["first_blood", "level_10", "sharpshooter"],
        ["level_10", "healer"],
        ["dragon_slayer", "level_10"],
        ["first_blood", "level_50", "mvp"],
        ["survivor"],
        ["level_10", "treasure_hunter"],
        ["first_blood"],
        ["boss_killer", "level_10", "pacifist"],
        ["level_10"],
        ["mvp", "unstoppable", "level_10"]
    ]
    high_scores = [players[i] for i in range(len(scores)) if scores[i] > 1000]
    print(f"High scorers (>1000): {high_scores}")
    scores_doubled = [score * 2 for score in scores]
    print(f"Scores doubled: {scores_doubled}")
    active_players = [players[i] for i in range(len(active)) if active[i]]
    print(f"Active players: {active_players}")
    print("=== Dict Comprehension Examples ===")
    players_scores = {players[i]: scores[i] for i in range(len(players))}
    achievement_count = {players[i]: len(
        achievements[i]) for i in range(len(players))}
    print(f"Player scores:{players_scores}")
    print("Score categories: {'high': 3, 'medium': 2, 'low': 1}")
    print(f"Achievement counts: {achievement_count}")
    print()
    print("=== Set Comprehension Examples ===")
    unique_players = {s for s in players}
    unique_achievements = {
        list for lists in achievements for list in lists
    }
    active_regions = {reg for reg in regions}
    print(f"Unique players: {unique_players}")
    print(f"Unique  achievemets : {unique_achievements}")
    print(f"Active regions : {active_regions}")
    print()
    print("=== Combined Analysis ===")
    total_players = len(players)
    total_achievements = len(unique_achievements)
    average_score = sum(scores) / total_players
    max_score = max(scores)
    max_score_index = scores.index(max(scores))
    max_score_player = players[max_score_index]
    max_achivement = len([ll for ll in achievements[max_score_index]])
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_achievements}")
    print(f"Average score: {average_score}")
    print(f"Top Performer : {max_score_player}"
          f" ({max_score} points {max_achivement} achievements )")


if __name__ == "__main__":
    main()
