

def getLeftPosition(array, target):
    left = 0
    right = len(array) - 1

    while(left<=right):
        mid = (left + right) // 2
        if array[mid] == target:
            if mid == 0 or array[mid-1] !=target:
                return mid
            right = mid - 1     
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1     
    return -1


def getRightPosition(array, target):
    left = 0
    right = len(array) - 1
    while(left<=right):
        mid = (left+right) // 2
        if array[mid] == target:
            if (mid == (len(array)-1) or array[mid+1] != target):
                return mid
            left = mid + 1
        elif array[mid] > target:
            right = mid -1 
        else:
            left = mid + 1
    return -1

def findFistAndLastPosition(array: list, target:int):
    left = getLeftPosition(array, target)
    right = getRightPosition(array, target)
    return (left,right)


if __name__ == "__main__":
    array = [1,2,3,4,5,5,6,7,7,7,7,7,7,7,7,7,9,9]
    positions = findFistAndLastPosition(array, 55)
    print(positions)

