#check if string is a palindrome or not
#O(N) running time complexity
def check_palindrome(string):
    stirng = string.lower()
    start_index=0
    end_index = len(string)-1
    while start_index<end_index:
        if string[start_index]!=string[end_index]:
            return "String are not palindrome"
        start_index+=1
        end_index-=1
    return "String are palindrome"

if __name__ == '__main__':
    string = 'madams'
    print(check_palindrome(string))
