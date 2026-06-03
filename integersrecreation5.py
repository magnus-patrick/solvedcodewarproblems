"""1, 246, 2, 123, 3, 82, 6, 41 are the divisors of number 246.

Squaring these divisors we get: 1, 60516, 4, 15129, 9, 6724, 36, 1681.

The sum of these squares is 84100 which is 290 * 290.

Task
Find all integers between m and n (m and n are integers with 1 <= m <= n) such that the sum of their squared divisors is itself a square.

We will return an array of subarrays or of tuples (in C an array of Pair) or a string.

The subarrays (or tuples or Pairs) will have two elements: first the number the squared divisors of which is a square and then the sum of the squared divisors.

Example:
m =  1, n = 250 --> [[1, 1], [42, 2500], [246, 84100]]
m = 42, n = 250 --> [[42, 2500], [246, 84100]]
The form of the examples may change according to the language, see "Sample Tests".

Note
In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings."""

import math

def list_squared(m, n):
    squares = []
    
    for dividend in range(m, n + 1): # from 1 to 250
        s = 0 # sum starts at 0
        for pot_div in range(1, int((dividend)**0.5) + 1): # finds potential divisors from 1 to sqrt dividend
            if dividend % pot_div == 0:
                s += (pot_div)**2 # sum increases by divisor^2
                if dividend // pot_div != pot_div: # finds other divisor to make a pair. This allows the second for loop to only have to check up to the sqrt of the dividend.
                    s += (dividend // pot_div)**2
        if (math.isqrt(int(s)))**2 == s:
            squares.append([dividend, int(s)])
    return squares
print(list_squared(250, 500))
