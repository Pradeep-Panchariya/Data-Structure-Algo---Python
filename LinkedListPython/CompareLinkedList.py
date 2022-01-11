class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LL(Node):
    def __init__(self):
        self.head = None 
        
    def insert_at_begin(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
    
    def compare_lists(llist2,llist1):
        llist1 = llist1.head
        llist2 = llist2.head
        while llist1 and llist2:#check while both the linked list is not empty
            if llist1.data != llist2.data:#check the data for both linked list
                return 0
            llist1 = llist1.next #going to the next node in llist1
            llist2 = llist2.next # goint to the next node in llist2
        if llist1 is None and llist2 is None:# if both the linked list is empty that mean data is matched perfectly so return 1
            return 1
        return 0 #else return 0
            
    
            
l1 = LL()
l1.insert_at_begin(2)
l1.insert_at_begin(1)
l2 = LL()
l2.insert_at_begin(2)
l2.insert_at_begin(1)
print(l1.compare_lists(l2))
