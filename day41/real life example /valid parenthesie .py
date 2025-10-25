class Solution:
    def validparentis (self,s)
        
        stack = []
        pairs = {'(': ')', '{': '}', '[': ']'}


        for ch in s:
            if ch in pairs:
                stack .appned(ch)
            elif not stack or pairs[stack.pop()] != ch:
                return False
        return not stack    


#print(Solution().isValid("()"))       # True
print(Solution().isValid("()[]{}"))   # True
print(Solution().isValid("(]"))       # False
print(Solution().isValid("([)]"))     # False
print(Solution().isValid("{[]}"))     # True

#Example:

stack = ['(', '['], ch = ')'

Pop '['

pairs['['] → expected ']'

']' != ')' → mismatch → return False.