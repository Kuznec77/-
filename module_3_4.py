def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if root_word.lower().count(word.lower()) or word.lower().count(root_word.lower()):
            same_words.append(word)
    return same_words
print(single_root_words('rich', 'richiest', 'orichalcum', 'chers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
