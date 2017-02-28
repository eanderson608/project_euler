# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder. What is the smallest positive number that is
# evenly divisible by all of the numbers from 1 to 20?

numbers = [20,19,18,17,16,15,14,13,12,11] # generate list of nums 1 - 20
result = 20 # start counting at 20

while True:

    # generate list of booleans that correspond to whether or not result is
    # divisible by each num between 1 - 20
    divisible = [result % number == 0 for number in numbers]

    # if a false is found in divisible list, increment and try next number
    if False in divisible:
        if result % 100000 == 0:
            print result, "FALSE"
        result += 20

    # otherwise num is divisible by 1 - 20 so print and break while loop
    else:
        print result, "TRUE"
        print "done"
        break
