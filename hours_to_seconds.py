
# 2 hours
# 

def hoursToSeconds(hour):
    minutes = 0
    seconds = 0

    if type(hour) == float or type(hour) == int:
        count = 0
        count_seconds = 0
        # to handle minutes
        while(count != hour):
            minutes = minutes + 60
            count = count + 1

        while(count_seconds != minutes):
            seconds = seconds + 60
            count_seconds = count_seconds + 1
    else:
        print("Not a number")
    
    print(f"Minutes: {minutes}, Seconds: {seconds}")


print(hoursToSeconds(2))
print(hoursToSeconds("test"))