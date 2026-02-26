class PracticeArray:
    def lrgestelemnt(self, l):
        max = l[0]
        for i in range(0, len(l)):
            if l[i] > max:
                max = l[i]
        # print("max:", max)
        return l.index(max)

    def secondlargestelement(self, l):
        max_ind = self.lrgestelemnt(l)
        second_max = l[0]
        for i in range(0, len(l)):
            if (l[i] > second_max) and (i != max_ind):
                second_max = l[i]
                print(second_max)
        # print("2nd max:", second_max)
        return l.index(second_max)

    # Array is sorted if every element at right side will be greater than left side.
    def checksortedarray(self, l):
        for i in range(0, len(l) - 1):
            if l[i] > l[i + 1]:
                return False
        return True

    def reversearray(self, l):
        # l2 = []
        # for i in range(len(l) - 1, -1, -1):
        #     l2.append(l[i])
        # return l2
        low = 0
        high = len(l) - 1
        while low < high:
            temp = l[low]
            l[low] = l[high]
            l[high] = temp
            low += 1
            high -= 1
        return l

    def moveZeoAtEnd(self, l):
        cnt = 0
        for i in range(0, len(l)):
            if i == 0 and l[i] != 0:
                l[cnt] = l[i]
                cnt += 1

            if l[i] != 0 and i != 0:
                temp = l[i - 1]
                l[cnt] = l[i]
                l[i] = temp
                cnt += 1
            print("i = ", i, l, "cnt", cnt)

        return l

    def removedDuplicates(self, l):
        max_len = max(l)
        l2 = [0] * max_len
        for i in l:
            l2[i - 1] = l2[i - 1] + 1
        for i in range(len(l) - 1, -1, -1):
            if l2[l[i] - 1] > 1:
                l2[l[i] - 1] -= 1
                l.pop(i)
        # can nto proceed with below operation bcz list length is going to reduce before it going to the end.
        # d = len(l)
        # for i in range(0, d):
        #     if l2[l[i] - 1] > 1:
        #         print("iteration", i)
        #         print(l2[l[i] - 1])
        #         l2[l[i] - 1] -= 1
        #         l.pop(i)
        #         print(l)
        return l

    def leftRotateArrayByOne(self, l):
        print("original arr ", l)
        for i in range(0, len(l) - 1):
            temp = l[i]
            l[i] = l[i + 1]
            l[i + 1] = temp
            print("iteration ", i, "arr", l)

    def leftRotateArrayBydElements(self, l, d):
        print("original arr ", l)
        temp_arr = []
        for i in range(0, d):
            temp_arr.append(l[i])
        print("temp", temp_arr)
        for i in range(0, len(l) - d):
            temp = l[i]
            l[i] = l[i + d]
            l[i + d] = temp
            print("iteration ", i, "arr", l)
        n = len(l)
        for i in range(0, d):
            l[n - d + i] = temp_arr[i]
        return l

    # An element is leader if there is no grater element than it in right side. even equal is not allowed in right side.
    def leadersInArray(self, l):
        leaders_arr = [l[len(l) - 1]]
        curr_leader = l[len(l) - 1]
        for i in range(len(l) - 2, 0, -1):
            if l[i] > curr_leader:
                curr_leader = l[i]
                leaders_arr.append(curr_leader)
        return leaders_arr

    # using Kaden algorithm. Generally it is used for maximum subarray sum.
    '''The idea of Kadane’s algorithm is to traverse over the array from left to right and for each element, find the maximum sum among all subarrays ending at that element. The result will be the maximum of all these values. 
        But, the main issue is how to calculate maximum sum among all the subarrays ending at an element in O(1) time?
        To calculate the maximum sum of subarray ending at current element, say maxEnding, we can use the maximum sum ending at the previous element. So for any element, we have two choices:
        Choice 1: Extend the maximum sum subarray ending at the previous element by adding the current element to it. If the maximum subarray sum ending at the previous index is positive, then it is always better to extend the subarray.
        Choice 2: Start a new subarray starting from the current element. If the maximum subarray sum ending at the previous index is negative, it is always better to start a new subarray from the current element.
        This means that maxEnding at index i = max(maxEnding at index (i – 1) + arr[i], arr[i]) and the maximum value of maxEnding at any index will be our answer. '''

    def maxSubarraySum(self, l):
        maxending = l[0]
        res = l[0]
        for i in range(1, len(l)):
            maxending = max(maxending + l[i], l[i])
            res = max(maxending, res)
        return res

    # using Kaden algorithm.
    def longestEvenOddSubarray(self, l):
        curr_count = 1
        res = 1
        for i in range(1, len(l)):
            if (l[i - 1] % 2 == 0 and l[i] % 2 != 0) or (l[i - 1] % 2 != 0 and l[i] % 2 == 0):
                curr_count += 1
                res = max(curr_count, res)
            else:
                curr_count = 1
                res = 1
        return res

    # using prefix and suffix sum
    def equibriumArray(self, l):
        rs = 0
        for i in range(0, len(l)):
            rs += l[i]
        ls = 0
        for i in range(0, len(l)):
            rs -= l[i]
            if ls == rs:
                return True
            ls += l[i]
        return False




obj = PracticeArray()
# print(obj.lrgestelemnt([10, 20, 30, 40, 25, 26]))
# print(obj.secondlargestelement([10, 20, 30, 40, 25, 26]))
# print(obj.checksortedarray([10, 20, 30, 40, 25]))
# print(obj.reversearray([10, 20, 30, 40, 25]))
print(obj.moveZeoAtEnd([10, 0, 30, 0, 25]))
print(obj.moveZeoAtEnd([10, 0, 30]))
print(obj.moveZeoAtEnd([0, 0, 30, 0, 25]))
# print(obj.removedDuplicates([10, 25, 25, 30, 25]))
# print(obj.leftRotateArrayByOne([10, 20, 30, 40, 50]))
# print(obj.leftRotateArrayBydElements([10, 20, 30, 40, 50], 2))
# print(obj.leadersInArray([10, 50, 30, 40,45, 20,20,6]))
# print(obj.maxSubarraySum([2, 3, -8, 7, -1, 2, 3]))
# print(obj.longestEvenOddSubarray([10, 12, 14, 7, 8]))
# print(obj.longestEvenOddSubarray([10, 12, 8, 4]))
# print(obj.equibriumArray([3, 4, 8, 9, -9, 7]))
