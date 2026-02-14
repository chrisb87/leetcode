from typing import Optional
from .binary_tree import TreeNode


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], treeMin: int, treeMax: int) -> int:
            if node is None:
                return treeMax - treeMin
            treeMin = min(node.val, treeMin)
            treeMax = max(node.val, treeMax)
            left = dfs(node.left, treeMin, treeMax)
            right = dfs(node.right, treeMin, treeMax)
            return max(left, right)
        return dfs(root, root.val, root.val)


def test_example_1():
    input_data = [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]
    root = TreeNode.build(input_data)
    assert Solution().maxAncestorDiff(root) == 7


def test_example_2():
    input_data = [1, None, 2, None, 0, 3]
    root = TreeNode.build(input_data)
    assert Solution().maxAncestorDiff(root) == 3
