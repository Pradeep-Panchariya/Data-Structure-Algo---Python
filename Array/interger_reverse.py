#reverse the integer
#O(N) - running time complexity

def reverse_integer(num):
    reverse = 0
    while num !=0:
        rem =  num%10
        reverse = reverse *10 +rem
        num//=10

    return reverse

if __name__ == '__main__':
    n = 123456780
    print(reverse_integer(n))
