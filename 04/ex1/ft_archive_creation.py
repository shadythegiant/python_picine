def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print()
    file_name: str = "new_discovery.txt"
    print(f"Initializing new storage unit: {file_name}")
    try:
        ofile = open(file_name, 'w')
    except Exception:
        print("Error! unable to create the file :(")
        return
    print("Storage unit created successfully...")
    print()
    print("Inscribing preservation data...")
    data: list[str] = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee"
    ]
    for e in data:
        print(e)
        ofile.write(e + "\n")
    print()
    ofile.close()
    print("Data inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    main()
