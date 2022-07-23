from turtle import right


def isPalindrome(word:str):

    leftPointer = 0
    rightPointer = len(word) - 1

    for i in range(0,len(word)//2):
        if not word[i] == word[rightPointer - i]:
            return False
    
    return True      

print(isPalindrome("anitalavalatina"))
print(isPalindrome("anma"))    