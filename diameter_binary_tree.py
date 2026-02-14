from typing import Optional
from .binary_tree import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self._diameter = -1
        self.maxEdges(root)
        return self._diameter

    def maxEdges(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        left_max_edges = self.maxEdges(root.left)
        right_max_edges = self.maxEdges(root.right)
        self._diameter = max(
            self._diameter, left_max_edges + right_max_edges + 2)
        return max(left_max_edges, right_max_edges) + 1


def test_example_1():
    input_data = [1, 2, 3, 4, 5]
    root = TreeNode.build(input_data)
    assert Solution().diameterOfBinaryTree(root) == 3


def test_example_2():
    input_data = [1, 2]
    root = TreeNode.build(input_data)
    assert Solution().diameterOfBinaryTree(root) == 1
