
from typing import List


def moveZeros(array:list):
    i = 0
    for num in array:
        if num !=0 :
            array[i] = num
            i+=1

    for j in range(i, len(array)):
        array[j] = 0
    return array

if __name__=="__main__":
    array = [1,5,9,0,5,0,2,1,5,0,3,5,0]
    print(moveZeros(array))