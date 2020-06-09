'''
Store Lecture Walkthrough
Intro to Python 2 and 3 from the TKIT
'''


class Category:
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

    def __str__(self):
        return f"{self.name}: {self.description}"


class Store:
    # attributes
    # name
    # categories

    # constructor
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories
        self.employees = []

    def __str__(self):
        output = f"Welcome to {self.name}!"
        index = 1
        for category in self.categories:
            output += f'\n {index}. {category.name}'
            index += 1
        return output

    def __repr__(self):
        return f"Store(Name={self.name}, Categories={self.categories})"


running_category = Category("Running", "All your running needs", [])
baseball_category = Category("Baseball", "Cards fans only", [])
basketball_category = Category("Basketball", "Hoosiers fans only", [])
football_category = Category("Football", "Colts Arena", [])

sports_store = Store(name="Athletics", categories=[
                     baseball_category, basketball_category, running_category, football_category])

# REPL
# Read
print(sports_store)
print("Type q to quit")

# Evaluate
explore = True
while explore:
    choice = input("Please choose a category (#): ")
    try:
        if choice == "q":
            break

        choice = int(choice) - 1

        if choice >= 0 and choice < len(sports_store.categories):
            print(sports_store.categories[choice])
        else:
            print("That number is out of range")

    except ValueError:
        print("Please enter a valid number")
