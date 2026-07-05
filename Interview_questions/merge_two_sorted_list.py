def merge(nums1, m, nums2, n) :
    nums1_copy = nums1[:m]
    for j in range(len(nums2)-1,-1,-1):
        inserted = False
        for i in range(len(nums1_copy)-1,-1,-1):
            if nums1_copy[i] <= nums2[j]:
                nums1_copy.insert(i+1, nums2[j])
                inserted = True
                break

        if not inserted:
            nums1_copy.insert(0, nums2[j])

    nums1[:] = nums1_copy
    return nums1

print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))

print(merge([7,9,11,0,0,], 3, [8,12], 2))

print(merge([0], 0, [1], 1))




