# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.head=self.tail=None
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans=[]
        for value in lists:
            temp=value
            while temp:
                ans.append(temp.val)
                temp=temp.next
        
        ans.sort()
        for value in ans:
            self.insert(value)
        return self.head
        
    def insert(self,value):
        new_l=ListNode(value)
        if self.head is None:
            self.head=self.tail=new_l
        else:
            self.tail.next=new_l
            self.tail=new_l