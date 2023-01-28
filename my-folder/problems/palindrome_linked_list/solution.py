# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ans, cur = [], head
        while cur:
            ans.append(cur.val)
            cur = cur.next
        return ans == ans[::-1]

        