"""
@Author : Pradeep Panchariya
@Email : panchariya11@gmail.com
"""

#Implementing the queue using the one single stack - Recursive method
class QueueUsingStackRecursion:

    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):

        #base case : pop the first element in the stack
        if len(self.queue)==1:
            return self.queue.pop()

        #getting the item
        item = self.queue.pop()

        #remove all the item
        recursive = self.dequeue()

        #append the item in the reverse order : queue FIFO
        self.queue.append(item)

        return self.queue.pop()


if __name__ == '__main__':
    Q = QueueUsingStackRecursion()
    for i in range(2,20,2):
        Q.enqueue(i)
    item = Q.dequeue()
    print(item)
