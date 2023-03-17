"""https://leetcode.com/problems/invert-binary-tree/

Given the root of a binary tree, invert the tree, and return its root.

function flip(node):
    if not node:
        return
    
    Flip the left and right child nodes
    
    flip(left)
    flip(right)

For each node in the tree,
    flip(node)
    

"""
# %%

from typing import Optional
from trees import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def _flip(node):
            if not node:
                return
            node.left, node.right = node.right, node.left
            _flip(node.left)
            _flip(node.right)

        _flip(root)

        return root


# Solution().invertTree(TreeNode.from_list([4, 2, 7, 1, 3, 6, 9])).get_bfs()
# Solution().invertTree(TreeNode.from_list([2, 3, 1])).get_bfs()
Solution().invertTree(None)
