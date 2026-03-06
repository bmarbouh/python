#!/usr/bin/env python3

import sys
import os
import site

if sys.prefix == sys.base_prefix:
    print("\nMATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print(
        "python -m venv matrix_env\n"
        "source matrix_env/bin/activate # On Unix\n"
        "matrix_env\n"
        "Scripts\n"
        "activate   # On Windows\n"
    )
    print("Then run this program again.")
else:
    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.prefix}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {os.environ.get("VIRTUAL_ENV")}\n")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")
    print("Package installation path:")
    print(site.getsitepackages()[0])
