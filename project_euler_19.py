# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
#
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
#
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                'Saturday', 'Sunday']

days_in_month = { months[0] : 31, months[1] : 28, months[2] : 31,
                  months[3] : 30, months[4] : 31, months[5] : 30,
                  months[6] : 31, months[7] : 31, months[8] : 30,
                  months[9] : 31, months[10] : 30, months[11]: 31}

total_sundays = 0 # store amount of sundays found on first of month

# store current day of week on first of the month
first_of_month_day = 0

for year in range(1900, 2001):

    # determine if its a leap year, if so, change number of days in February
    if year % 400 == 0:
        days_in_month['February'] = 29

    elif year % 4 == 0 and not year % 100 == 0:
        days_in_month['February'] = 29

    else:
        days_in_month['February'] = 28

    for month in months:

        print year, month, days_of_week[first_of_month_day]

        # calculate which day is on the first of next month
        first_of_month_day = (first_of_month_day + days_in_month[month] % 7) % 7

        # if it is a sunday, increment sunday counter
        if days_of_week[first_of_month_day] == 'Sunday' and year > 1900:
            total_sundays += 1

print total_sundays
