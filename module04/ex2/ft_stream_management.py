#!/usr/bin/env python3
import sys


def get_info():
    ar = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")
    print("")
    sys.stdout.write(f"[STANDARD] Archive status from {ar}: {status}\n")
    sys.stderr.write(
        "[ALERT] System diagnostic: Communication channels verified\n"
        )
    sys.stdout.write("[STANDARD] Data transmission complete\n")
    print("")
    sys.stdout.write("Three-channel communication test successful.\n")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    print("")
    get_info()
