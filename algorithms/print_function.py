if __name__ == '__main__':
    answers = {
        "num": 0,
        "start": 0,
        "count": 0
    }

    questions = [
        'Please Supply a number: ', 
        'Please Pick a Starting Point: ', 
        'What would you like to count by? '
    ]

    for key in answers.keys():
        index = 0
        if index < len(questions):

            question = questions[index]
            answers[key] = int(input(questions[index]))
            index += 1

    # n = int(input('Please Supply a number: '))
    # j = int(input('Please Pick a Starting Point: '))
    # count = int(input('What would you like to count by? '))

    i = answers["start"]
    arr = []
    strArr = []
    results = ""

    while i <= answers["num"]:
        arr.append(i)
        i += answers["count"]

    for num in arr:
       j = str(num)
       strArr.append(j)

    print("-".join(strArr))