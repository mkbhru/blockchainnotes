from datetime import *

d1 = datetime.now()
d2 = datetime.now()  # after a 5-second or so pause

# datetime.timedelta(0, 5, 203000)
dd = d2 - d1
print(dd.days)  # get days
print(dd.seconds)  # get seconds
print(dd.microseconds)  # get microseconds
# print(int(round(dd.total_seconds()/60, 0)))  # get minutes
