# input.py : Définition du graphe orienté et des paramètres

SOURCE = "A"
SINK = "G"

# Liste des arcs orientés sous le format : (u, v, capacité)
# L'ordre dans le tuple définit strictement l'orientation : u -> v
edges = [
    ("A", "B", 7),
    ("A", "C", 6),
    ("A", "G", 5),
    ("A", "F", 10),
    ("B", "C", 5),
    ("B", "D", 7),
    ("B", "E", 9),
    ("C", "E", 9),
    ("C", "F", 7),
    ("D", "E", 5),
    ("E", "F", 5),
    ("F", "G", 6),
]