# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the
# primes below two million.

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

n = 2000000

result = sum([x for x in range(2,n) if is_prime(x)])
print result
