#Array interview question.

#1. Reversing the array In-Place
#time complexity - O(N) - In place reversing the array

def reverse_1(nums):
    L = nums
    print("Original list: ",L)
    temp=0
    for i in range(len(L)//2):
        L[i], L[-1-i] = L[-1-i], L[i] #this is shortcut assignment for swapping var in python

        # You can use this method also for swapping the variable
        # temp =L[i]
        # L[i] = L[-i-1]
        # L[-i-1] = temp
    return nums

def reverse_2(num):

    start_index = 0
    end_index = len(num)-1
    print("Original List: ",num)
    while end_index > start_index:
        num[start_index],num[end_index] = num[end_index], num[start_index]
        start_index+=1
        end_index-=1

    return num

if __name__ == '__main__':
    n = [1,2,3,4]
    print("Reversed list: ",reverse_1(n))
    n = [4,3,2,1]
    print("Reversed List: ",reverse_2(n))
