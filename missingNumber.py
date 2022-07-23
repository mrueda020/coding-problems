def missingNumber(array:list):
    n = len(array)
    actualSum = 0
    #actualSum = sum(array)
    for  num in array:
        actualSum += num 

    intentedSum = n*(n+1) / 2
    
    return intentedSum - actualSum


if __name__=="__main__":
    array = [0,1,2,3,5,6,7,8,9]
    print(missingNumber(array))