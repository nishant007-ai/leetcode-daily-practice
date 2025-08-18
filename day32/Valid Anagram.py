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

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    sol = Solution()
    print(sol.isAnagram(s, t))  # Expected output: True

    s = "rat"
    t = "car"
    print(sol.isAnagram(s, t))  # Expected output: False
