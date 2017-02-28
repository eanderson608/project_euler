# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

written_nums = { 0: "zero", 1 : "one", 2: "two", 3: "three", 4: "four",
+ 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
+ 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
+ 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
+ 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
+ 70: "seventy", 80: "eighty", 90: "ninety", 100: "hundred and",
+ 1000: "one thousand" }

def count_alpha(s):
    count = 0
    for char in s:
        if char.isalpha():
            count += 1
    return count

def written_num(num):

    if num > 1000 or num < 0:
        return
    num = str(num)
    if len(num) == 2:
        num = '0' + num
    if len(num) == 1:
        num = '00' + num

    if num == '000':
        return written_nums[0]

    if num == '1000':
        return written_nums[1000]

    result = ''

    if int(num[0]) > 0:
        if int(num[1:]) == 0:
            result += written_nums[int(num[0])] + " " + written_nums[100][:-3]
        else:
            result += written_nums[int(num[0])] + " " + written_nums[100] + " "




    if int(num[1]) == 1:
        result = result + written_nums[int(num[1:])] + " "
        return result

    if int(num[1]) > 1:
        result = result + written_nums[int(num[1]) * 10] + " "

    if int(num[2]) > 0:
        result = result + written_nums[int(num[2])] + " "


    return result

total = 0
for i in range(1, 1001):
    num_letters = count_alpha(written_num(i))
    num = written_num(i)
    total += num_letters
    print num, num_letters

print total
