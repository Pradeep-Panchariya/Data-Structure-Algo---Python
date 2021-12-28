# Insertion and deletion in the linked list : O(1) constant Time complexity
#For accessing the arbitary element : O(N) running time complexity (Linear).

#Insert itema at beginning : O(1)  vs array O(N)
#remove item at the beginning : O(1) vs array O(N)
#Insert item at the end of the linked list : O(N) vs array O(1)
#To remove item at the arbitary location : O(N) vs array O(N)

#Conclusion
# Manipulate the first item (add or remove)
# O(1)

# Manipulating arbitary item:
# O(N)

################

-------------------------------------
          Linked list  | Array      |
-----------------------|------------|
searchIndex | O(N)     | O(1)       |
insertBegin | O(1)     | O(N)       |
insertEnd   | O(N)     | O(1)       |
waste space | O(N)     | 0          |
look item   | O(N)     | O(N)       |
------------------------------------|
