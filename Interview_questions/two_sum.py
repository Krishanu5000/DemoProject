def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        if (target - nums[i]) not in d:
            d[nums[i]] = i
        else:
            prev_index = d[target - nums[i]]
            return (prev_index, i)



print(twoSum([2,7,11,15], 9))
