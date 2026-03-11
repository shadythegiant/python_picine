import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    print()
    sys.stdout.write("Input Stream active. Enter archivist ID: ")
    sys.stdout.flush()

    id: str = sys.stdin.readline().strip()
    sys.stdout.write("Input Stream active. Enter archivist ID: ")
    sys.stdout.flush()

    report: str = sys.stdin.readline()
    print()
    sys.stdout.write(f"[STANDARD] Archive status from {id}: {report }")
    sys.stderr.write(
        "[ALERT] System diagnostic: Communication channels verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")
    print()
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    main()
