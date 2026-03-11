def crisis_handler(filename: str, access_prefix: str) -> None:
    print(f"{access_prefix} : Attempting to access {filename}")
    try:
        with open(filename, 'r') as f:
            content: str = f.read().strip()
        print(f"SUCCESS: Archive recovered - ''{content}''")
        print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis handled, anomaly contained")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    crisis_handler("lost_archive.txt", "CRISIS ALERT")
    print()
    crisis_handler("classified_vault.txt", "CRISIS ALERT")
    print()
    crisis_handler("standard_archive.txt", "ROUTINE ACCESS")
    print()
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
