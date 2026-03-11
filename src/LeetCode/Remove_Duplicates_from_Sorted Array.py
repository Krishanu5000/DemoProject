"""Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted."""


def removeDuplicates(nums):
    d = {}
    n = len(nums)
    for i in range(len(nums)):
        if nums[i] not in d:
            d[nums[i]] = 1
        else:
            d[nums[i]] +=1
    print(d)
    print("before going inside for loop", nums)
    for i in range(len(nums)):
        if nums[i] != '_':
            while d[nums[i]] > 1:
                nums.pop(i)
                nums.append("_")
                # print(nums[i])
                print("iteration no", i, "array after pop in each iteration", nums)
                d[nums[i]]-=1
                n -= 1

    return n, nums



print(removeDuplicates([1, 1, 2]))
#
# print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

# print(removeDuplicates([-1,0,0,0,0,3,3]))