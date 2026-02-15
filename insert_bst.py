from typing import Optional
from .binary_tree import TreeNode


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
        elif val < root.val:
            if root.left:
                root.left = self.insertIntoBST(root.left, val)
            else:
                root.left = TreeNode(val)
        elif val > root.val:
            if root.right:
                root.right = self.insertIntoBST(root.right, val)
            else:
                root.right = TreeNode(val)
        return root


def test_example_1():
    input_data = [4, 2, 7, 1, 3]
    val = 5
    root = TreeNode.build(input_data)
    new_root = Solution().insertIntoBST(root, val)
    assert [v for v in new_root] == [4, 2, 7, 1, 3, 5]


def test_failure_1():
    input_data = []
    val = 5
    root = TreeNode.build(input_data)
    new_root = Solution().insertIntoBST(root, val)
    assert [v for v in new_root] == [5]
