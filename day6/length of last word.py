class Solutu():
    def lengthOfLastWord (self,s):

        s= s .rstrip()
        word = s.split()


        return len(word[-1])
