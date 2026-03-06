import sys


def main() -> None:
    print("=== Command Quest ===")
    if len(sys.argv) < 2:
        print("No Arguments Provided")
        print(f"Program Name: {sys.argv[0].split('/')[-1]}")
        print(f"Total Argument : {len(sys.argv)}")
    else:
        print(f"Program Name: {sys.argv[0].split('/')[-1]}")
        count: int = 1
        for arg in sys.argv[1:]:
            print(f"Argument {count}: {arg}")
            count += 1
        print(f"Total Argument : {len(sys.argv) - 1}")


if __name__ == "__main__":
    main()
