"""You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

If the string's length is odd, return the middle character.
If the string's length is even, return the middle 2 characters.
Examples:
"test" --> "es"
"testing" --> "t"
"middle" --> "dd"
"A" --> "A" """

def get_middle(s):
    if len(s) % 2 == 0:
        return s[int((len(s) / 2) - 1):int((len(s) / 2) + 1)]
    elif len(s) % 2 == 1:
        return s[(len(s) // 2)]
