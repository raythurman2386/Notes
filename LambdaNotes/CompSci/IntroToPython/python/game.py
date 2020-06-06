import random


# Add ability to load saved data
def load_game():
    with open("history.txt", "r") as f:
        history = f.read().split(',')
    return history


# Add ability to save data
def save_game(w, t, l):
    with open("history.txt", 'w') as f:
        f.write(f"{w}, {t}, {l}")


# Print the score
def print_score(w, t, l):
    print(f"Wins: {w}, Ties: {t}, losses: {l}\n")
    print("Please choose to continue . . .")


def user_choice():
    return int(input("[1] Rock [2] Paper [3] Scissors [9] Quit\n"))


def comp_choice():
    return random.randint(1, 3)



# Initialize Game
results = load_game()
wins, loss, ties = int(results[0]), int(results[1]), int(results[2])
print("Welcome to Rock, Paper, Scissors!")
print_score(wins, ties, loss)
computer = comp_choice()
user = user_choice()

while not user == 9:
    # User chooses rock
    if user == 1:
        if computer == 1:
            print('Computer chose rock. . . tie!')
            ties += 1
        elif computer == 2:
            print('Computer chose paper. . .Computer wins!')
            loss += 1
        else:
            print('Computer chose scissors. . .You win!!')
            wins += 1

    # User chooses paper
    elif user == 2:
        if computer == 1:
            print('Computer chose rock. . . You Win!')
            wins += 1
        elif computer == 2:
            print('Computer chose paper. . .tie!')
            ties += 1
        else:
            print('Computer chose scissors. . .Computer Wins!!')
            loss += 1

    # User chooses scissors
    elif user == 3:
        if computer == 1:
            print('Computer chose rock. . . Computer wins!')
            loss += 1
        elif computer == 2:
            print('Computer chose paper. . .You win!')
            wins += 1
        else:
            print('Computer chose scissors. . .tie!')
            ties += 1
    else:
        print('Please choose only 1, 2, or 3 for rock, paper, or scissors')

    print_score(wins, ties, loss)
    computer = comp_choice()
    user = user_choice()

save_game(wins, ties, loss)
