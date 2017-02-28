fib_list = [1, 2]
n = 4000000


# create list of fibbonacci numbers
while True:
    length = len(fib_list)
    last_item = fib_list[length - 1]
    second_to_last_item = fib_list[length - 2]

    new_fib = last_item + second_to_last_item

    if new_fib < n:
        fib_list.append(new_fib)
    else:
        break

print fib_list

# add together even elements
total = 0 # running total
for fib in fib_list:
    if fib % 2 == 0:
        total += fib

print total
