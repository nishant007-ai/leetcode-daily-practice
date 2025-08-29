class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        count = [0] * 26  

        for ch in s:
            count[ord(ch) - ord('a')] += 1
        for ch in t:
            count[ord(ch) - ord('a')] -= 1

        for c in count:
            if c != 0:
                return False
        return True


# ------------------------------
# Run test cases when file is executed
# ------------------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.isAnagram("anagram", "nagaram"))  # Expected: True
    print(sol.isAnagram("rat", "car"))          # Expected: False
