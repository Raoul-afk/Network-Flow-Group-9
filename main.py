import sys
from Input import edges, SOURCE, SINK
from Edmonds_karp import edmonds_karp
from Dinic import dinic

def main():
    # Usage: python main.py            -> runs both algorithms
    #        python main.py edmonds    -> runs Edmonds-Karp only
    #        python main.py dinic      -> runs Dinic only
    choice = sys.argv[1].lower() if len(sys.argv) > 1 else "all"

    print("=== Algorithm Execution ===")
    results = {}

    if choice in ("all", "edmonds", "edmonds-karp", "ek"):
        results["Edmonds-Karp"] = edmonds_karp(edges, SOURCE, SINK)
        print()

    if choice in ("all", "dinic"):
        results["Dinic"] = dinic(edges, SOURCE, SINK)
        print()

    if not results:
        print("Unknown algorithm. Use: edmonds | dinic (or no argument for both).")
        return

    if len(results) > 1:
        print("=== Comparison ===")
        for name, value in results.items():
            print(f"{name}: {value}")
        same = len(set(results.values())) == 1
        print("Both algorithms agree." if same else "WARNING: the results differ!")

if __name__ == "__main__":
    main()
