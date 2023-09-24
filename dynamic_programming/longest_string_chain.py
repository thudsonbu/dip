def longestStrChain(words):
    length_to_words = {}
    word_lengths = set()
    for word in words:
        if len(word) in length_to_words:
            length_to_words[len(word)].add(word)
        else:
            length_to_words[len(word)] = set([word])
        word_lengths.add(len(word))

    max_chain_length = 1

    word_to_score = {}
    for word in words:
        word_to_score[word] = 1

    word_lengths = sorted(list(word_lengths))
    current_words = length_to_words[word_lengths.pop(0)]

    while len(word_lengths):
        next_words = list(length_to_words[word_lengths.pop(0)])

        for current_word in current_words:
            for next_word in next_words:
                if isPredecessor(current_word, next_word):
                    word_to_score[next_word] = max(
                        word_to_score[next_word], word_to_score[current_word] + 1)

                    max_chain_length = max(
                        word_to_score[next_word], max_chain_length)

        current_words = next_words

    return max_chain_length


def isPredecessor(current_word, next_word):
    if len(current_word) != len(next_word) - 1:
        return False

    offset = 0
    for i in range(0, len(current_word)):
        if current_word[i + offset] != next_word[i]:
            offset -= 1
        if offset < -1:
            return False

    return True


print(longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]))
print(longestStrChain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))
print(longestStrChain(["abcd", "dbqca"]))
