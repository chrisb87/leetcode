from collections import deque
from typing import Optional
from .binary_tree import TreeNode


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])

        while queue:
            len_current_level = len(queue)
            sum_current_level = 0

            for _ in range(len_current_level):
                node = queue.popleft()
                sum_current_level += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if len(queue) == 0:
                return sum_current_level


def test_example_1():
    input_data = [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8]
    root = TreeNode.build(input_data)
    assert Solution().deepestLeavesSum(root) == 15


def test_example_2():
    input_data = [6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5]
    root = TreeNode.build(input_data)
    assert Solution().deepestLeavesSum(root) == 19
