"""
@Author : Pradeep Panchariya
@Email : panchariya11@gmail.com
"""

#Implementing the Queue data structure
#FIFO : First in First out
class Queue:

    def __init__(self):
        self.queue = []

    #Inserting the item to the queue
    #O(1)  : Running time complexity
    def enqueue(self, data):
        self.queue.append(data)

    #removing the item from the quueu and return the removed value : from beginning
    #O(N) : Running time complexity
    def dequeue(self):
        #checking whether quueu is empty or not to avoid exception
        if self.is_empty():
            return -1
        data = self.queue.pop(0) #
        return data

    #getting the current item from the queue
    #O(1) : running time complexity
    def peek(self):
        if self.is_empty():
            return -1
        return self.queue[0]

    #check whether queue  is empty or not
    #O(1)
    def is_empty(self):
        return self.queue == []

    #getting the size (total element) of the queue
    #O(1) : constant running time
    def size_queue(self):
        return len(self.queue)

    #print the queue
    def print_data(self):
        print(self.queue)

#initialize the queue object
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
#print
queue.print_data()
#getting the size
print(queue.size_queue())
#check whether empty or not True or False
print(queue.is_empty())
#removing the item
last_element = queue.dequeue()
#print again
queue.print_data()
#getting the last element
lst_ele = queue.peek()
