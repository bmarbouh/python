#!/usr/bin/env python3


def read_file():
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")
    print("")
    with open("classified_data.txt", "r") as file:
        print("SECURE EXTRACTION:")
        print(f"{file.read()}")


def write_file():
    print("SECURE PRESERVATION:")
    with open("security_protocols.txt", "w") as file:
        entry = "[CLASSIFIED] New security protocols archived"
        file.write(entry + "\n")
        print(entry)
    print("Vault automatically sealed upon completion")
    print("")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("")
    read_file()
    print("")
    write_file()
