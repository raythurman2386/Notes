def grade_students(grades):

    for grade in grades:
        if grade < 38 or grade % 5 < 3:
            return grade
        else:
            return grade + (5 - (grade % 5))


print(grade_students([73, 67, 38, 33]))

# CamelCase
print(sum(map(str.isupper, input())) + 1)
