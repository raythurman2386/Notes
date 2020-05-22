min = 21
sec = 15

total_seconds = (21 * 60) + 15

print(total_seconds)


# miles in 5 kilometers
mile_in_kilo = 0.621371
miles_in_5_kilo = 5 / mile_in_kilo

print(miles_in_5_kilo)


# Pace in MPH
print((total_seconds / miles_in_5_kilo))


# Book Price
book = 19.95
discount_in_percent = .25
ship_one = 2.50
additional_shipping = 1.00
# total_copies = int(input("How many copies would you like to buy? "))
total_copies = 10

discount_amount_in_dollars = book * discount_in_percent
book_after_discount = book - discount_amount_in_dollars

total_shipping = 0.0
if total_copies > 1:
    total_shipping = ((total_copies - 1) * additional_shipping) + ship_one
else:
    total_shipping = ship_one

wholesale_cost = total_shipping + (book_after_discount * total_copies)

print(total_shipping, 'shipping')

print(book_after_discount, 'after discount')

print(wholesale_cost, 'wholesale')

#  EX 2
# do twice


def print_something(str):
    print(str)


def repeat_func(func, num, value):
    i = 0
    while i < num:
        func(value)
        i += 1


repeat_func(print_something, 5, "Hello World")
repeat_func(print_something, 10, "Kinda Cool")
repeat_func(print_something, 1, "Would Ya Look At It!")


#  EX 3
def check_fermat():
    num_one = int(input('Please enter a number: '))
    num_two = int(input('Please enter another number: '))
    num_three = int(input('Please enter one more number: '))
    fermat = int(input('Please enter one last number: '))

    if fermat > 2 and num_one**fermat + num_two**fermat == num_three**fermat:
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn\'t work')


check_fermat()
