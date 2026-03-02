import re


class StringPractice:
    def anagramcheck(self, s1, s2):
        if len(s1) != len(s2):
            return False
        s1_freq = {}
        s2_freq = {}

        for i in s1:
            s1_freq[i] = 0

        for i in s2:
            s2_freq[i] = 0

        for i in s1:
            s1_freq[i] += 1
        for i in s2:
            s2_freq[i] += 1

        s1_sorted = sorted(s1)
        s2_sorted = sorted(s2)
        if s1_sorted != s2_sorted:
            return False

        for i in s1:
            if s1_freq[i] != s2_freq[i]:
                return False
        return True

    def leftMostRepeatingCharacter(self, s):
        s_dict = {}
        for i in s:
            s_dict[i] = 0
        for i in s:
            s_dict[i] += 1
        for i in range(0, len(s)):
            if s_dict[s[i]] > 1:
                return i
        return -1

    def circularString(self, s1, s2):
        s = s1 + s1
        if len(s1) != len(s2):
            return False
        if s.find(s2) >= 0:
            print(s.find(s2))
            return True

        return False

    def are_circular_rotations(self, s1, s2):
        # Check if lengths are the same
        if len(s1) != len(s2):
            return False
        # Check if s2 is a substring of s1 concatenated with itself
        return s2 in (s1 + s1)

    def regxp_search(self, s1, s2):
        print(re.search(s1, s2))
        x = re.search(s1, s2)
        if x:
            print(True)
        else:
            print(False)

        x = re.split("\s", s2)
        print(x)

        x = re.sub("\s", "-", s2)
        print(x)

    def string_functions_exmaple(self, s):
        print(s.split(" "))
        s1 = s.split(" ")
        s2 = "-".join(s1)
        print(s2)
        s3 = s2.replace("-", "<>")
        print(s3)
        print(s.find("are"))
        print(s.find("drive"))

    def naive_pattern_searching(self, s, p):
        pat_len = len(p)
        l = []
        for i in range(0, len(s) - pat_len + 1):
            k = i
            for j in range(0, pat_len):
                if s[k] == p[j]:
                    flag = True
                    k += 1
                else:
                    flag = False
                    break
            if flag == True:
                l.append(i)
        return l

    def lognest_substring_without_repeating_char(self, s):
        l = [False] * 256
        # print(l)
        max_len = 1
        s1 = ""
        for i in s:
            # print(i, "-->", ord(i))
            if not l[ord(i)]:
                s1 += i
                max_len = max(max_len, len(s1))
                l[ord(i)] = True
                # print(s1)
            else:
                s1 = i
                # print(s1)

        # print(l)
        return max_len

    # longest palindrmic substring
    # Input: s = "aaaabbaa"
    # Output: aabbaa

    def longestPalindromesubstring(self, s):
        # code here
        d = {}
        l = []
        tmp = ""
        for i in range(len(s)):
            tmp = s[i]
            l.append(tmp)
            d[s[i]] = len(s[i])
            for j in range(i + 1, len(s)):
                tmp += s[j]
                l.append(tmp)
                d[tmp] = len(tmp)
        # print(l)
        # print(d)
        max = 0
        max_palindm_str = ""
        for i in l:
            if i == i[::-1]:
                if d[i] > max:
                    max = d[i]
                    max_palindm_str = i
        for i in l:
            if i == max_palindm_str:
                return i


obj = StringPractice()
'''Anagram test case'''
# print(obj.anagramcheck("listen", "silent"))
# print(obj.anagramcheck("aaacb", "cabaa"))
# print(obj.anagramcheck("aab", "bab"))
'''Left Most repeating elements '''
# print(obj.leftMostRepeatingCharacter("geeksforgeeks"))
# print(obj.leftMostRepeatingCharacter("abbcc"))
# print(obj.leftMostRepeatingCharacter("abcd"))
# print(obj.circularString("abcd", "cdab"))
# print(obj.circularString("abab", "abba"))
# print(obj.are_circular_rotations("abab", "abba"))
# obj.regxp_search("ab", "abba are good example")
# obj.string_functions_exmaple("abba are good example")
# print(obj.naive_pattern_searching("ABABABCD", "ABAB"))
# print(obj.naive_pattern_searching("ABCABCD", "ABCD"))
# print(obj.naive_pattern_searching("AAAAA", "AAA"))
# print(obj.lognest_substring_without_repeating_char("pwwkew"))
print(obj.longestPalindromesubstring("aaaabbaa"))
