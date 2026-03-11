def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    file_name: str = "ancient_fragment.txt"
    print(f"Accessing file : {file_name}")
    try:
        ofile = open(file_name, 'r')
        print("Connection established...")
    except FileNotFoundError:
        print("File not found :(")
        return
    print()
    print("RECOVERED DATA:")
    print(ofile.read())
    print()
    ofile.close()
    print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
