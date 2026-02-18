#!/usr/bin/env python3
import sys
print("=== Command Quest ===")
args = sys.argv
if (len(args) <= 1):
    print("No arguments provided!")
    print("Program name:", args[0])
    print("Total arguments:", len(args))
else:
    print("Program name:", args[0])
    print("Arguments received:", len(args) - 1)
    count = 1
    while count < len(args):
        print(f"Argument {count}: {args[count]}")
        count += 1
    print("Total arguments:", len(args))
