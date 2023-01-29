# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        check, i, cur = {}, 0, head
        while cur:
            if cur in check:
                return True
            else:
                check[cur] = 1
            i += 1
            cur = cur.next
        return False
