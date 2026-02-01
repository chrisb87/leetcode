from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, arr: List):
        if not arr:
            return None
        dummy = cls(0)
        curr = dummy
        for val in arr:
            curr.next = cls(val)
            curr = curr.next
        return dummy.next

    def __to_list(self):
        vals = []
        curr = self
        while curr:
            vals.append(curr.val)
            curr = curr.next
        return vals

    def __repr__(self):
        return str(self.__to_list())
    
    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        return self.__to_list() == other.__to_list()


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev


def test_example_1():
    list = ListNode.from_list([1,2,3,4,5])
    expected = ListNode.from_list([5,4,3,2,1])
    assert Solution().reverseList(list) == expected


def test_example_2():
    list = ListNode.from_list([1,2])
    expected = ListNode.from_list([2,1])
    assert Solution().reverseList(list) == expected


def test_example_3():
    list = ListNode.from_list([])
    expected = ListNode.from_list([])
    assert Solution().reverseList(list) == expected
