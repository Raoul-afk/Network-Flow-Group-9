# Network input configuration

SOURCE = "S"
SINK = "T"

# List of directed edges formatted as: (u, v, capacity)
edges = [
    ("S", "A", 10),
    ("S", "B", 8),
    ("A", "B", 4),
    ("A", "C", 7),
    ("B", "C", 3),
    ("B", "D", 6),
    ("C", "D", 2),
    ("C", "T", 9),
    ("D", "T", 8),
]
