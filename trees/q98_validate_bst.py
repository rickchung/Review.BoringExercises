"""https://leetcode.com/problems/validate-binary-search-tree/
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    
    The right subtree of a node contains only nodes with keys greater than the node's key.
    
    Both the left and right subtrees must also be binary search trees.

For each node, there are two conditions:

(1) node.left.val < node.val < node.right.val
(2) max(left tree) < node.val < min(right tree)

Idea: a recursion function 

a. if not left < node < right:
    stop
b. find the max on the left
    if the max_left > the current
        stop
c. find the min on the right
    if the min_right < the current
        stop
d. return (cur, cur) (the current is the max on the left and min on the right)

"""
# %%

from typing import Optional, Tuple
from trees import TreeNode


class Solution:
    def __init__(self):
        self._min_val = -2**31 - 1
        self._max_val = 2**31 + 1
        self._is_bst = True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def _failed_case():
            self._is_bst = False
            return (self._max_val, self._min_val)

        def _none_case():
            return (self._min_val, self._max_val)

        def _check(node) -> Tuple[int, int]:
            if not node:
                return _none_case()

            min_left = self._max_val
            max_right = self._min_val

            min_left = min_right = self._max_val
            max_left = max_right = self._min_val

            if node.left:
                # Check the left leaf
                if node.left.val > node.val:
                    print("Left failed at node", node)
                    return _failed_case()
                min_left, max_left = _check(node.left)
                print(f"At {node.val}: {min_left} {max_left}")
                if max_left >= node.val:
                    print("Left failed at node due to max(left) > current", node)
                    return _failed_case()

            if node.right:
                # Check the right leaf
                if node.right.val < node.val:
                    print("Right failed at node", node)
                    return _failed_case()
                min_right, max_right = _check(node.right)
                print(f"At {node.val}: {min_right} {max_right}")
                if min_right <= node.val:
                    print("Right failed at node due to min(right) < current", node)
                    return _failed_case()
                
            print(f"Finally At {node.val} {min_left}, {max_left}, {min_right}, {max_right}")

            return (min(node.val, min_left, min_right), max(node.val, max_left, max_right))

        _check(root)

        return self._is_bst


# Solution().isValidBST(TreeNode.from_list([2, 1, 3]))
# Solution().isValidBST(TreeNode.from_list([5, 1, 4, None, None, 3, 6]))
# Solution().isValidBST(TreeNode.from_list([]))
# Solution().isValidBST(TreeNode.from_list([0, -1]))
# Solution().isValidBST(TreeNode.from_list([5, 4, 6, None, None, 3, 7]))
Solution().isValidBST(TreeNode.from_list([2, 2, 2]))
