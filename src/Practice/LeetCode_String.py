class Solution:
    def lognest_substring_without_repeating_char(self, s):
        if s == "":
            return 0

        l = [False] * 256
        # print(l)
        max_len = 1
        s1 = ""
        start = 0
        for i in range(0, len(s)):
            print(s[i], "-->", ord(s[i]))
            if i == 0:
                s1 += s[i]
                l[ord(s[i])] = True

            if not l[ord(s[i])] and i > 0:
                s1 += s[i]
                max_len = max(max_len, len(s1))
                l[ord(s[i])] = True
                print(s1)
            elif l[ord(s[i])] and (i > 0 and s[i] != s[i - 1]):
                print("**")
                print("s1 bfore", s1)
                b = s1.find(s[i])
                # print(s1[s1.index(s[i])+1])
                s1 = s1[b + 1:] + s[i]
                max_len = max(max_len, len(s1))
                # l[ord(s[i])] = True
                print(s1)
            else:
                s1 = s[i]
                print(s1)

            print(l[ord(s[i])])
        return max_len

    def longest_palindromic_substring(self, s):

        if s == s[::-1]:
            return s

        temp = ""
        for i in range(0, len(s)):
            print("i", i)
            s1 = ""
            for j in range(i, len(s)):
                s1 += s[j]
                print("s1", s1)
                if s1 == s1[::-1]:
                    if len(s1) > len(temp):
                        temp = s1
        return temp

    def printZigZagConcat(self, s, n):
        if n == 1:
            print(str)

        l = len(s)
        arr = ["" for x in range(l)]
        row = 0
        for i in range(l):
            arr[row] += s[i]
            if row == n - 1:
                down = False
            elif row == 0:
                down = True

            if down:
                row += 1
            else:
                row -= 1

        for i in range(n):
            print(arr[i], end = "")

        s1 = ""
        for i in range(len(arr)):
            s1 += arr[i]
        return s1











obj = Solution()
# print(obj.longest_palindromic_substring("babad"))
# print(obj.longest_palindromic_substring("aacabdkacaa"))
#print(obj.longest_palindromic_substring("abcda"))
# print(obj.longest_palindromic_substring("abacab"))
# print(obj.lognest_substring_without_repeating_char("pwwkew"))

s="PAYPALISHIRING"
print(obj.printZigZagConcat(s, 3))
