class Solution:
    def reverseWords(self, s):
         
        s = s.strip()

        words = s.split()
        words.reverse()
        # Join with single space
        return ' '.join(words)



#testing 
input = my name is Nishant
output = Nishant is name my