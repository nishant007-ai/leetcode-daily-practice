# Real-life Mini Project based on LeetCode 27 - Remove Element
# Project: Blocked Words Filter
# 📥 Input:
words = ["delhi", "solapur", "maharashtra", "pune", "goa"]
blocked = ["goa", "pune"]


# 🔧 Code:
def remove_blocked_words(words, blocked):
    i = 0
    while i < len(words):
        if words[i] in blocked:
            words.pop(i)
        else:
            i += 1
    return words


output 
Filtered words: ['dhelhi', 'solapur', 'maharashtra']
it based on my understadninh knowledge