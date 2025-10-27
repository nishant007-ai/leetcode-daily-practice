class Solution:
    def simplifyPath(self,path):
        stack= []
        n= path.split("/")


        for path in n:
            if path = '.'or path =='':
                continue
            elif path == '..':
                if stack :
                    stack.pop()
                else :
                    stack.append()
        return '/'+'/'.join(stack)               