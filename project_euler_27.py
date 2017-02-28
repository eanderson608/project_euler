# Euler discovered the remarkable quadratic formula:
#
# n2+n+41n2+n+41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0<=n<=390<=n<=39. However, when n=40,402+40+41=40(40+1)+41n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41n=41,412+41+41 is clearly divisible by 41.
#
# The incredible formula n2-79n+1601n2-79n+1601 was discovered, which produces 80 primes for the consecutive values 0<=n<=790<=n<=79. The product of the coefficients, -79 and 1601, is -126479.
#
# Considering quadratics of the form:
#
# n2+an+bn2+an+b, where |a|<1000|a|<1000 and |b|<=1000|b|<=1000
#
# where |n||n| is the modulus/absolute value of nn
# e.g. |11|=11|11|=11 and |-4|=4|-4|=4
# Find the product of the coefficients, aa and bb, for the quadratic expression that produces the maximum number of primes for consecutive values of nn, starting with n=0n=0.

import math

# returns True if argument is a prime number
def is_prime(x):

    if x < 2:
        return False

    # return false if factor is found
    # only need to check for factors up to sqrt(x)
    for i in xrange(2,int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    # no factor found
    return True

# generate list of all possible pairs of a and b
ab = [(a, b) for a in range(-999, 1000) for b in range(-1000, 1001)]

# find consecutive primes
max_num_primes = (0, 0, 0) # holds current result in the form (n, a, b)
for (a, b) in ab:

    n = 0 # start with a n of 0

    while True:

        # if a nonprime n is found, save n, a, b and break loop
        if not is_prime(n**2 + a * n + b):
            if n > max_num_primes[0]:
                max_num_primes = (n, a, b)
            break

        # otherwise increment n and continue
        n += 1


print max_num_primes
