def detect_anagrams(word, word_list):
    results = []
    for item in word_list:
        current_word = list(word.lower())
        current_item = list(item.lower())
        if current_word != current_item and sorted(current_word) == sorted(current_item):
            results.append(item)
    return results
