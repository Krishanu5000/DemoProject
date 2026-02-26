'''Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]'''


class Solution:
    def generateParenthesis(self, n: int):
        l = []

        def backtracking(s, open_count, close_count):
            if len(s) == 2 * n:
                l.append(s)
                print("i'm now inside default statements and l is", l)
            if open_count < n:
                print("open_count", open_count, s)
                backtracking(s + "(", open_count + 1, close_count)
            if close_count < open_count:
                print("open_count", open_count, "close_count", close_count, s)
                backtracking(s + ")", open_count, close_count + 1)


        backtracking("", 0, 0)
        return l


s = Solution()
print(s.generateParenthesis(2))
