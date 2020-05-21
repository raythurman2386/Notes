def grade_students(grades):
    updated_grades = []

    for grade in grades:
        if grade < 38 or grade % 5 < 3:
            updated_grades.append(grade)
        else:
            updated_grades.append(grade + (5 - (grade % 5)))

    return updated_grades


print(grade_students([73, 67, 38, 33]))

# CamelCase
print(sum(map(str.isupper, input())) + 1)
