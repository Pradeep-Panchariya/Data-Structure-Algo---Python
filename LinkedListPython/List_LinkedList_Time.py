'''
@Author : Pradee Panchariya
@Email : panchariya11@gmail.com
'''

from LinkedListProgram import LinkedList
import time

#current time
now = time.time()

#inserting the 500000 item at the begin in the linked list . O(1)
for i in range(500000):
    LinkedList().add_begin(i)

print(f'Linked List Running time (In second) : {time.time()-now}')


now = time.time()
lst = []

for i in range(500000):
    lst.insert(0,i)

print(f'List Running time (In second) : {time.time()-now}')


#Output on my pc
'''
Linked List Running time (In second) : 1.4874837398529053
List Running time (In second) : 222.28053498268127
'''
