"""LeetCode Problem 897 - Increasing Order Search Tree

Given the root of a binary search tree, rearrange the tree in in-order so that
the leftmost node in the tree is now the root of the tree, and every node has
no left child and only one right child.

Constraints
===========
 * The number of nodes in the given tree will be in the range [1, 100].
 * 0 <= Node.val <= 1000

"""

from typing import Generic, Optional, Text, TypeVar


# Define a type variable to create a generic stack.
T = TypeVar("T")


class Stack(Generic[T]):
    """Generic Stack"""
    def __init__(self) -> None:
        """Stack Constructor"""
        self._items = []
    
    def __bool__(self) -> bool:
        """Boolean representation of the stack.

        The stack returns True in a boolean context if and only if it has at
        least one item. If the stack is empty, it returns False.
        """
        return len(self._items) > 0
    
    def __str__(self) -> Text:
        """Return a textual representation of the stack."""
        return "[" + ", ".join(map(str, self._items)) + "]"
    
    def __repr__(self) -> Text:
        """Return a descriptive textual representation of the stack."""
        return f"Stack({self})"

    def peek(self) -> Optional[T]:
        """Peek

        See the topmost element in the stack without removing it, if there is
        one.
        """
        return self._items[-1] if self._items else None

    def pop(self) -> Optional[T]:
        """Remove the topmost item on the stack, if there is one."""
        return self._items.pop() if self._items else None
    
    def push(self, item: T) -> None:
        """Add an item to the stack."""
        self._items.append(item)


# Forward-declaration for static type-checking.
TreeNode = type("TreeNode")


class TreeNode:
    """Tree Node"""
    def __init__(self, value: int, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None) -> None:
        """Tree Node Constructor"""
        self.value = value
        self.left = left
        self.right = right
    
    def __str__(self) -> Text:
        """Return a text representation of this node's data."""
        return f"{self.value}"
    
    def __repr__(self) -> Text:
        """Return a descriptive text representation of this tree node."""
        return f"TreeNode({self})"


def add_node_to_stack(node: Optional[TreeNode], stack: Optional[Stack[TreeNode]] = None) -> Stack[TreeNode]:
    """Add Tree Node to Stack"""
    # If no stack was passed in, go ahead and create it. Otherwise, simply use
    # the one that was passed in.
    stack = stack if stack else Stack()

    # If the current node is not a valid node, simply return the current stack.
    if not node:
        return stack
    
    # Since the current node is a valid node, we will traverse its descendants
    # in post-order, adding them all to the stack. To begin, we will traverse
    # it's right subtree.
    stack = add_node_to_stack(node.right, stack)

    # Since this is a binary search tree, the node with the next highest value
    # after the right subtree is the current node, so add it to the stack.
    stack.push(node)

    # Finally, add all of the nodes in this node's left subtree to the stack.
    return add_node_to_stack(node.left, stack)


def increasing_bst(root: TreeNode) -> TreeNode:
    """Increasing Binary Search Tree

    Given the root of a binary search tree, rearrange the tree in in-order so
    that the leftmost node in the tree is now the root of the tree, and every
    node has no left child and only one right child.
    """
    # Create the stack in which the nodes will be temporarily placed.
    stack = add_node_to_stack(root)

    # Once all of the nodes in the tree have been added to the stack, we simply
    # need to pop the first node off the stack and use it as our new root, and
    # continue popping and appending nodes from the stack as the right children
    # of the current tree.
    #
    # In other words, when we pop a node from the stack, if we have no root
    # node yet, the popped node becomes our root node. If we do have a root
    # node, the popped node becomes the right child of our current node. The
    # right child of our current node then becomes our current node.
    #
    # Reset the root node variable to none until we re-initialize it with the
    # new root node.
    root = None

    # Define the current node iterator to keep track of where in the tree we
    # currently are. This iterator variable begins as a null value, since the
    # root node is also null.
    current_node = None

    # Continue iterating over the nodes in the stack while we have nodes in the
    # stack remaining.
    while stack:
        # Pop the topmost tree node from the stack.
        popped_node = stack.pop()

        # Check whether we need to initialize our root node before doing
        # anything else.
        if not root:
            # Initialize the root using the node we just popped off the stack.
            root = popped_node

            # Set the current node variable to the root node.
            current_node = root

            # Continue on with the rest of the nodes in the stack.
            continue
        
        # Add this node as the right child of the current node.
        current_node.right = popped_node

        # Zero out the left child of the current node.
        current_node.left = None

        # Finally, set the right child we just added to the current node as the
        # new current node.
        current_node = current_node.right

    # Zero out the left and right children of the last node we added to the
    # re-arranged tree.
    current_node.left = None
    current_node.right = None
    
    # Once we have finished adding all of the nodes in the stack to the new
    # tree, return the root node of the new tree.
    return root
