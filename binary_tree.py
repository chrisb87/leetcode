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
        def build_lines(node, level=0, prefix="root: "):
            if not node:
                return []
            
            lines = []

            # right appears above
            lines.extend(build_lines(node.right, level + 1, "/-- "))

            # current node in the middle
            indent = "    " * level
            lines.append(f"{indent}{prefix}{node.val}")

            # left appears below
            lines.extend(build_lines(node.left, level + 1, "\\-- "))

            return lines
        
        return "\n" + "\n".join(build_lines(self)) + "\n"

if __name__ == "__main__":
    input_data = [3, 9, 20, None, None, 15, 7]
    root = TreeNode.build(input_data)
    print(root)
