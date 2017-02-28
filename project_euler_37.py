# Truncatable primes
# Problem 37
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
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

def is_truncatable_prime(x):

    if not is_prime(x):
        return False

    for i in range(1, len(str(x))):

        a = str(x)[i:]
        b = str(x)[:i]

        if not is_prime(int(a)) or not is_prime(int(b)):
            return False

    return True


result = [i for i in range(10, 1000000) if is_truncatable_prime(i)]

print result, sum(result)
