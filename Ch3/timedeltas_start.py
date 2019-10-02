#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))

# print today's date
now = datetime.now()
print("Today is {}".format(now))

# print today's date one year from now
print("In one year it will be {}".format((now + timedelta(days=365))))

# create a timedelta that uses more than one argument
print("In 5 days and 3 weeks it will be {}".format((now + timedelta(weeks=3, days=5))))

# calculate the date 1 week ago, formatted as a string
print("One week ago, it was {}".format(now + timedelta(weeks=-1)))

# How many days until April Fools' Day?
today = date.today()
afd = date(today.year, 4, 1)


# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
    print("April fool's day already went by %d days ago" % (today-afd).days)
    afd = afd.replace(year=today.year + 1)

# Now calculate the amount of time until April Fool's Day  
time_to_afd = afd - today
print("It's just", time_to_afd.days, "to next AFD")

