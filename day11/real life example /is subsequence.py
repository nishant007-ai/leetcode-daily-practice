class Solution:
    def isSubsequence(self, s, t):
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

        if i == len(s):
            return True
        else:
            return False


# ✅ Testing the function
sol = Solution()

s = "abcvsv"
t = "fnvrn"

result = sol.isSubsequence(s, t)
print("Is Subsequence:", result)  # Output: False
