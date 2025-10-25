class Solution:
    def validParanteshjo (self,s):

        if not s :
            return 0 
        
        stack = []
        pairs = {'(': ')', '{': '}', '[': ']'}


        for ch in s:
            if ch in pairs:
                stack.append(ch)
            elif not stack or pairs[stack.pop()] != ch:
                return False   