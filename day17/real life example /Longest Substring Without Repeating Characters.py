class Solution:
    def lengthOfLongestSubstring(self, s):
        k = {}
        left = 0    
        m = 0       

        for i in range(len(s)):
            if s[i] in k and k[s[i]] >= left:
                left = k[s[i]] + 1

            k[s[i]] = i  
            m = max(m, i - left + 1)

        return m

#sol = Solution()
#print(sol.lengthOfLongestSubstring("abcabcbb"))  # Output: 3

