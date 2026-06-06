class ListNode:
    def __init__(self, val:int):
        self.val = val
        self.next=None
class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.size=0
        

    def get(self, index: int) -> int:
        curr=self.head.next
        count =0
        while curr:
            if count ==index:
                return curr.val
            count+=1
            curr=curr.next
            
        return -1


        

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head.next
        self.head.next = node
        self.size +=1
        

    def addAtTail(self, val: int) -> None:
        node =  ListNode(val)
        curr = self.head
        while curr.next:
            curr=curr.next
        curr.next = node
        self.size+=1
        

        

    def addAtIndex(self, index: int, val: int) -> None:
        node = ListNode(val)
        curr=self.head.next
        prev=None

        count = 0
        if index == self.size:
            self.addAtTail(val)
        elif index > self.size:
            pass
            
        else: 
            while index > count:
                prev=curr
                curr=curr.next
                count+=1
            prev.next = node
            node.next = curr
            self.size +=1
            
        
            

        

    def deleteAtIndex(self, index: int) -> None:
        count =0
        curr = self.head.next
        if index>= self.size:
            pass
        else:
            while index > count:
                prev=curr
                curr=curr.next
                count+=1
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