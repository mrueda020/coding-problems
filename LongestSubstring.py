
#ffffgggthyu

def longestSubstring(string: str):
    maxLength = 0
    leftPointer = 0
    rightPointer = 0

    m = {}
    strLength = len(string)
    while(leftPointer < strLength and rightPointer < strLength):
        currentChar = string[rightPointer]
        if currentChar in m:
            leftPointer = max(leftPointer, m[rightPointer] + 1)
        m[currentChar] = rightPointer
        maxLength = max(maxLength, rightPointer - leftPointer + 1)
        rightPointer+=1
    return maxLength    