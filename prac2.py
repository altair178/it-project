def time_determiner():
    time = int(input("enter the time: "))
    if time >= 5 and time < 11:
        print("It is morning")
    elif time >= 12 and time < 16:
        print("It is afternoon")
    elif time >= 17 and time < 20:
        print("It is evening")
    elif time >= 21 and time <= 4:
        print("It is night")
    else:
        print("Enter time in 0-24 format")
time_determiner()