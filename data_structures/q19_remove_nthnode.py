"""https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

# %%

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        stack = []
        cur = head
        while cur is not None:
            stack.append(cur)
            cur = cur.next

        cp = len(stack) - n
        cp_prev = cp - 1
        stack[cp_prev].next = stack[cp].next
        stack.pop(cp)
        
        return stack[0]
    
