"""Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

DIFFICULTY: 7 kyu 

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false"""

def xo(s):
    characters = list(s)
    num_x = 0
    num_o = 0
    for character in characters:
        if character.lower() == "o":
            num_o += 1
        elif character.lower() == "x":
            num_x += 1
    if num_x == num_o:
        return True
    else:
        return False
xo(s)
