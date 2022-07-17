
def isMountainArray(array:list) :
    arrayLength = len(array)
    if arrayLength <= 3:
        return False

    index = 1
    while index < arrayLength and array[index] > array[index-1] :
        index +=1

    if index == 1 or index == arrayLength:
        return False

    while index < arrayLength and array[index] < array[index-1] :
        index +=1          

    return index == arrayLength    