# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import math

def is_curious(num):

    return sum([math.factorial(int(i)) for i in list(str(num))]) == num


print sum([i for i in range(10, 100000) if is_curious(i)])
