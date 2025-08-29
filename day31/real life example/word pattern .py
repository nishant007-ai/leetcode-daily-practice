class Solution :
    def wordPattern(self, pattern,s):
        n = s.splite()

        if len (pattern!= len(n)):
            return False
        return len(set(zip(pattern,n))) == len(set(pattern)) == len(set(n))
#    
  #  Input: pattern = "abba", s = "dog cat cat dog"
#Output: True ✅

#Input: pattern = "abba", s = "dog cat cat fish"
#Output: False ❌
