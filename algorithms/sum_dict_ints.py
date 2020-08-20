"""
Given an object/dictionary with keys and values that consist of 
both strings and integers, design an algorithm to calculate and 
return the sum of all of the numeric values.
For example, given the following object/dictionary as input:
{
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}
Your algorithm should return 41, the sum of the values 23 and 18.
You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing 
any code. Run through the UPER problem solving framework while going 
through your thought process.
"""

# initialize a total variable
# loop through the items of the dict
# check the type of the value "str" or "int"
# if the type is an int
# add to the total


def sum_values(my_dict):
    total = 0
    for value in my_dict.values():
        if type(value) == int:
            total += value

    return total


d = {
    "cat": "bob",
    "dog": 23,
    19: 18,
    90: "fish"
}

print(sum_values(d))
