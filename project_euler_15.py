# Starting in the top left corner of a 2x2 grid, and only being able to move to
# the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20x20 grid?

# to get from the upper left corner to the lower right of a 20 x 20 grid, you have to go right 20 times and you have to go down 20 times.  So the question basically is 'how many combinations are there of 20 rights and 20 downs?'
import math


def nCk(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

d = 4
total = 0
for k in range(d + 1):
    result = nCk(d, k) ** 2
    total += result
    print result

print total
