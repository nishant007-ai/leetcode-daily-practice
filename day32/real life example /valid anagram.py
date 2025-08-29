class Solution :
    def isAnagram(self,s,t):
        if len(s)!=len(t):
            return False
        count =[0]*26

        for char in s:
           
           count[ord(char)-ord('a')]==+1:

        for char in t:
            count[ord(char)-ord(char)]==-1:

          for c in count:
            if c != 0:
                return false
        return True 
    


# Run test cases when file is executed
# ------------------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.isAnagram("anagram", "nagaram"))  # Expected: True
    print(sol.isAnagram("rat", "car"))          # Expected: False

