class Solution :
    
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(pattern) != len(words):
            return False
            

        return len(set(zip(pattern, words))) == len(set(pattern)) == len(set(words))
