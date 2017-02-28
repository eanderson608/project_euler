# In England the currency is made up of pound, L, and pence, p, and there are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, L1 (100p) and L2 (200p).
# It is possible to make L2 in the following way:
#
# 1xL1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
# How many different ways can L2 be made using any number of coins?

count = 0
coins = [1, 2, 5, 10, 20, 50, 100, 200]
thresh = coins[-1]

for i in range(thresh / coins[0] + 1):
    # if i <= thresh:
        for j in range(thresh / coins[1] + 1):
            # if sum((i * 1, j * 2)) <= thresh:
                for k in range(thresh / coins[2] + 1):
                    # if sum((i * 1, j * 2, k * 5)) <= thresh:
                        for l in range(thresh / coins[3] + 1):
                            # if sum((i * 1, j * 2, k * 5, l * 10)) <= thresh:

                                for m in range(thresh / coins[4] + 1):
                                    # if sum((i * 1, j * 2, k * 5, l * 10, m * 20)) <= thresh:
                                        for n in range(thresh / coins[5] + 1):
                                            # if sum((i * 1, j * 2, k * 5, l * 10, m * 20, n * 50)) <= thresh:
                                                for o in range(thresh / coins[6] + 1):
                                                    # if sum((i * 1, j * 2, k * 5, l * 10, m * 20, n * 50, o * 100)) <= thresh:
                                                        for p in range(thresh / coins[7] + 1):
                                                            if sum((i * 1, j * 2, k * 5, l * 10, m * 20, n * 50, o * 100, p * 200)) == thresh:

                                                                print (i, j, k, l, m, n, o, p)
                                                                count += 1

print count
