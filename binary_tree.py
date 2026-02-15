from collections import deque
from typing import Optional


class TreeNode:
    @classmethod
    def build(cls, nodes: Optional[list] = None):
        if not nodes or nodes[0] == None:
            return None

        root = TreeNode(nodes[0])
        queue = deque([root])

        i = 1
        while queue and i < len(nodes):
            current = queue.popleft()

            # left
            if nodes[i] is not None:
                current.left = TreeNode(nodes[i])
                queue.append(current.left)

            i += 1
            if i >= len(nodes):
                continue

            # right
            if nodes[i] is not None:
                current.right = TreeNode(nodes[i])
                queue.append(current.right)

            i += 1

        return root

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        def build_lines(node, prefix="", is_left=True):
            if not node:
                return []

            lines = []
            lines.extend(build_lines(node.right, prefix +
                         ("│   " if is_left else "    "), False))
            lines.append(
                prefix + ("└── " if is_left else "┌── ") + str(node.val))
            lines.extend(build_lines(node.left, prefix +
                         ("    " if is_left else "│   "), True))
            return lines

        return "\n" + "\n".join(build_lines(self)) + "\n"

    def __iter__(self):
        return TreeIterator(self)


class TreeIterator:
    def __init__(self, root):
        self.queue = deque([root])

    def __iter__(self):
        return self

    def __next__(self):
        if not self.queue:
            raise StopIteration()
        node = self.queue.popleft()
        if node.left:
            self.queue.append(node.left)
        if node.right:
            self.queue.append(node.right)
        return node.val


if __name__ == "__main__":
    input_data = [3, 9, 20, None, None, 15, 7]
    root = TreeNode.build(input_data)
    print(root)
    print([v for v in root])
