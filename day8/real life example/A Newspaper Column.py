class Solution:
    def textFullJustify(self, words, maxWidth):
        res = []
        line = []
        length = 0  # Should be a number, not a list

        for word in words:
            if length + len(line) + len(word) > maxWidth:
                spaces = maxWidth - length

                if len(line) == 1:
                    res.append(line[0] + ' ' * spaces)
                else:
                    even_space = spaces // (len(line) - 1)
                    extra_space = spaces % (len(line) - 1)

                    for i in range(extra_space):
                        line[i] += ' '

                    res.append((' ' * even_space).join(line))

                line = []
                length = 0

            line.append(word)
            length += len(word)

        # Last line: left-align and fill spaces to right
        last_line = ' '.join(line)
        last_line += ' ' * (maxWidth - len(last_line))
        res.append(last_line)

        return res

# testing 
input =["India", "is", "a", "beautiful", "country", "with", "rich", "history"]
maxWidth = 30

output ="India   is   a  beautiful"
"country   with   rich"
"history                    "
