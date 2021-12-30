
#Doubly linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    #traversing in the forward way begin to end : O(N)
    def traverse_forward(self):
        if self.head is None:
            print("Linked list is empty ")
            return
        n = self.head

        while n is not None:
            print(n.data,end="<--->")
            n = n.next
        print()

    #traversing from backward to start : reverse order : O(N)
    def traverse_backward(self):
        if self.head is None:
            print("Linked list is empty ")
            return
        n = self.head
        #traverse till the end so now n is pointing to the last node
        while n.next is not None:
            n=n.next
        #traverse from end to start while n.prev not become None
        while n is not None:
            print(n.data,end="<--->")
            n = n.prev
        print()

    #insert the item at the desired position
    #O(1)
    def insert_begin(self, data):

        #creting the new node
        self.length += 1
        new_node = Node(data)
        #if there are no node then head and tail will point to the new node
        if self.head is None :
            self.head = new_node
        # if there is at least one node presneted
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # O(N)
    def insert_end(self, data):

        self.length += 1
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
            new_node.prev = n

    #O(N)
    #inserting the new item before the index
    def insert_before(self, index, data):

        #if index is <0 or greater than legnth then return this message
        if index < 0 or index > self.length :
            print("Index is out of range\n")
            return
        # if the index is 0 then it will insert the new_node at the beginning
        if index == 0:
            self.insert_begin(data)
            return
        #if the index is equal to length of list then it will append the new node at the end
        elif index == self.length:
            self.insert_end(data)
            return
        else:
            new_node = Node(data)
            n = self.head
            self.length+=1
            for i in range(self.length):
                if i==index-1:
                    break
                n = n.next
                print(n.data)
            new_node.next = n.next
            n.next = new_node
            new_node.prev = n
            new_node.next.prev = new_node


    #insert the new node after the index
    def insert_after(self, index, data):
        self.insert_before(index+1,data)



if __name__ == '__main__':
    DoublyList = DoublyLinkedList()
    DoublyList.traverse_forward()
    print("Inserting at the beginning")
    DoublyList.insert_begin(45)
    DoublyList.insert_begin(53)
    DoublyList.insert_begin(123)
    DoublyList.traverse_forward()
    print("insert at the end")
    DoublyList.insert_end(324)
    DoublyList.insert_end(89)
    DoublyList.traverse_forward()
    print("\nTraversing the backward")
    DoublyList.traverse_backward()
    print("\nInsert between with index value")
    DoublyList.insert_before(2,"hello")
    DoublyList.traverse_forward()
    DoublyList.traverse_backward()
    DoublyList.insert_after(4,"Adam")
    DoublyList.traverse_forward()
    DoublyList.traverse_backward()
