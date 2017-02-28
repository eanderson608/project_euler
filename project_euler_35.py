# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?
import math

# returns True if argument is a prime number
def is_prime(x):

    if x < 2:
        return False

    # return false if factor is found
    # only need to check for factors up to sqrt(x)
    for i in xrange(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    # no factor found
    return True

def is_circular_prime(x):

    for i in range(len(str(x))):

        # rotate x and check if prime
        x = str(x)[1:] + str(x)[0]
        if not is_prime(int(x)):
            return False

    # if all rotations are prime return true
    return True

# check if circular prime and print result and count
result = [i for i in range(1000000) if is_circular_prime(i)]
print result
print "count : ", len(result)
