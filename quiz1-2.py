# Author: Emanuel Mark Gjoka (AMDG) 10/19/2020

q = input("What is the day of the month?")
m = input("What is the month?")
y = input("What is the year?")

k = int(y) / 100
j = int(y) % 100

h = (int(q) + ((26 * (int(m) + 1) // 10)) + int(k) + (int(k) // 4) + (int(j) // 4) + (5 * int(j))) % 7

if int(h) == 0:
    x = "Saturday"
elif int(h) == 1:
    x = "Sunday"
elif int(h) == 2:
    x = "Monday"
elif int(h) == 3:
    x = "Tuesday"
elif int(h) == 4:
    x = "Wednesday"
elif int(h) == 5:
    x = "Thursday"
elif int(h) == 6:
    x = "Friday"
else:
    x = "non-existent day"

print(m + "/" + q + "/" + y + " is a " + x + ".")
