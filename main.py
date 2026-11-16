import sys
from Input import edges, SOURCE, SINK
from Edmonds_karp import  edmonds_karp

def main():
    print("=== Algorithm Execution ===")
    edmonds_karp(edges, SOURCE, SINK)
if __name__ == "__main__":
    main()
