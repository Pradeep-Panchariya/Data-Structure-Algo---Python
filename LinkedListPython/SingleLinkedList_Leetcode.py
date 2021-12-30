'''
@Author : Pradee Panchariya
@Email : panchariya11@gmail.com
'''

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """

        if self.head is None:
            return -1
        if index==0:
            return self.head.data
        elif index > self.length-1 or index < 0:
            return -1
        else:
            ind = 0
            n = self.head
            while ind < self.length :
                # n=n.next
                if ind == index:
                    return n.data
                n = n.next
                ind+=1
        return -1



    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.length += 1
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.length+=1
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n= n.next
            n.next = new_node


    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.length:
            return -1
        if index == 0 :
            self.addAtHead(val)
            return
        elif index ==  self.length:
            self.addAtTail(val)
            return
        else:
            ind = 0
            n = self.head
            new_node = Node(val)
            while ind <= self.length:
                if ind == index-1:
                    self.length += 1
                    break
                n = n.next
                ind+=1
            new_node.next = n.next
            n.next = new_node






    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if self.head is None:
            return
        elif index > self.length-1 or index < 0:
            return
        elif index == 0:
            self.head = self.head.next
        else:
            ind = 0
            n = self.head
            while ind < self.length:
                if ind == index-1:
                    self.length -= 1
                    break
                n = n.next
                ind +=1
            n.next = n.next.next




obj = MyLinkedList()
# Your MyLinkedList object will be instantiated and called as such:
# x=["MyLinkedList","addAtHead","addAtIndex","get","addAtHead","addAtTail","get","addAtTail","get","addAtHead","get","addAtHead"]
# y=[[],[5],[1,2],[1],[6],[2],[3],[1],[5],[2],[2],[6]]
# for x,y in list(zip(x,y))[1:]:
#     if x=='get':
#         print(obj.x(y[0]))
#     elif x=='getAtIndex':
#         obj.x(y[0],y[1])
#     else:
#         obj.x(y[0])
#     obj.traverse()


# param_1 = obj.get(index)
obj.traverse()
obj.addAtHead(5)
print("len: ",obj.length)
obj.addAtIndex(1,2)
print("len: ",obj.length)
obj.traverse()
v = obj.get(1)
print(v)
obj.traverse()
obj.addAtHead(6)
print("len: ",obj.length)
obj.traverse()
obj.addAtTail(2)
print("len: ",obj.length)
obj.traverse()
v2 = obj.get(3)
print(v2)
obj.addAtTail(1)
print("len: ",obj.length)
obj.traverse()
print("len: ",obj.length)
v3 = obj.get(5)
print(v3)
obj.addAtHead(2)
obj.traverse()
v4 = obj.get(2)
print(v4)
obj.addAtHead(6)
obj.traverse()
print(obj.length)
