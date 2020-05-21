def time_conversion(time):
    time_arr = time.split(':')

    if "PM" in time_arr[2]:
        hour = int(time_arr[0])

        if hour == 12:
            hour = 12
        else:
            hour += 12

        minutes = time_arr[1]
        seconds = time_arr[2].replace('PM', ' ')
        print(f"{hour}:{minutes}:{seconds}".rstrip())

    else:
        hour = time_arr[0]

        if hour == "12":
            hour = "00"

        minutes = time_arr[1]
        seconds = time_arr[2].replace('AM', ' ')
        print(f"{hour}:{minutes}:{seconds}".rstrip())


time_conversion("12:05:45AM")
time_conversion("11:05:45AM")
time_conversion("01:05:45PM")
time_conversion("05:05:45AM")
time_conversion("05:05:45PM")
