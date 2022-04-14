"""LeetCode Problem 700 - Search in a Binary Search Tree

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the
subtree rooted with that node. If such a node does not exist, return null.

Constraints
===========
 * The number of nodes in the tree is in the range [1, 5000].
 * 1 <= Node.val <= 10^7
 * root is a binary search tree.
 * 1 <= val <= 10^7

"""

from typing import Optional


class TreeNode:
    """Binary Search Tree Node"""
    def __init__(self, value: int, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = value
        self.left = left
        self.right = right


def search_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """Search Binary Search Tree"""
    # Since this is a recursive routine, check for the degenerate case where a
    # subtree (or even the root node itself) contains a null pointer.
    if not root:
        # If the root node pointer is null, then this subtree does not contain
        # the value.
        return None
    
    # Having checked for a potential null pointer, we may now check the value
    # of this node without having to worry about triggering a segmentation
    # fault from dereferencing a null pointer (or whatever happens in Python).
    if root.val == val:
        # If the root node of this subtree contains the value we are looking
        # for, we're done looking. We can now simply return this subtree.
        return root
    
    # This is a binary search tree, so if the value is less than the value of
    # this node, it's either in the left subtree, or it isn't in this tree at
    # all.
    if val < root.val and root.left:
        # If the value we're looking for is less than the value of this node,
        # search the left subtree.
        subtree = search_bst(root.left, val)

        # If we get a null pointer back from the function call, the value is
        # not in this tree.
        if subtree is not None:
            # If the subtree node is a valid pointer, we've found the target
            # subtree, and we can simply return it.
            return subtree
    
    # If the value is greater than the value of this node, search the right
    # subtree.
    if root.val < val and root.right:
        # Recurse into the right subtree, passing in the value we are looking
        # for.
        subtree = search_bst(root.right, val)

        # Make sure we didn't get a null pointer back from the function call
        # above.
        if subtree is not None:
            # If we got a valid pointer, we've found the subtree, and we can
            # now simply return it.
            return subtree

    # If none of the branches above yielded a return statement until now, this
    # subtree does not contain the target value.
    return None
