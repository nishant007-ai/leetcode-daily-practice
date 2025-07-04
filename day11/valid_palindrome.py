class Solution:
    def isPalindrome(self, s):
        clean = ""

        for i in range(len(s)):
            char = s[i]
            if char.isalnum():
                clean += char.lower()

        reversed_str = ''.join(reversed(clean))

        if clean == reversed_str:
            return True
        else:
            return False
