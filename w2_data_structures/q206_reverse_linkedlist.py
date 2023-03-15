"""https://leetcode.com/problems/reverse-linked-list/
"""

# %%

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self) -> str:
        nums = [self.val]
        cur = self.next
        while cur:
            nums.append(cur.val)
            cur = cur.next
        return str(nums)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        
        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next
        
        head = ListNode(nums[-1])
        cur = head
        for i in range(len(nums) - 2, -1, -1):
            cur.next = ListNode(nums[i])
            cur = cur.next

        return head


nums = [1, 2, 3, 4, 5]
nums = [1, 2]

head = ListNode(nums[0])
cur = head
for i in nums[1:]:
    cur.next = ListNode(i)
    cur = cur.next

s = Solution()
print(s.reverseList(head))
