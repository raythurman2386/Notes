class Animal:
    def __init__(self, age, gender):
        self.age = age
        self.gender = gender

    def __str__(self):
        return super().__str__()


class Llama(Animal):
    def __init__(self, height, is_domesticated):
        self.height = height
        self.is_domesticated = is_domesticated

        def __str__(self):
            # return f'{super().__str__()}, {self.height} in. tall'
            return f'Llama info: {Animal.super()}, {self.height} in tall, {self.is_domesticated}'


my_llama = Llama("2m", "yes")

print(my_llama.__str__())


class Book:
    def __init__(self, name, year, author_first, author_last):
        self.name = name
        self.year = year
        self.author = Author(author_first, author_last)


class Author:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __str__(self):
        return f'{self.first} {self.last}'


my_book = Book("name", 2004, "ray", "thurman")

print(my_book.author)
