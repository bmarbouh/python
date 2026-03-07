#!/usr/bin/env python3

import importlib

pkg = {
    "pandas": "Data manipulation ready",
    "requests": "Network access ready",
    "matplotlib": "Visualization ready"
}


def check_lib():
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    lib = []
    missing = []
    try:
        for k,val in pkg.items():
            module = importlib.import_module(k)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {k} {version} - {val}")
        print("\nAnalyzing Matrix data...")
    except Exception as v:
        print(f"[KO] module not found :{v}")


check_lib()