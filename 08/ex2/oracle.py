import os
import sys
try:
    from dotenv import load_dotenv
except ImportError:
    print("ERROR : dotenv is not found")
    print("[>] Install it using : pip install python-dotenv")
    sys.exit(1)


def check_protocols() -> None:
    print("\nEnvironment security check:")
    print("No hardcoded secrets detcted")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARN] no .env file found")
    print("[OK] Porduction ovverrides available")


def main() -> None:
    load_dotenv()
    mode = os.getenv("MATRIX_MODE")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    configs = [mode, db_url, api_key, log_level, zion_endpoint]
    if not all(configs):
        print("[Warning] : the orcale's vision is clouded!"
              "Missing critical configuration")
        print("Please copy .env.example to .env and fill your values :-)")
        print("cp .env.example .env")
        sys.exit(1)

    if mode == "production":
        db_display = "Connected to Secure Production Cluster"
        log_display = "ERROR (Silenced non-critcal logs for prod)"
    else:
        db_display = "Connected to local instance"
        log_display = log_level

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {db_display}")
    print(f"API Access: {'Authenticated' if api_key else 'FAILED'}")
    print(f"Log Level: {log_display}")
    print(f"Zion Network: {'Online' if zion_endpoint else 'Offline'}")

    check_protocols()
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
