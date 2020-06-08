# Intro to Python 3

## Object Oriented Programming

Object oriented programming is a way of writing computer programs to use objects to model data and behaviors.
Frequently, computer programs are just a list of instructions to the computer(procedural programming), telling the computer to do certain things in certain ways.
However, in oop, computer programs make use of "objects" that talk to one another to change the data in those objects. Also, because of the way a programmer
designs an object oriented program, other parts of the program can easily reuse the code.

### The Problem with Procedural Programming

THe primary purpose of procedural programming is to break down a programming task into a collection of variables, data structures, and subroutines. This is the
first approach many programmers learn because it is simple and straighhtforward. However, when writing larger computer programs that are likely more complex,
it is easy for a procedural program to devolve into "spaghetti code"-a phrase for unstructured and difficult to maintain code

### The Four Pillars of OOP

1. Encapsulation
2. Abstraction
3. Inhheritance
4. Polymorphism

#### Encapsulation

The main point of representing an object in object oriented design is to define the objects public interface (the collection of attributes and methods that other objects can use to interact with the object) Other objects in the program need not access the inner workings of the object.

In programming, hiding the implementation details of an object is called `encapsulation`.

> One thing to note about this process is the need to design the public interface of your objects carefully. Once you've developed a large program with many interacting objects, changing the public interface can have cascading effects that are difficult to correct and keep track of. However, the benefit of encapsulation is you can change the inner workings of your objects without having negative effects on your program. For example, imagine you've carefully designed an objects public interface, but later you realize the inner workings are inefficient and are slowing down your program. You can go refactor the inner workings of that object to improve the efficiency and you won't have to chage the other objects in your program at all

#### Abstraction

In it's simplest terms, abstraction means dealing with the level of detail that is most appropriate to a task. It is important to remember that the objects in our program are not real objects. The are models of objects. A model car may look like the real thing on the outside, but the engine doesn't run and the brakes likely don't work. The model car is an abstraction of the real thing.

> One tip to achieve the right level of abstraction is to only model exactly what the system needs to perform. Don't model what the system might need. By targeting exactly what the system needs, you are more likely to achieve the correct level of abstraction for your program.

#### Inheritance

There are many types of relationships that you can model between objects. Inheritance describes the relationship where "The dog is an animal", or where "the teacher is an employee"

Inheritance is like a family tree. A person could say that they inherited their last name and their brown eyes from their grandfather. Similarly, inheritance allows our object classes to inherit attributes and methods from other classes in the program.

#### Polymorphism

Polymorphism is the ability to treat a class differently depending on which subclass is implemented.

For example, let's say we modeled a game of chess in our program. We created a Board class that can accept a move from a Player calss. Now, the Board will call a move function on the Piece class. Each of the six pieces are subclasses of the Piece class(Rook, Bishop, King, etc.) Each of the classes has a specific move method that overrides the move methods on the parent classes

So the Board class has a move method available on its interface. The Board class need not know what type of piece it is dealing with when it calls move, because the subclasses override that method. This is an example of Polymorphism.

## A starting point

A good starting point is to describe your problem in detailed sentences. Once you have some text that describes your general problem, you go through and find all of the nouns in the text. The nouns then become the classes in your program. Any verbs associated with a noun become methods on the class. Any adjectives associated with the nnoun become the attributes on the class

This can be an excellent starting point, however there are a few things to be careful of. A proficient programmer will use built in data structures until there is a need to define a class. If an object has only data, then a built in structure like a list, set, or dictionary might be more appropriate than a class. If an object only has behavior and no stored data, then defining a function may be a better choice.

## Self Documenting

When programmers first start writing object oriented code a common complaint is that they end up writing more code to accomplish the same task than they would if they just wrote simple procedural code.

One thing to note is that object oriented code although at times more verbose, often ends up being self documenting and much easier to read. Code length is not a good indicator of code complexity, and by the time we documented the procedural code, it would likely be as long as the oop version.

#### Model an online store in python

We need to design an online store where customers can purchase products from vendors. Vendors need to be able to create the products that customers can then purchase

- Users
  - Customers
  - Vendors
  - Admins
- Products
- Purchases

- Users

  - Attributes
    - name
    - isAdmin
  - Customers
    - Attributes
      - name
      - collection of purchases
  - Vendors
    - Attributes
      - name
      - collection of products
  - Admin
    - name
    - admin flag

- Products

  - Attributes
    - name
    - price
    - vendor

