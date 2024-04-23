
class Node:

    def __init__(self, val=0, next=None):
        # self.head = None
        # self.size = 0
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        # self.size = 0
        # self.val = 0
        # self.next = None
    
    def main(self):
        node = MyLinkedList()
        node.addAtTail(2)
        node.print()
        
        
    def addAtTail(self, val: int) -> None:
        # newNode = ListNode(val)
        #if list is empty
        
        if self.head is None:
            self.head = Node(val)
            
        else:
            # inserting at end
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(val)
            # self.size+=1
        
        
    def print(self):
        # n = self.size
        # for i in range(n):
        node = self.head
        while node != None:
            print(node.val)
            node = node.next

    
        
