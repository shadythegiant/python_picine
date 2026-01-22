def ft_water_reminder():
    daysTowater = int(input("Days since last watering:"))
    if daysTowater > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
