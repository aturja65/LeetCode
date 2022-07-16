# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        l=0
        temp=head
        while temp:
            l+=1
            temp=temp.next
        if l==n:
            head=head.next
            return head
        temp=head
        lt=0
        while temp:
            lt+=1
            if lt==l-n:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return head