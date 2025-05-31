"""You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the argument is itself not a perfect square then return either -1 or an empty value like None or null, depending on your language. You may assume the argument is non-negative.

Examples ( Input --> Output )
121 --> 144
625 --> 676
114 --> -1  #  because 114 is not a perfect square"""


def find_next_square(sq):
    if int(sq ** 0.5) == sq ** 0.5:
        return (sq ** 0.5 + 1) ** 2
    elif int(sq ** 0.5) != sq ** 0.5:
        return -1
