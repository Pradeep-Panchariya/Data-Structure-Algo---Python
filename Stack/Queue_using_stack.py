"""
@Author : Pradeep panchariya
@Email : panchariya11@gmail.com
"""

#FIFO : first item we insert will be the first we take out
class Queue_Using_Stack:

    def __init__(self):
        #use this stack for enquue operation
        self.enqueue_stack = []
        #use this stack for dequeue operation
        self.dequeue_stack = []

    def enqueue(self,data):
        self.enqueue_stack.append(data)

    def dequeue(self):
        #if both the stack are empty
        if len(self.enqueue_stack)==0 and len(self.dequeue_stack)==0:
            raise Exception("Stacks are empty...")

        # if the dequeue stack is empty then remove the item from enqueue top and insert in dequeue
        if len(self.dequeue_stack)==0:

            while len(self.enqueue_stack)!=0:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()

Q = Queue_Using_Stack()
for i in range(1,10):
    Q.enqueue(i)
print("enqueue: ",Q.enqueue_stack,end=", ")
for i in range(1,4):
    removed = Q.dequeue()
    print(r)
print("dequeue: ",Q.dequeue_stack,end=", ")
