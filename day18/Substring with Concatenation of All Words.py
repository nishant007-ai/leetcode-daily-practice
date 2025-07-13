from collections import Counter

class Solution:
    def findSubString(self, s, words):
        if not s or not words:
            return []

        word_length = len(words[0])
        num_words = len(words)
        total_length = word_length * num_words
        word_freq = Counter(words)
        result = []

        for i in range(len(s) - total_length + 1):
            current = {}
            for j in range(0, total_length, word_length):
                word = s[i + j:i + j + word_length]
                if word in word_freq:
                    current[word] = current.get(word, 0) + 1
                    if current[word] > word_freq[word]:
                        break
                else:
                    break

            if current == word_freq:
                result.append(i)

        return result
