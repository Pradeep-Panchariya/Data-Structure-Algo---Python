"""
@Author: Pradeep Panchariya
@Email : panchariya11@gmail.com
"""

#Reverse a singly linked list In - Place
#O(1) : Space complexity
#O(N) : Running time complexity

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ReverseInPlace:

    def __init__(self):
        self.head = None

    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    #Traverse the linked list
    def traverse(self):
        n = self.head
        while n is not None:
            print(n.data,end="-->")
            n = n.next
        print()
    #reverse it
    def reverse(self):
        n = self.head
        prev = None
        while n is not None:
            nxt = n.next
            n.next = prev
            prev = n
            n = nxt
        self.head = prev


if __name__ == '__main__':
    LL = ReverseInPlace()
    for i in range(2,10):
        LL.add_begin(i)
    LL.traverse()
    LL.reverse()
    LL.traverse()
