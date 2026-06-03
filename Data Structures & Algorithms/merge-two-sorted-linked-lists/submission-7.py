# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = list1
        curr2 = list2
        prev=None
        while curr and curr2:
            if not curr2:
                return list1
            if curr.val<= curr2.val:
                prev = curr
                curr=curr.next
            else:
                temp = curr2.next
                curr2.next =curr
                if prev:
                    prev.next= curr2
                if not prev:
                    list1 =curr2
                prev=curr2
                curr2=temp
        while curr2:
            if not prev:
                return list2
            prev.next=curr2
            prev = prev.next
            curr2 =curr2.next

        return list1