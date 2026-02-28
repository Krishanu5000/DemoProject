"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty."""


def longestCommonPrefix(strs):
    if len(strs) == 1:
        return strs[0]
    min_length = len(strs[0])
    min_idx = 0
    for i in range(len(strs)):
        if len(strs[i]) < min_length:
            min_length = len(strs[i])
            min_idx = i
    # print(min_length)
    min_str = strs[min_idx]
    # print("minmum string", min_str)

    flag = False
    s = ""
    for i in range(len(min_str)):
        for j in range(len(strs) - 1):
            if strs[j][i] == strs[j + 1][i]:
                flag = True
            else:
                flag = False
                break
        if flag:
            s += min_str[i]
        else:
            break
    return s

print(longestCommonPrefix(["flower","flow","flight"]))

print(longestCommonPrefix(["dog","racecar","car"]))

print(longestCommonPrefix(["a"]))

print(longestCommonPrefix(["cir","car"]))

print(longestCommonPrefix(["reflower","flow","flight"]))
