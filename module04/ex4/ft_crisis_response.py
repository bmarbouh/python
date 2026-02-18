#!/usr/bin/env python3


def manage_file():
    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    try:
        with open("lost_archive.txt", "r") as file:
            pass
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    print("")
    print("CRISIS ALERT: Attempting access to 'corrupted_archive.txt'...")
    try:
        with open("corrupted_archive.txt", "r") as file:
            pass
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    print("")
    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    try:
        with open("standard_archive.txt", "r") as file:
            read_content = file.read()
            print(f"SUCCESS: Archive recovered - ``{read_content}''")
            print("STATUS: Normal operations resumed")
    except (FileNotFoundError, PermissionError):
        print("Semthing Went Wrong !!")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print("")
    manage_file()
