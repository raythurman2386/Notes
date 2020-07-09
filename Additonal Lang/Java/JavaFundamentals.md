# Java Fundamentals

Java was originally created to make web content dynamic

- This was done through Java applets, but were very insecure
- Java is cross platform
  - Java is a compiled language
  - To run any java program, your machine must be running a Java Virtual Machine
  - JVM's are compiled to native machine language for each type of computer
  - This compiled intermediate code is called `ByteCode`

Java conceptual diagram from Oracle https://docs.oracle.com/javase/8/docs/index.html

Java has 5 primary goals

- It must be "simple, object-oriented and familiar"
  - mimics C++, a popular programming language at the time of Java's release
- It must be "robust and secure"
- It must be "architecture-neutral and portable"
- It must execute with "high performance"
- It must be "interpreted, threaded, and dynamic"

### Java Organization

Everything in Java starts with a Class, From this Class you can instantiate, make an instance of, objects. Most work is then done on these objects

```
class Car {
  data;
  behaviors();
}

// Objects - real things constructed from the Class following it's blueprint
// in the end we will have tree objects of type Car - truck, sedan, suv
// They all know the same things and can do the same things

Car truck = new Car();
Car sedan = new Car();
Car suv = new Car();
```

Java is a Strongly typed language
Meaning everything in Java has a type, which is a way to say what type of data can be stored in that memory location. Once Set the type cannot change and the value of a variable is unknown until initialized

```
int count = 1;
booleant stopIt;
```

Java arrrays are not immune to being strongly typed:

- Arrays have a fixed length predetermined before they can be used
- Arrays contain a single data element type

### Java Development

Java development is primarily done through Integrated Development Environments

Each time you change something in the source code, you will have to redo all three steps to compile and see the effects of your change:

```
javac hello/*.java
jar cvfe hellothere.jar hello.HelloWorld hello/*.class
java -jar hellothere.jar
```

And that is a complete first Java Application

## Basics of OOP

OOP is a Programming Style

A programming style is a way of organizing programs based on some conceptual model of programming. The style should include an appropriate language to make programs written in that style clear and readable. OOP specifically supports objects that are data abstractions with an interface of named operations and a hidden local state.

Objects have an associated type (Class) and classes may inherit attributes from superclasses.

To do work in Java, you must first create a Class, sometimes called a factory or a blueprint. From that class, you create, or instantiate and object.
You can create as many of the same objects as you wish, just like a factory can mass produce a product.

Classes

- Collections of objects
- Blueprint to create individual objects
- Static Fields and Methods - class level attributes and behaviors shared by all objects of the class

Objects

- An entity with state fieldsand behaviors
- Chair, person, dog - examples of a physical or logical entity upon which the program performs work
- Considered an `instance` of a class; to make an object, you instantiate it
- This is where the work in Java Happend

### 4 Pillars of OOP: Examples with Spring

#### Abstraction: Creating a class

#### Encapsulation: Creating pieces of code that do one thing well and then calling is over and over again.

- Grouping our fields and methods into classes for a single entity. Everything related to employees, data and behaviors

#### Polymorphism: We can create a sum function that takes various parameters

#### Inheritance: Abstract classes and interfaces

- Child classes can then inherit their parents characteristics and expand upon those.

### SOLID: Examples with Spring

#### SRP

- manage configuration for Swagger, interface with the employee's table, print a HelloWorld mmessage

#### OCP

- The Spring Framework is a great example. The core logic is fixed; we cannot change it. The framework does have interfaces where we can inject our own code

#### LSP

- Our abstract classes will fit this description

#### ISP

- Different interfaces for different fuctions

#### DIP

- In Spring all modules are separate entities but can be used together as Beans

Java OOP Concepts: https://www.javatpoint.com/java-oops-concepts

SOLID: https://scotch.io/bar-talk/s-o-l-i-d-the-first-five-principles-of-object-oriented-design

4 Pillars of OOP: https://howtodoinjava.com/oops/object-oriented-principles/

## Types in Java

Java has 8 different primitive data types built into the Language

- boolean
- byte
- char
- short
- int
- long
- double
- float
- double

A `String` in Java is not a primitive data type

String is actually a Class derived using the primitive type `char`. That is why String is capitalized

```
String school = "North Harrison";
```

A `;` is REQUIRED` at the end of all Java Statements

## Scope

Scope is defined as the space in the program where variables are available for use. Scope tells us in which blocks of code which variables are available. Java is very strict about the way it handles scope.

- Fields are in scope throughout the class
- Local variables are in scope from their declaration to the end of the block
- You can reuse names in different scopes, blocks
- You can enen hide the name within a scope

## Typecasting

Sometimes you have one data type but need to convert it to be another type

Changing a data type is called `typecasting`

smaller data type to larger = widening casting
larger to smaller = narrowing casting

going from a double to an int

```
int myValue = (int) 3.14;
```

## Access Modifiers

- Public - Anyone can access. You might have to use the package.class.object dot notation to access it, but you can still access it.
- Private - Can only be accessed within the class and objects instantiated from the class.
- Protected - Accessible within the same package and with the class and subclasses in other packages.
- Default - Accessible only with in the same package. For this you just leave the access modifier blank.

## Getters and Setters

- Restricting access to only those objects who are allowed to have access. Remember with public anyone can access them.
- Checking or Modifying the data prior to releasing or changing. Some data validation might be done here. Perhaps all string values should be capitalized. Perhaps negative numbers are not allowed.
- Preventing access completely. Perhaps the value is only needed within the object and the outside world should not read or modify the field.

## Constructors

Now we start a series of three constructors, three different ways to send the initial state to the class to create the object. Notice each one has the same name but has different parameters. The headers for the constructor methods all start with public Dog.

    Constructors are always public
    Unlike other methods, constructors have no type. They are always of type void meaning that they cannot return a value.
    They are named the same name as the class
    They differ by the parameter list. You can have as many different constructors as you can construct combinations of parameters.

Now this one is called the default constructor. If no constructor is specified, the JDK will automatically create this default constructor. This constructor creates an object using no parameters. In this case, all of our fields are created with uninitialized values.

## Collections

A collection is a way of storing a series of related data under one variable name. You collect the data under a single variable to make data manipulation easier. Thus you have a collection of data under one name.

- Array -- Fixed length, single element type, accessed via index
- ArrayList (One most used in Java Web Programming) -- Variable Length, single element type, accessed via index
- HashMap -- Variable length, Key/Value pair, accessed via key value
- HashSet -- Variable length, single element type, accessed via the value itself