- Purchases
  - Attributes
    - product
    - customer
    - price
    - date and time about purchase

We also need to think about the relationship between these objects

- Sellers have products(one to many)
- Customers have purchases(one to many)
- Purchases have products(one to many)

Now we can write the code

```
from datetime import datetime

class User:
    def __init__(self, name, is_admin=False):
        self.name = name
        self.is_admin = is_admin

class Admin(User):
    def __init__(self, name):
        super().__init__(name, is_admin=True)

class Customer(User):
    def __init__(self, name):
        super().__init__(name)
        self.purchases = []

    def purchase_product(self, product):
        purchase = Purchase(product, self)
        self.purchases.append(purchase)

class Vendor(User):
    def __init__(self, name):
        super().__init__(name)
        self.products = []

    def create_product(self, product_name, product_price):
        product = Product(product_name, product_price, self)
        self.products.append(product)


class Product:
    def __init__(self, name, price, vendor):
        self.name = name
        self.price = price
        self.vendor = vendor

class Purchase:
    def __init__(self, product, customer):
        self.product = product
        self.customer = customer
        self.purchase_price = product.price
        self.purchase_data = datetime.now()
```

User is the BASE class and the others `inherit` from the User

## Defining Classes

We define the class by starting with the reserved class keyword. Then we write the name of the class and terminate the line with a colon.

> Note: PEP 8 recommends that classes be named using CamelCase notation

After the class definition, we have the contents of the class indented below. In python, indentation is used rather than braces or brackets to delimit the class definition

### Instantiating a class

`a = MyFirstClass()`

## Demonstrate Usage of **init**, **str**, and **repr**

- init
  Most oop languages have the concept of a constructor. A constructor is a special method that initializes an object when it is created

> Python is unique in that it has a constructor method and an init method. However, the constructor method is only used if you are doing something rare and exotic. We will focus on the init method here

The `self` argument is simply a reference to the object that the method is being invoked on.

- str
  The str method is spection just like the init method. The **str** method is supposed to return a string representation of an object

For example

```
def __str__(self):
    return f`{self.hour}:{self.minute}:{self.second}`
```

When you print an object python calls the str method to determine what to print out

Whenever you are difining a new class, you should start by defining the **init** method so you can instantiate objects. The next thing you should do is define the **str** method so you have useful info for debugging

- repr
  repr is similar to str, in that it will return a printable representation of the object. However, with **repr** it will return one of the ways possible to create the object

What we might really want to know is how we could recreate that object. By defining a repr method on the Point class we can do that

```
def __repr__(self):
    return 'Point(x=%s, y=%s)' % (self.x, self.y)
```

now point would print:

`Point(x=1, y=2)`

## Private Data in Python

Most oop languages have a concept of access control. This means that some attributes and methods on an object are marked private.

Python is different and does not do this. Python doesn't enforce laws that someday might get in your way. The Python way is to provide unenforced guidelines and best practices instead

It is also the convention to prefix an attribute or method with an underscore character \_. Other python programmers will see this and recognize it as a flag for an internal variable. However the interpreter will still allow direct access.

To strongly usggest that outside objects not access a property or method, we can add a double underscore prefix \_\_. This causes the interpreter to perform name mangling on the attribute. Essentially an outside object could still access the internal data, but they will have to try a bit harder to do so.

## LEGB variable scope

1. Local
2. Enclosing
3. Global
4. Builtin

The order matters. THe interpreter will first search the local, then enclosing, global and builtin

## Instance vs. Class

Some attributes and methods are part of the class itself and some are part of the objects that are created using that class as a blueprint

When looking at a class definition, if you see an initial self argument on a method, then you know that it is an instance method. The self keyword is referencing the object instance that was created from the class, not the class itself. These are the types of methods you normally write when you create your own classes. The excclaim method on the car class is a good example of a simple instance method.

Within a class definition, a preceding @classmethod decorator indicates that the following function is a class method. Also, the first param to the method is the class itself. The Python tradition is to name this parameter `cls` because class is reserved

```
>>> class Counter():
...     count = 0
...     def __init__(self):
...         Counter.count += 1
...     def exclaim(self):
...         print("I'm a Counter!")
...     @classmethod
...     def children(cls):
...         print(f"Counter class has {cls.count} instances that have been created")
...
>>> counter_one = Counter()
>>> counter_two = Counter()
>>> counter_three = Counter()
>>> Counter.children()
Counter class has 3 instances that have been created
>>>

```
