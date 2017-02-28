# The following iterative sequence is defined for the set of positive integers:
#
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# Once the chain starts the terms are allowed to go above one million.

# returns a list of the collatz sequence
def collatz_seq(start_num):
    seq = [start_num]
    while seq[-1] > 1: # while the last num in sequence is greater than 1

        if seq[-1] % 2 == 0: # do if last is even
            seq.append(seq[-1] / 2)
        else:
            seq.append(3 * seq[-1] + 1) # do if last is odd

    return seq

max_len = 0
max_len_i = 0

# find largest collatz_seq for start num under 1 million
for i in range(1000000):
    seq_len = len(collatz_seq(i))
    if seq_len > max_len:
        max_len = seq_len
        max_len_i = i

print max_len_i
print max_len
