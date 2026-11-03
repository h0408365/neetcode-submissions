def get_longer_word(word1: str, word2: str) -> str:
    pass
    word1_len = len(word1)
    word2_len = len(word2)

    if word1_len >= word2_len:
        return word1
    elif word2_len >= word1_len:
        return word2
    else :
        return word1


# do not modify below this line
print(get_longer_word("yellow", "orange"))
print(get_longer_word("red", "blue"))
print(get_longer_word("green", "blue"))
