class ListNode:
    def __init__(self, val:int, next=None, prev =None):
        self.val = val
        self.next = next
        self.prev = prev
        
class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def getPrev(self, index:int)->ListNode:
        
        if index <= self.size/2:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            return curr
        else: 
            curr = self.tail
            for _ in range(self.size - index+1):
                curr = curr.prev
            return curr

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        return self.getPrev(index).next.val
    
    

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)
        

        

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        
        if index > self.size:
            return -1
        else:
            node = ListNode(val)
            prev = self.getPrev(index)
            next = prev.next
            prev.next = node
            next.prev = node
            node.next= next
            node.prev = prev
            self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return 
        else:
            prev = self.getPrev(index)
            next = prev.next.next
            prev.next = next
            next.prev = prev
            self.size-=1

            

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)