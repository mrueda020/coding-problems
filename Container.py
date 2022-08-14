
def calculateMaxArea(heightArray:list):
    leftPointer = 0
    rightPointer = len(heightArray) - 1
    maxArea = 0

    while leftPointer < rightPointer:
        height = min(heightArray[leftPointer],heightArray[rightPointer])
        width = rightPointer - leftPointer
        area = height * width
       
        maxArea = max(maxArea,area)

        if heightArray[leftPointer] < heightArray[rightPointer]:
            leftPointer +=1
        else:
            rightPointer -=1

    return maxArea 


if __name__ == "__main__":
    array = [1,8,6,2,5,7]
    print(calculateMaxArea(array))               