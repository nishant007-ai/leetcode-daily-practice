from collections import Counter

class Solution:
    def minWindow(self, s, t):
        if s ==0 and t == 0:
            return ""


        t_count = Counter(t)
        window = {}
        have = 0
        need =len(t_count)
        res, res_len = [-1, -1], float("inf")
        left = 0

        for right in range(len(s)):
            char = s[right]
            if char in window:
                 window[char] += 1
   
            else:
                 window[char] = 1 

   

            if char in t_count :
                  if window[char] == t_count[char]:
                    have+=1
 

            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

               
                window[s[left]] -= 1
                if s[left] in t_count window[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""
