from stack import Stack

# Class used for leaves of expression tree; represents a value.
class Leaf:
    def __init__(self, value):
        self.value = value

# Stores a left and right leaf, two operands, and an operator, given as character input.
# Also stores reference to parent node, which is None by default unless specified.
class Node:
    def __init__(self, operator: char, left: Leaf, right: Leaf, parent: Node = None):
        self.operator = operator
        self.left = left
        self.right = right
        self.parent = parent

class BinaryExpressionTree:
    def __init__(self):
        self.root = None
        self.stack = Stack()

