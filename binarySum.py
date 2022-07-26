def binarySum(num1:str, num2:str):

    i = len(num1) - 1
    j = len(num2) - 1

    result = []
    carry = 0

    while(i>=0 or j>= 0 or carry==1):
        sum = carry
        if i>=0:
            sum += int(num1[i])
            i-=1

        if j>=0:
            sum += int(num1[j])
            j-=1

        result.append(str(sum % 2))
        carry = sum // 2

    return ("".join(reversed(result)))              

if __name__ == "__main__":
    print(binarySum("1","1"))    