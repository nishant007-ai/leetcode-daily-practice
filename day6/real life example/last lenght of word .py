class Solution:
    def lengthOfLastWord(self, s):
        s = s.rstrip()
        words = s.split()
        return len(words[-1])






    print("Length of last word:")


    #testing
    input = "Great, Nishant! Here's how you can create a .py file in VS Code to run the "
    output  = 3 


