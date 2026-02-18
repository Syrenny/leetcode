from __future__ import annotations

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


class Solution:
    """LeetCode problem

    Link:
        https://leetcode.com/problems/merge-two-sorted-lists
    """

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        first = ListNode()
        last = first

        while list1 and list2:
            last.next = ListNode()
            last = last.next

            if list1.val < list2.val:
                last.val = list1.val
                list1 = list1.next
            else:
                last.val = list2.val
                list2 = list2.next

        if list1:
            last.next = list1
        elif list2:
            last.next = list2

        return first.next
