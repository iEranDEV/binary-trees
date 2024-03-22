from node import Node
import utils

"""
T = [8, 2, 5, 14, 1, 10, 12, 13, 6, 9]
tree = Node(T[0])
for i in range(1, len(T)):
    tree.insert(T[i])
print(tree.getHeight())
"""

loop = True
while loop:
    utils.menu("Wybierz typ drzewa", ["Drzewo AVL", "Losowe drzewo BST"])
