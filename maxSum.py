def maxSum(array:list, windowSize:int):
    if len(array) <= windowSize:
        return -1

    windowSum = sum(array[i] for i in range(windowSize))
    maxSum = windowSum

    for i in range(len(array)-windowSize):
        windowSum = windowSum - array[i] + array[i+windowSize]
        maxSum = max(windowSum, maxSum)
    return maxSum    

if __name__ == "__main__":
    array = [1,5,9,0,5,0,2,1,5,0,3,5,0]
    print(maxSum(array,2))