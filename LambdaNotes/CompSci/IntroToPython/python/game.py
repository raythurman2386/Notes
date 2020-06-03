import random

wins, loss, ties = 0, 0, 0
print("Welcome to Rock, Paper, Scissors!")
print(f"Wins: {wins}, Ties: {ties}, losses: {loss}")
print("Please chose to continue . . .")

# Initialize Choices
computer = random.randint(1, 3)
user = input("[1] Rock [2] Paper [3] Scissors [9] Quit\n")

while not user == 9:
    pass
