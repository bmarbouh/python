#!/usr/bin/env python3


def read_from_file():
    try:
        my_file = open("ancient_fragment.txt", "r")
        print("Accessing Storage Vault: ancient_fragment.txt")
        print("Connection established...")
        print("")
        print("RECOVERED DATA:")
        print(my_file.read())
        print("")
        my_file.close()
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("Error :File Not Found")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print("")
    read_from_file()
