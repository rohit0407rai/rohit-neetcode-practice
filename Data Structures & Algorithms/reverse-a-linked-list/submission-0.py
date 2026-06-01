# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        arr=[]
        newLL=ListNode(0)
        cr = newLL
        while curr:
            arr.append(curr.val)
            curr=curr.next
        arr.reverse()
        for i in arr:
            cr.next= ListNode(i)
            cr=cr.next
        return newLL.next
            
    

        