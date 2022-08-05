def fourSumCount(nums1: list, nums2: list, nums3: list, nums4: list) -> int:

    ans = 0
    m = {}
    sNums1 = len(nums1)
    sNums2 = len(nums2)
    sNums3 = len(nums3)
    sNums4 = len(nums4)

    for i in range(sNums1):
        for j in range(sNums2):

            target = nums1[i] + nums2[j]
            if target not in m:
                m[target] = 0
            m[target] += 1

    for i in range(sNums3):
        for j in range(sNums4):

            target = -(nums3[i] + nums4[j])
            if target in m:
                ans += m[target]

    return ans


if __name__ == "__main__":
    a = [1, 2]
    b = [-2, -1]
    c = [-1, 2]
    d = [0, 2]

    print(fourSumCount(a, b, c, d))
