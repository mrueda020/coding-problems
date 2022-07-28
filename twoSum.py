def twoSum(array:list, target:int):
    m = {}
    for i in range(0,len(array)):
        value = target - array[i]
        if value in m:
            return (i, m[value])
        m[array[i]] = i    
            

if __name__ == '__main__':

    array = [2,8,5,7,11,15]
    target = 9
    print(twoSum(array,target))
