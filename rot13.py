"""ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating."""

def rot13(message):
    abet = 99*"abcdefghijklmnopqrstuvwxyz"
    uabet = 99*"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chars = list(message)
    nlets = []
    for char in chars:
        if char in abet:
            if (abet.index(char) - 1) <= 13:
                nlets.append(abet[abet.index(char) + 13])
            else:
                nlets.append(abet[abet.index(char) - 13])
        elif char in uabet:
            if uabet.index(char) - 1 <= 13:
                nlets.append(uabet[uabet.index(char) + 13])
            else:
                nlets.append(uabet[uabet.index(char) - 13])
        else:
            nlets.append(char)             
    return "".join(nlets)
