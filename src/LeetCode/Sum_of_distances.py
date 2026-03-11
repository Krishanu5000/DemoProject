def distance(nums):
    n = len(nums)
    arr = []
    for i in range(n):
        s = 0
        for j in range(n):
            if nums[i] == nums[j]:
                s+= abs(i - j)
        arr.append(s)
    return arr

print(distance([1,3,1,1,2]))


