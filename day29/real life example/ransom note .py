class Solution :
    def ransomNote(self, ransomNote, magazine):

        n= counter (ransomNote)
        k = counter (magazine)
        for char, count in n.items():
            if k[char] < count:
                return False
        return True 
    #Input: ransomNote = "aa", magazine = "aab"
#Output: true


