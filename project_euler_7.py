# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13. What is the 10 001st prime number?

n = 10001

# returns True if argument is a prime number
def is_prime(x):
    for i in xrange(2,x):
        if x % i == 0:
            return False

    return True

nth_prime = 1
i = 2
while True:
    if is_prime(i):
        print nth_prime, ":\t", i
        if nth_prime == n:
            break
        else:
            nth_prime += 1
    i += 1
