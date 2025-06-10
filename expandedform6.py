"""Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

   12 --> "10 + 2"
   45 --> "40 + 5"
70304 --> "70000 + 300 + 4"
NOTE: All numbers will be whole numbers greater than 0."""

def expanded_form(num):
    chars = list(str(num))
    parts = []
    for digit in chars:
        if digit != '0':
            zeros = len(chars) - (chars.index(digit) + 1) #Calculates number of zeros following digit
            parts.append(f'{digit}{zeros * "0"}')
            chars[chars.index(digit)] = 'a'
    return " + ".join(parts)
