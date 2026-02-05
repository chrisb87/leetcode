# You are given an absolute path for a Unix-style file system, 
# which always begins with a slash '/'. 
# Your task is to transform this absolute path into its simplified canonical path.

class Solution:
    def simplifyPath(self, path: str) -> str:
        return path


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
