import os
import random
import re
import sys

# Should print Bon Appetit if the bill is fairly split
# else it should print the integer amount of money that Brian owes Anna

# bill: array of integers representing the cost of each item ordered
# k: an integer representing the zero-based index of the item anna doesn't eat
# b: the amount of money that Anna contributed to the bill

# Complete the bonAppetit function below.


def bon_appetit(bill, k, b):
    anna_total = sum(bill) - bill[k]
    if anna_total/2 == b:
        print("Bon Appetit")
    else:
        print(b - (anna_total//2))


bon_appetit([2, 4, 6], 1, 8)
