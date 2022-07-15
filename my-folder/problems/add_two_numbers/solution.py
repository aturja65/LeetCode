# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.head=self.tail=None
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a=[]
        b=[]
        temp1=l1
        temp2=l2
        while temp1:
            a.append(temp1.val)
            temp1=temp1.next
        while temp2:
            b.append(temp2.val)
            temp2=temp2.next
        a.reverse()
        b.reverse()
        num1=0
        num2=0
        for value in a:
            num1=(num1*10)+value
        for value in b:
            num2=(num2*10)+value
        del a
        del b
        res=str(num1+num2)
        res=res[::-1]
        ans=[int(value)for value in res]
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