# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.
#
# What is the total of all the name scores in the file?

# open file in read-only mode
f = open('p022_names.txt', 'r')

# create list of names from file, strip off quotation marks, and sort
names = f.read().split(',')
names = [name[1:-1] for name in names]
names = sorted(names)

# create char to integer value mapping using a dictionary
letters = {}
for i in range(26):
    letters[chr(ord('A') + i)] = i + 1

total = 0 # running total of name scores

# for each name in list, multiply sum of integer values with its position in the alphabetical list (since names uses zero-based indexing use i + 1)
for i, name in enumerate(names):

    total += sum([letters[char] for char in name]) * (i + 1)

print total
