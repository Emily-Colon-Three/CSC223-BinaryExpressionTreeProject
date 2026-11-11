from stack import Stack

# Can function as internal node or leaf, depending on whether left and right are None.
# Also stores reference to parent node, which is None by default unless specified.
class _Node:
    def __init__(self, element, parent: _Node = None):
        self.element = element
        self.parent = parent
        self.left = None
        self.right = None

# An outer shell which holds a node, avoiding exposing references and node data to client
# during traversal or other adjacent processes.
class Position:
    def __init__(self, container, node):
        self._container = container
        self._node = node

    def element(self):
        return self._node.element

"""An implementation of the Binary Tree data structure, which is built with a number of
protected and public methods included, as well as the _root and _stack data members. Uses 
Stack, Position, and _Node classes.
Protected methods include _make_position() and _validate(). The former creates a new
position in the tree, based of a node given through the parameter, and the latter checks
that a Position is valid, its container not being self and it being an instance of Position.
Then, root() returns root of tree, parent(p) returns parent of a position, left(p) returns
the left node for a position, and right(p) returns the right node. is_leaf(p) returns bool
value for whether a Position represents a leaf. add_root(e) adds a root to the tree of
element e, add_left() adds left node of element e to position p, and add_right() adds a
right node of element e to a position, and all three return ValueError if there already
exists a node in that spot."""
class BinaryExpressionTree:
    def __init__(self):
        self._root = None
        self._stack = Stack()

    # Creates a new Position which will hold node passed in as parameter. Returns the new
    # position, or None if node is None. Position's container is self.
    def _make_position(self, node):
        if node is not None:
            return self.Position(self, node)
        else:
            return None

    # Checks that parameter p is a Position object, and that the container of it is the
    # BinaryExpressionTree object. If either condition untrue, error is raised.
    # If validation successful, method returns the node held within the position.
    def _validate(self, p):
        if not isinstance(p, self.Position) or p._container is not self:
            raise ValueError("Position does not belong to tree.")
        return p._node

    # Returns root of BinaryExpressionTree.
    def root(self):
        return self._root

    # parent getter which uses Position wrapper class and validation logic, returning the
    # parent of parameter p, a Position object.
    def parent(self, p):
        return self._make_position(self._validate(p).parent)

    # Gets left node for position p, with validation, returning that left node's Position.
    def left(self, p):
        return self._make_position(self._validate(p).left)

    # Same as left(p), but for right node of p.
    def right(self, p):
        return self._make_position(self._validate(p).right)

    # Determines if Position p is for an internal node. True if node of p has no left
    # or right node references, False if it does.
    def is_leaf(self, p) -> bool:
        node = self._validate(p)
        return node.left is None and node.right is None

    # Adds a root for an empty BinaryExpressionTree, raising an error if not empty.
    # Creates a new node with element e
    def add_root(self, e):
        if self._root is not None:
            raise ValueError("Root already exists for tree.")

        self._root = self._Node(e)
        return self._root

    # Given Position p and Node e, adds a left node to p of element e.
    # Raises ValueError if left node already present for Position p. Validates p.
    def add_left(self, p, e):
        node = self._validate(p)
        if node.left is not None:
            raise ValueError("Left node already exists.")

        node.left = self._Node(e, node)
        return self._make_position(node.left)

    # Same as add_left, but for the right node of Position p.
    def add_right(self, p, e):
        node = self._validate(p)
        if node.right is not None:
            raise ValueError("Right node already exists.")

        node.right = self._Node(e, node)
        return self._make_position(node.right)

    # The method through which a Binary Expression Tree is constructed.
    # Takes postfix expression, processes it as tokens then builds a binary tree which
    # represents it. The expression must be valid, or error raised. Returns built tree.
    def build_tree(self, expression):
        tokens = expression.split()
        if len(tokens) == 0: # Validates input
            raise ValueError("Empty expression.")

        for token in tokens:
            if token.isdigit():
                subtree = BinaryExpressionTree()
                subtree.add_root(int(token)) # New subtree given root of token

            elif token is in "+-*/":
                if self._stack.size() < 2: # Operation needs two operands
                    raise ValueError("Too few operands.")
                # Most recent subtree made right tree, one just before made left
                right_tree = self._stack.pop()
                left_tree = self._stack.pop()

                subtree = BinaryExpressionTree() # subtree reset to new, empty tree
                subtree.add_root(token)
                # Operands joined to operator as children
                subtree.add_left(left_tree)
                subtree.add_right(right_tree)

                self._stack.push(subtree) # New subtree for operation added back to stack

            else:
                raise ValueError("Invalid expression: token does not exist.")

        # Stack is validated as having only one subtree left, before it is popped from stack and returned.
        if self._stack.size() != 1:
            raise ValueError("Too many operands.")
        return self._stack.pop()


# Testing
import unittest