#!/usr/bin/env python3
def create_file():
    my_file = open("new_discovery.txt", "w")
    print("Initializing new storage unit: new_discovery.txt")
    my_file.write("[ENTRY 001] New quantum algorithm discoveredl\n")
    my_file.write("[ENTRY 002] Efficiency increased by 347%\n")
    my_file.write("[ENTRY 003] Archived by Data Archivist trainee\n")
    print("Storage unit created successfully...")
    my_file.close()


def read_file():
    try:
        r_file = open("new_discovery.txt", "r")
        print("Inscribing preservation data...")
        print(r_file.read())
        print("")
        print("Data inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
        r_file.close()
    except FileNotFoundError:
        print("Error :File Not found")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print("")
    create_file()
    print("")
    read_file()
