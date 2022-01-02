"""
@Author : Pradeep Panchariya
@Email : panchariya11@gmail.com
"""

#We have to get the maximum item from the stack using o(1) running time complexity
#O(1) : running time complexity
#O(N) : space/memory complexity

class MaxStack:

    def __init__(self):
        self.main_stack = []
        self.max_stack = [] #to track the max item in the stack O(1)

    #inserting the item in the stack O(1)
    #size of the main and max stack should be the same . O(N)
    def push(self, data):
        self.main_stack.append(data)

        # if the main stack has one element then insert that element to the max_stack
        if self.size_main_stack()==1:
            self.max_stack.append(data)
        if data > self.max_stack[-1]:
            self.max_stack.append(data) # if the current element is greater then last then insert it
        else:
            self.max_stack.append(self.max_stack[-1])#if the current element is smaller then last element then keep the last element as the max

    #getting the size of the stack
    def pop(self):
        if is_empty():
            return -1
        self.max_stack.pop()
        return self.main_stack.pop()

    def size_main_stack(self):
        return len(self.main_stack)

    def is_empty(self):
        return self.main_stack==[]

    #O(1) : running time complexity
    def get_max_item(self):
        return self.max_stack.pop()

s = MaxStack()
s.push(34)
s.push(23)
s.push(12)
s.push(67)
s.push(2)
s.push(234)

print("max item: ", s.get_max_item())
# print(len(s.main_stack),len(s.max_stack))
