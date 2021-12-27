# Accessing the array/list element is O(1) running time.
#Searching the element in the array also takes O(N) running time complexity.
L = [1,2,3,4,5]
print(L[2])#O(1) - constent time for accessing element in the arry/list

#for appending and removing the last element in the array/list also has the O(1) constant time.
L.append(55)#O(1) - adding the last element
print(L)

L.pop()#O(1) - removing the last element
print(L)

#O(N) - it takes linear running time because we have to shift the array while adding and filling the holes while removing the array.
#If inserting/removing the arbitary element it takes O(N) Linear Time.
L.insert(1,45)#insert(index,element to be added) - O(N) - Linear time complexity.
print(L)

L.remove(4)#removing the element 4 from the List L - O(N) - Linear time complexity.
print(L)

L.pop(2)# removing the element from the index 2 . O(N) - Linear time complexity.
print(L)
