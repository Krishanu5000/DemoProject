# Longest common subsequence
# Using recursion

def Longest_commnon_subsequence(s1, s2, m, n):
    if m==0 or n==0:
        return 0
    if s1[m-1] == s2[n-1]:
        return 1 + Longest_commnon_subsequence(s1, s2, m-1, n-1)
    else:
        return max(Longest_commnon_subsequence(s1, s2, m-1, n), Longest_commnon_subsequence(s1, s2, m, n-1))


print(Longest_commnon_subsequence("AXYZ", "BAZ", 4, 3))