city = input("Enter your city name:")
temp = float(input("Enter the temperature in Celsius:"))

if temp > 30:
    print("It's a hot day in", city)
else:
    print("It's a cool day in", city)

    if temp > 25:
        print("It's a warm day in", city)
    else:
        print("It's a cold day in", city)


if temp > 35:
    print("It's a scorching day in", city)
elif temp > 25:
    print("It's a warm day in", city)
elif temp > 15:
    print("It's a mild day in", city)
else:
    print("It's a cold day in", city)

import datetime
import calendar

now = datetime.datetime.now()
print("City:", city)
print("Time now:", now)

print(calendar.calendar(now.year))