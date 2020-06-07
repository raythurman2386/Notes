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
