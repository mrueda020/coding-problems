import math


def countOfPrimeNumbers(n:int):
    if n < 2:
        return 0

    isPrimeNumber = [True] * n

    isPrimeNumber[0] = False
    isPrimeNumber[1] = False

    limit = math.ceil(math.sqrt(n))
    for i in range(2, limit):
        if isPrimeNumber[i]:
            for j in range(i*i, n, i):
                isPrimeNumber[j] = False   

    numberOfPrimes = sum(isPrimeNumber)
    return numberOfPrimes            