# You are given an absolute path for a Unix-style file system, 
# which always begins with a slash '/'. 
# Your task is to transform this absolute path into its simplified canonical path.
#
# The rules of a Unix-style file system are as follows:
#
#     A single period '.' represents the current directory.
#     A double period '..' represents the previous/parent directory.
#     Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
#     Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
#
# The simplified canonical path should follow these rules:
#
#     The path must start with a single slash '/'.
#     Directories within the path must be separated by exactly one slash '/'.
#     The path must not end with a slash '/', unless it is the root directory.
#     The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.



class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = ['/']

        for c in path:
            stack.append(c)

            if stack[-2:] == ['/', '/']:
                stack.pop()
            elif stack[-4:] == ['/', '.', '.', '/']:
                for _ in range(4):
                    stack.pop()
                while stack and stack[-1] != '/':
                    stack.pop()
                if not stack:
                    stack = ['/']
            elif stack[-3:] == ['/', '.', '/']:
                for _ in range(2):
                    stack.pop()

        if len(stack) > 1 and stack[-1] == '/':
            stack.pop()

        return ''.join(stack)


def test_example_1():
    path = "/home/"
    expected = "/home"
    assert Solution().simplifyPath(path) == expected

def test_example_2():
    path = "/home//foo/"
    expected = "/home/foo"
    assert Solution().simplifyPath(path) == expected

def test_example_3():
    path = "/home/user/Documents/../Pictures"
    expected = "/home/user/Pictures"
    assert Solution().simplifyPath(path) == expected

def test_example_4():
    path = "/../"
    expected = "/"
    assert Solution().simplifyPath(path) == expected

def test_example_5():
    path = "/.../a/../b/c/../d/./"
    expected = "/.../b/d"
    assert Solution().simplifyPath(path) == expected
