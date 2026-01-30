from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


def test_example_1():
    five = ListNode(5)
    four = ListNode(4, five)
    three = ListNode(3, four)
    two = ListNode(2, three)
    one = ListNode(1, two)
    assert Solution().middleNode(one) == three

def test_example_2():
    six = ListNode(6)
    five = ListNode(5, six)
    four = ListNode(4, five)
    three = ListNode(3, four)
    two = ListNode(2, three)
    one = ListNode(1, two)
    assert Solution().middleNode(one) == four
