from collections import deque
from typing import Optional, List
from .binary_tree import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        answer = []
        queue = deque([root])
        reverse_row = False

        while len(queue) > 0:
            row_count = len(queue)
            row = []

            for _ in range(row_count):
                node = queue.popleft()
                row.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if reverse_row:
                row = reversed(row)

            answer.append(list(row))
            reverse_row = not reverse_row

        return answer


def test_example_1():
    input_data = [3, 9, 20, None, None, 15, 7]
    root = TreeNode.build(input_data)
    assert Solution().zigzagLevelOrder(root) == [[3], [20, 9], [15, 7]]


def test_example_2():
    input_data = [1]
    root = TreeNode.build(input_data)
    assert Solution().zigzagLevelOrder(root) == [[1]]


def test_example_3():
    input_data = []
    root = TreeNode.build(input_data)
    assert Solution().zigzagLevelOrder(root) == []
