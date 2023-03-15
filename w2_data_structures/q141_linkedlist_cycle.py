"""https://leetcode.com/problems/linked-list-cycle/
"""

# %%

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur1, cur2 = head, head

        while cur1 and cur2:
            cur1 = cur1.next 
            cur2 = cur2.next.next if cur2.next is not None else None
            if (cur1 and cur2) and (cur1 is cur2):
                return True

        return False
