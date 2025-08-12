

class Solution:
    def canConstruct(self, ransomNote, magazine):
        ransom_count = Count(ransomNote)
        magazine_count = Count(magazine)
        
        for char, count in ransom_count.items():
            if magazine_count[char] < count:
                return False
            else :
                  return True    
 
