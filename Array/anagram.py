#Check anagaram
#Running time complexity = O(Nlogn)+log(N)
def is_anagram(str1, str2):
    if len(str1)==len(str2) and sorted(str1)==sorted(str2):
        return True
    return False

if __name__ == '__main__':
    str1 = 'hello'
    str2 = 'ollhhe'
    print(is_anagram(str1,str2))
