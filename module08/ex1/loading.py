#!/usr/bin/env python3

import importlib

pkg = {
    "pandas": "Data manipulation ready",
    "requests": "Network access ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready"
}


def check_lib() -> dict:
    """
    Check that all required packages are installed
    and return a dict of loaded modules.
    """
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    lib = {}
    missing = []
    for k, val in pkg.items():
        try:
            module = importlib.import_module(k)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {k} {version} - {val}")
            lib[k] = module
        except Exception as v:
            print(f"[KO] :{v}")
            missing.append(k)
    if missing:
        print(
            "you need to instaall all packges using:\n"
            "pip install -r requirements.txt\n"
            "or\n"
            "poetry install\n"
        )
        exit(1)
    return lib


def main() -> None:
    """
    Generate random data, compute value distribution,
    and save a bar chart.
    """
    md = check_lib()
    numpy = md["numpy"]
    pandas = md["pandas"]
    d = numpy.random.randint(0, 101, size=1000)
    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")
    df = pandas.DataFrame({"signal": d})
    plt = importlib.import_module("matplotlib.pyplot")
    print("\nGenerating visualization...")
    plt.hist(df['signal'], bins=20)
    plt.title("Matrix Signal Distribution")
    plt.xlabel("Signal Value")
    plt.ylabel("Frequency")
    plt.savefig("matrix_analysis.png")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
