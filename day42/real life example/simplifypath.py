class Solution :
    def simpliPath(self,path):
        stack = [ ]

        k = path.split('/')

        for path in k:
            if path ='.' or path=='':
                continue
            elif path == ' ..':
                if stack :
                    stack.pop()
                else:
                    stack.append()
        return '/'+'/'.join(stack)                
                       
            
     #       parts = ['', 'home', '', 'foo', '']
stack = []

→ part = ''       → skip
→ part = 'home'   → add → ['home']
→ part = ''       → skip
→ part = 'foo'    → add → ['home', 'foo']
→ part = ''       → skip
#path =
"/home/"
#Output
"/home"

