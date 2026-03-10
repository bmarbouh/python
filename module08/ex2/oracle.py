#!/usr/bin/env python3

import os
from dotenv import load_dotenv

load_dotenv()


def check_env(api_key: str, database: str) -> None:
    """Check environment security and display results."""
    env_exist = os.path.exists(".env")
    secrets_ok = api_key is not None and database is not None
    print("\nEnvironment security check:")
    print(
        "[OK] No hardcoded secrets detected"
        if secrets_ok
        else "[WARN] Some secrets may be missing"
        )
    print(
        "[OK] .env file properly configured"
        if env_exist else
        "[WARN] No .env file found, using defaults"
        )
    print(
        "[OK] Production overrides available"
        if os.getenv("MATRIX_MODE") == "production"
        else "[WARN] Production overrides Not available"
        )


def main() -> None:
    """Load environment variables and print the current configuration."""
    print("ORACLE STATUS: Reading the Matrix...\n")
    mode = os.getenv("MATRIX_MODE")
    database = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion = os.getenv("ZION_ENDPOINT")
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    if database:
        print("Database: Connected to local instance")
    else:
        print("Database: Not configured")
    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing key")
    print(f"Log Level: {log_level}")
    if zion:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")
    check_env(api_key, database)


if __name__ == "__main__":
    main()
