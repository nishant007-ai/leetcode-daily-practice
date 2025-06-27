class Nishart:
    def reversestring(self, s):
        s = s.strip()
        words = s.split()
        words.reverse()
        i = ' '.join(words)
        return i
