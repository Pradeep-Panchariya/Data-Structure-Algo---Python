'''
@Author : Pradee Panchariya
@Email : panchariya11@gmail.com
'''

#Traverse the linked List
#Time complexity : O(N)

#define the Node class
#It is as a container which will hold the data and ref of the any new node
#Represantation of this class

""" ________________
    |data|nextNode|
    ----------------
"""


class Node:
    def __init__(self,data):
        self.data = data
        self.nextNode = None

#define the linked list class for linking the newly node and do basic operations.

class LinkedList:

    def __init__(self):
        self.head = None

    #Traverse the Linked List and print the element.
    def traverse(self):

        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,end="-->")
                n = n.nextNode
            print()

    #O(N)/2 : O(N) Time compelxity
    #interiew question
    def get_middle_node(self):

        fast_node = self.head
        slow_node = self.head
        while fast_node.nextNode is not None and fast_node.nextNode.nextNode is not None:
            fast_node = fast_node.nextNode.nextNode
            slow_node = slow_node.nextNode
        return slow_node.data
    # O(1) - Time complexity
    def add_begin(self, data):
        new_node = Node(data) #Creating the new node
        new_node.nextNode = self.head #Pointing the head pointer to new node
        self.head = new_node# Poiniing the new node pointer to the head node

    # O(N) - Time complexity becaue of while loop - traverse all the linked list
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nextNode is not None:
                n = n.nextNode
            n.nextNode = new_node

    # O(N) : Time complexity
    def add_after(self,data, x):
         n = self.head
         while n is not None:
             if n.data == x:
                 break
             n = n.nextNode
         if n is None:
            print('X is not present',x)
         else:
            new_node = Node(data)
            new_node.nextNode = n.nextNode
            n.nextNode = new_node

    # O(N) : Running time complexity - while loop
    def add_before(self,data, x):
         if self.head is None:
             print("Linked list is empty")
         if self.head.data ==x:
             self.add_begin(data)
         else:

             n = self.head
             while n is not None:
                 if n.nextNode.data==x:
                     break
                 n = n.nextNode
             if n is None:
                 print("Not present")
             else:
                 new_node = Node(data)
                 new_node.nextNode = n.nextNode
                 n.nextNode = new_node

    # O(1)
    def remove_begin(self):
        if self.head is None:
            print("There are no Node")
        else:
            self.head = self.head.nextNode

    # O(N)
    def remove_end(self):
        if self.head is None:
            print("The LinkedList is empty")
        else:
            n = self.head
            while n.nextNode.nextNode is not None:
                n = n.nextNode
            n.nextNode = None

    # O(N)
    def remove_between(self, element):
        if self.head is None:
            print("LInked List is empty")
        if self.head.data == element:
            self.head = self.head.nextNode
        else:
            n = self.head
            while n is not None:
                if n.nextNode.data == element:
                    break
                n = n.nextNode
            if n is None:
                print("Element is not present in the linked list")
            else:
                n.nextNode = n.nextNode.nextNode

    #O(N) - Linear running Time
    #This method work same as remove_begin,remove_end,remove_between

    def remove(self, element):
        if self.head is None:
            print("Linked list is empty")
            return
        n  = self.head
        previous_node = None
        while n is not None and element !=n.data:
            previous_node = n
            n = n.nextNode
        if n is None:
            print("Element is not present in the list")
            return
        elif previous_node is None:
            self.head = n.nextNode
        else:
            previous_node.nextNode = n.nextNode






if __name__ == '__main__':
    L1  = LinkedList()
    print("Traverse the Linked List")
    L1.traverse()
    # print("Adding item at beginning")
    L1.add_begin(34)
    L1.add_begin(43)
    L1.add_begin(900)
    # print("adding item at the end ")
    L1.add_end(34)
    L1.add_end(555)
    # print("adding the item after the node")
    L1.add_after(12,43)
    # print("adding the item before the node")
    L1.add_before(66,34)
    L1.add_after(7,555)

    L1.traverse()
    print("remove the item at the beginning")

    L1.remove_begin()
    L1.traverse()
    print("remove the item at the end")
    L1.remove_end()
    L1.remove_end()
    L1.traverse()

    print("remove first element")
    L1.remove_between(66)
    L1.traverse()
    print("remove middle element")
    L1.remove_between(12)
    L1.add_end(656)

    L1.traverse()
    L1.remove(34)
    print("Remove the item")
    L1.traverse()

    L1.add_begin(121)
    L1.traverse()
    L1.add_begin(12971)
    L1.traverse()
#####Interview Question method added:
    middle_node = L1.get_middle_node()
    print("Middle Node: ",middle_node)
