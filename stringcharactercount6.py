"""The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}."""

def count(s):
    abet = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    lets = []
    counted = []
    for char in abet:
        if char in s:
            lets.append(char)
            counted.append(s.count(char))
    return dict(zip(lets, counted))
