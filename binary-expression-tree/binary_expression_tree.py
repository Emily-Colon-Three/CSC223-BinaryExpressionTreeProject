from stack import Stack

# Class used for leaves of expression tree; represents a value.
class _Leaf:
    def __init__(self, value):
        self._value = value

# Stores a left and right leaf, two operands, and an operator, given as character input.
# Also stores reference to parent node, which is None by default unless specified.
class _Node:
    def __init__(self, operator, left: _Leaf, right: _Leaf, parent: _Node = None):
        self.operator = operator
        self.left = left
        self.right = right
        self.parent = parent

# An outer shell which holds a node, avoiding exposing references and node data to client
# during traversal or other adjacent processes.
class Position:
    def __init__(self, container, node):
        self._container = container
        self._node = node

    def operator(self):
        return self._node.operator

class BinaryExpressionTree:
    def __init__(self):
        self._root = None
        self._stack = Stack()

