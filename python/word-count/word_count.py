import re

def word_count(words):
    counts = {}
    new_words = re.sub('[^a-zA-Z0-9]', ' ', words.lower()).split()
    for word in new_words:
        counts[word] = new_words.count(word)
    return counts
