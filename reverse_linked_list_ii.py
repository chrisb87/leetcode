# Given the head of a singly linked list 
# and two integers left and right where left <= right, 
# reverse the nodes of the list from position left to position right, 
# and return the reversed list.

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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = None
        curr = head
        dummy_head = ListNode()
        end_of_beginning = dummy_head
        dummy_head.next = curr
        i = 1

        while curr and i < left:
            
            prev = curr
            end_of_beginning = curr
            curr = curr.next
            i += 1

        if not curr:
            return dummy_head.next

        end_of_reversed_section = curr

        while curr and i <= right:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            i += 1

        beginning_of_reversed_section = prev
        end_of_beginning.next = beginning_of_reversed_section
        end_of_reversed_section.next = curr
        return dummy_head.next


def test_example_1():
    list = ListNode.from_list([1,2,3,4,5])
    left = 2
    right = 4
    expected = ListNode.from_list([1,4,3,2,5])
    assert Solution().reverseBetween(list, left, right) == expected


def test_example_2():
    list = ListNode.from_list([5])
    left = 1
    right = 1
    expected = ListNode.from_list([5])
    assert Solution().reverseBetween(list, left, right) == expected


def test_simple_reverse():
    list = ListNode.from_list([1,2,3,4,5])
    left = 1
    right = 5
    expected = ListNode.from_list([5,4,3,2,1])
    assert Solution().reverseBetween(list, left, right) == expected


def test_failure_1():
    list = ListNode.from_list([3,5])
    left = 1
    right = 1
    expected = ListNode.from_list([3,5])
    assert Solution().reverseBetween(list, left, right) == expected


def test_failure_2():
    list = ListNode.from_list([3,5])
    left = 2
    right = 2
    expected = ListNode.from_list([3,5])
    assert Solution().reverseBetween(list, left, right) == expected


def test_failure_3():
    list = ListNode.from_list([1,2,3])
    left = 3
    right = 3
    expected = ListNode.from_list([1,2,3])
    assert Solution().reverseBetween(list, left, right) == expected
