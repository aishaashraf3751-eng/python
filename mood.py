name = input("Enter your name: ")
mood = input("How are you feeling today? happy, sad, excited, or tired?: ")

energy_level = int(input("Enter your energy level (1-10): "))
if energy_level < 4:
    print("You might want to take it easy today, " + name + ".")

else:
    if energy_level < 7:
        print("You have a moderate energy level today, " + name + ". Keep going!")


if mood== "happy":
    print("That's great to hear, " + name + "! Keep smiling!")
elif mood== "sad":
    print("I'm sorry to hear that, " + name + ". I hope things get better soon.")
elif mood== "excited":
    print("That's awesome, " + name + "! What are you excited about?")
elif mood== "tired":
    print("You should get some rest, " + name + ". Take care of yourself.")
else:
    print("I'm not sure what you mean, " + name + ". Please try again.")

import datetime

import calendar

now = datetime.datetime.now()
city = input("Enter your city: ")
print("City:", city)
print("Time now:", now)

print(calendar.calendar(now.year))

