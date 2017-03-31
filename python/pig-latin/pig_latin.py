def translate(word_list):
    words = []
    for word in word_list.split():
        if word[0:3] in ['squ','thr','sch']:
            words.append(word[3:] + word[0:3] + "ay")
        elif word[0:2] in ['ch','qu','th']:
            words.append(word[2:] + word[0:2] + "ay")
        elif word[0:2] in ['yt', 'xr']:
            words.append(word + "ay")
        elif word[0] in ['a','e','i','o','u']:
            words.append(word + "ay")
        else:
            words.append(word[1:] + word[0] + "ay")
    return ' '.join(words)
