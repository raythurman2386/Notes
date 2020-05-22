# Complete the timeInWords function below.
def timeInWords(h, m):
    hour_arr = [
      "one", 
      "two", 
      "three", 
      "four", 
      "five", 
      "six", 
      "seven", 
      "eight", 
      "nine", 
      "ten", 
      "eleven", 
      "twelve"
    ]

    min_dict = {
      "1": "one",
      "2": "two",
      "3": "three",
      "4": "four",
      "5": "five",
      "6": "six",
      "7": "seven",
      "8": "eight",
      "9": "nine",
      "10": "ten",
      "11": "eleven",
      "12": "twelve",
      "13": "thirteen",
      "14": "forteen",
      "15": "quarter",
      "16": "six teen",
      "17": "seven teen",
      "18": "eight teen",
      "19": "nine teen",
      "20": "twenty",
      "21": "twenty one",
      "22": "twenty two",
      "23": "twenty three",
      "24": "twenty four",
      "25": "twenty five",
      "26": "twenty six",
      "27": "twenty seven",
      "28": "twenty eight",
      "29": "twenty nine",
      "30": "half"
    }

    min_string = "o' clock"
    hour_string = hour_arr[h - 1]
    initial_str = str(m)
    remainder = str(60 - m)
    result = f"{hour_string} {min_string}"
    # Set the Hours to a string
    # If greater than 30
    # Hour is equal to the following hour
    # Convert the minutes to a string
    # if 15 min past the hour or before the new hour,
    # min_string will equal quarter past
    if initial_str in min_dict.keys() or remainder in min_dict.keys():
        if m == 1:
            min_string = min_dict[initial_str]
            result = f"{min_string} minute past {hour_string}"

        elif m in range(2, 30):
            min_string = min_dict[initial_str]
            result = f"{min_string} minutes past {hour_string}"

            if min_string == "quarter":
                result = f"{min_string} past {hour_string}"

        elif m == 30:
            min_string = min_dict[initial_str]
            result = f"{min_string} past {hour_string}"

        elif m > 30:
            hour_string = hour_arr[h]
            min_string = min_dict[remainder]
            result = f"{min_string} minutes to {hour_string}"

            if min_string == "quarter":
                result = f"{min_string} to {hour_string}"

    return result


print(timeInWords(5, 0))
