
class Solution:
    def calcutlator (self,s):
        result = 0
        stack =[]
        num = 0
        ign =1


        for ch in s:
            if ch .isdigit():
                num = num *10+int(ch)
            elif ch == '-':
                result += ign * num
                num=0
                ign=-1
            elif ch =='+':
                result += ign*num
                num=0
                ign =1
            elif ch == '(':
                stack .append(result)
                stack .append(ign)
                result= [] 
                sign =1
            elif ch ==')':
                result += ign*num
                num=0
                result *=stack.pop()
                result +=stack.pop()
        result += ign *num
        return result        
