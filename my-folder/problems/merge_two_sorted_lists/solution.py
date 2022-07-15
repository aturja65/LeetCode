# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.head=self.tail=None
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1=list1
        temp2=list2
        a=[]
        b=[]
        while temp1:
            a.append(temp1.val)
            temp1=temp1.next
        while temp2:
            b.append(temp2.val)
            temp2=temp2.next
        a.extend(b)
        a.sort()
        for value in a:
            self.insert(value)
        return self.head
    
    def insert(self,value):
        new_l=ListNode(value)
        if self.head is None:
            self.head=self.tail=new_l
        else:
            self.tail.next=new_l
            self.tail=new_l
            