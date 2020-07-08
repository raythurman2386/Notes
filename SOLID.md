# SOLID

- Single Responsibility Principle
- Open/Closed Principle
- Lishkov sustitution principle
- Interface segregation principle
- Dependency inversion principle

## The Single Responsibility Principle

- A class should only do one thing, have a single responsibility, a single job - manage configuration for Swagger, interface with the employees table, print a HelloWorld message

The single responsibility principle states that each of our classes has to be only used for one purpose

We need this so that we don't have to change code as often when something changes. It's also hard to understand what the class is doing if it's doing many things

An example of following the SRP is as follows:

```
class Rectangle {
  constructor(length, width) {
    this.length = length;
    this.width = width;
  }

  getArea() {
    return this.length * this.width;
  }
}
```

## The Open/Closed Principle

- Objects are open for extension but closed for modification
- Open says you can add fields (behaviors) by inheriting from the class
- Closed says the other entities can rely on the object's structure through implementation of a standard interface

The open/closed principle states that a piece of software is open for extension, but closed for modification

This means that we should be able to add more functionality without changing existing code.

For example:

```
class Rectangle {
  constructor(length, width) {
  this.length = length;
  this.width = width;
  }

  getArea() {
    return this.length * this.width;
  }

  getPerimeter() {
    return 2 * (this.length + this.width);
  }
}
```

As you can see, the existing code did not have to be changed to extend the functionality

## Liskov Substitution Principle

- Objects can be replaced with subtypes without alternating the correctness of the program. Subtypes should do at least what their parents do

This principle states that if we have a parent class and a child class, then we can interchange the parent and child class without getting incorrect results.

This means that the child class must implement everything that's in the parent class.

For example, if we want to implement classes for a bunch of shapes, we can have a parent Shape class, which are extended by all classes by implementing everything in the Shape class.

```
class Shape {
  getArea() {
    return 0;
  }
}

class Rectangle extends Shape {
  constructor(length, width) {
    super();
    this.length = length;
    this.width = width;
  }

  getArea() {
    return this.length * this.width;
  }
}

class Square extends Shape {
  constructor(length) {
    super();
    this.length = length;
  }

  getArea() {
    return this.length ** 2;
  }
}

class Circle extends Shape {
  constructor(radius) {
    super();
    this.radius = radius;
  }

  getArea() {
    return Math.PI * (this.radius ** 2);
  }
}

const shapes = [
  new Rectangle(1, 2),
  new Square(1, 2),
  new Circle(2)
]

for(let shape of shapes) {
  console.log(shape.getArea)
}
```

## Interface Segregation Principle

- Just implement what you need; many interfaces are better than a huge general one

The interface segregation principle states that "clients shouldn't be forced to depend on interfaces that they don't use."

This means that we shouldn't impose the implementation of something if it's not needed.

JavaScript doesn't have interfaces, so this principle doesn't apply directly since it doesn't enforce the implementation of anything via interfaces.

## Dependency Inversion Principle

- Abstract as much as possible "Entities must depend on abstractions not on concretions". Higher level classes must not depend on lower classes. Modules are all separate entities that can be tied together using some abstract layer.

This principle states that high-level modules shouldn't depend on low-level modules and they both should depend on abstractions, and abstractions shouldn't depend upon details. Details should depend upon those abstractions.

This means that we shouldn't have to know any implementation details of our dependencies, if we do, then we violated this principle.

We need this principle because if we do have to reference our code for the implementation details of a dependency to use it, then when the dep changes, there will be lots of breaking changes.

As software gets more complex, if we don't follow this principle, then our code will break a lot.

```
class ClassA {}

class ClassB {}

class ClassC {}

class Facade {
  constructor() {
    this.a = new ClassA();
    this.b = new ClassB();
    this.c = new ClassC();
  }
}

class Foo {
  constructor() {
    this.facade = new Facade();
  }
}
```

We don’t have to worry about ClassA , ClassB and ClassC to implement the Foo class. As long as the Facade class doesn’t change, we don’t have to change our own code.

## Conclusion

We should follow the SOLID principle to write code that’s easy to maintain.

To following SOLID, we have to write classes that only do one thing.

Our code has to open for extension but closed for modification. This reduces the chance of messing up the existing code.

Parent and child classes have to be interchangeable when we switch them. When we switch them, the result still has to be correct.

Finally, we should never have to depend on the implementation details of any piece of code that we reference so that we won’t end up with lots of breaking changes when something changes.

This lets us reduce the coupling between modules.
