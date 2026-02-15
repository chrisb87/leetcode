from typing import Optional
from .binary_tree import TreeNode


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def dfs_helper(node: Optional[TreeNode], target: float, best_so_far: int, best_distance: float):
            if node is None:
                return best_so_far
            elif node.val == target:
                return node.val
            this_distance = abs(target - node.val)
            if this_distance == best_distance and node.val < best_so_far:
                best_so_far = node.val
            elif this_distance < best_distance:
                best_so_far = node.val
                best_distance = abs(target - node.val)
            if target < node.val:
                return dfs_helper(node.left, target, best_so_far, best_distance)
            elif target > node.val:
                return dfs_helper(node.right, target, best_so_far, best_distance)
        return dfs_helper(root, target, root.val, abs(target - root.val))


def test_example_1():
    root = TreeNode.build([4, 2, 5, 1, 3])
    target = 3.714286
    print(root)
    assert Solution().closestValue(root, target) == 4


def test_example_2():
    root = TreeNode.build([1])
    target = 4.428571
    assert Solution().closestValue(root, target) == 1


def test_failure_1():
    root = TreeNode.build([4, 2, 5, 1, 3])
    target = 3.5
    assert Solution().closestValue(root, target) == 3
