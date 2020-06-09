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
        for category in self.categories:
            output += f'\n {str(category)}'
        return output

    def __repr__(self):
        return f"Store(Name={self.name}, Categories={self.categories})"


running_category = Category("Running", "All your running needs", [])
baseball_category = Category("Baseball", "Cards fans only", [])
basketball_category = Category("Basketball", "Hoosiers fans only", [])
football_category = Category("Football", "Colts Arena", [])

sports_store = Store(name="Athletics", categories=[
                     baseball_category, basketball_category, running_category, football_category])
produce_store = Store(name="Braums", categories=[
    "dairy", "meat", "bread", "produce"])


print(sports_store)
# print(sports_store.name)
# print(sports_store.categories)
# print(produce_store)
# print(repr(produce_store))
# print(produce_store.name)
# print(produce_store.categories)
