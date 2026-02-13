from typing import Optional
from .binary_tree import TreeNode


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return 0


def test_example_1():
    input_data = [3, 9, 20, None, None, 15, 7]
    root = TreeNode.build(input_data)
    assert Solution().minDepth(root) == 2


def test_example_2():
    input_data = [2, None, 3, None, 4, None, 5, None, 6]
    root = TreeNode.build(input_data)
    assert Solution().minDepth(root) == 5
