import sys


def main():
    print("=== Player Score Analytics ===")
    if len(sys.argv) < 2:
        print("No scores provided. Usage: python3",
              "ft_score_analytics.py <score1> <score2> ...")
        return

    scores = []
    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            print("Error: Scores must be numbers")
            return
    print(f"Scores processed: {scores}")
    print(f"Total Players: {len(scores)}")
    print()

    print(f"Total score: {sum(scores)}")
    print(f"Average Score: {sum(scores) / len(scores)}")
    print(f"High Score: {max(scores)}")
    print(f"Low Score: {min(scores)}")
    print(f"Score Range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
