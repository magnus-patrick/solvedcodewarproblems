"""Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid."""

def high(x):
    abet = "abcdefghijklmnopqrstuvwxyz"
    word_scores = []
    words = x.split(" ")
    for word in words:
        score = 0
        for char in word:
            score += abet.index(char) + 1
        word_scores.append(score)
    return words[word_scores.index(max(word_scores))]
