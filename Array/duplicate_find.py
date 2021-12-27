#finding duplicate in the Array
#O(N) - running time complexity

def duplicate(arr):
    rev=arr[::-1]
    for i in arr:
        if rev.index(i)+arr.index(i)!=len(arr)-1:
            return False
    return True

if __name__ == '__main__':
    s = [1,2,1,3,4]
    print(duplicate(s))
