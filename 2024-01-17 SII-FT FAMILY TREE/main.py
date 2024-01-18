# 9 reglas de producción en redes semánticas
# Se necesita:
#     * Categorización
#     * Nodos

from nodes_enum import Categorization

class Node:
    def __init__(self, name, left = None, right = None, left_w = None, right_w = None):
        self.name = name
        self.left = left
        self.right = right
        self.left_w = left_w  # w stands for weight
        self.right_w = right_w

class BinaryTree:
    def __init__(self, root = None):
        self.root = root

if __name__ == "__main__":
    print("Hi, world!")
