
def isBadVersion(n):
    return n >= 75

def getFirstBadVersion(n):
    low = 1
    high = n
    while low < high:
        mid = (low+high) // 2
        #If not bad version then move to next one
        if not isBadVersion(mid):
            low = mid +1
        #If bad version we still need to find the first    
        else:
            high = mid
    return low        

if __name__ == "__main__":
    print(getFirstBadVersion(100))    