def maxBoats(array:list, limit:int):

    array.sort()

    lightPointer = 1
    heavyPointer = len(array) -1 
    boats = 0

    while (heavyPointer >= lightPointer):

        if (array[lightPointer] + array[heavyPointer] <= limit):
            lightPointer+=1
            heavyPointer+=1
            boats +=1
        else:
            heavyPointer+=1
            boats+=1
    return boats             


