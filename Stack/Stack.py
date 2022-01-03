"""
@Author : Pradeep Panchariya
@Email : panchariya11@gmail.com
"""

#Implementing the stack data structure
#LIFO : Last in first out
class Stack:

    def __init__(self):
        self.stack = []

    #Inserting the item to the stack : at the end
    #O(1)  : Running time complexity
    def push(self, data):
        self.stack.append(data)

    #removing the item from the stack and return the removed value : at the end
    #O(1) : Running time complexity
    def pop(self):
        #checking whether stack is empty or not to avoid exception
        if self.is_empty():
            return -1
        data = self.stack.pop() # self.stack[-1] also valid to use
        return data

    #getting the last item from the stack
    #O(1) : running time complexity
    def peek(self):
        if self.is_empty():
            return -1
        return self.stack[-1]

    #check whether stack is empty or not
    #O(1)
    def is_empty(self):
        return self.stack == []

    #getting the size (total element) of the stack
    #O(1) : constant running time
    def size_stack(self):
        return len(self.stack)

    #print the Stack
    def print_data(self):
        print(self.stack)

if __name__ == '__main__':
    #initialize the stack object
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    #print
    stack.print_data()
    #getting the size
    print(stack.size_stack())
    #check whether empty or not True or False
    print(stack.is_empty())
    #removing the item
    last_element = stack.pop()
    #print again
    stack.print_data()
    #getting the last element
    lst_ele = stack.peek()
