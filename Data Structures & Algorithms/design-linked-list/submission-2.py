class ListNode:
    def __init__(self, val:int):
        self.val = val
        self.next=None
class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.size=0

    def getPrev(self, index:int) -> ListNode:
        count = 0
        curr= self.head.next
        while index - 1 > count:
            curr=curr.next
            count+=1
        return curr
        

    def get(self, index: int) -> int:
        curr=self.head.next
        
        
        if index > self.size-1:
            return -1
        else:
            node = self.getPrev(index)
        
        return node.next.val
            
            


        

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head.next
        self.head.next = node
        self.size +=1
        

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
        

        

    def addAtIndex(self, index: int, val: int) -> None:
        node = ListNode(val)
        curr=self.head.next
        if index > self.size:
            pass
            
        else: 
            prev = self.getPrev(index)
            curr = prev.next
            prev.next =node
            node.next=curr
            self.size +=1
            
        
            

        

    def deleteAtIndex(self, index: int) -> None:
        count =0
        curr = self.head.next
        if index>= self.size:
            pass
        else:
            prev = self.getPrev(index)
            curr= prev.next
            prev.next=curr.next
            curr.next=None
            self.size-=1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)