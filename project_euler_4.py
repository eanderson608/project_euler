numbers = []

def is_palindrome(x):
    forwards = str(x)
    backwards = forwards[::-1]
    if forwards == backwards:
        return True
    else:
        return False

# generate list of three digit products
for i in xrange(1,1000):
    for j in xrange(1, 1000):
        numbers.append(i * j)

# iterate list backwards and to find first (highest) palindrome
result = 0
for i in xrange(1, len(numbers)):
    num = numbers[len(numbers) - i]
    if is_palindrome(num) and num > result:
        result = num

print result
