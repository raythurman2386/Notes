# Inheritance

_`Inheritance relationships`_ can be dfined between classes in situations where more specific child classes extend the functionality of more general parent classes. These heirarchies help us write well-organized code and can allow for code re-use.

When you're attempting to solve a programming problem, you will often find an existing class that does almost what you need. If you changed the class, you could end up breaking something that used to work.

You could also create a new class and copy and paste from the old one the functionality that you want to borrow. Then you could add the new functionality, but this causes repetition and could end up creating a lot of confusion.

Instead of changing the old class and copying all attributes to a new class, you can use `inheritance` to solve your problem.

In the new class, we only need to define what we add or change from the old class.

The original class is the `Parent` class and the extended class is the `Child`

```
class Bicycle:
    def __init__(self, name):
        self.name = name


    def exclaim(self):
        print("I'm a bicycle!")


class Specialized(Bicycle):
    def __init__(self, name, specialization):
        super().__init__(name)
        self.specialization = specialization


    def exclaim(self):
        print("I am a special bicycle!")


a_bike = Bicycle()
a_specialized = Specialized()

```

By defining the`__init__` method in Specialized, we are overiding it from Bicycle. But, we still want the Bicycle portion our our child class to run its iitialization, even when instantiating a Specialized. 

Inside the child Specialized, to access the parent Bicycle's method, we use `super()`. Then after running the parent initializer, we run the Specialized specific initialization behavior.

## Association through appropriate class design

Now that you have explored inheritance relationships, we will look at another category of class relationships - _`association`_

Composition in programming is when we collect several objects together to create a new one. 

Composition is usually the the right choice when one object is part of another object. It's often said that if inheritance establishes an _`is-a`_ relationship, then composition establishes a _`has-a`_ relationship.

To illustrate, imagine you've created a `Duck` class. A duck is made up of many parts, or a duck _has_ many parts. So, a `Tail` class would not inherit from the `Duck` class, rather the duck would be composed of the tail and any other class that makes up the duck.

```
class Bill:
    def __init__(self, description):
        self.description = description

class Tail:
    def __init__(self, length):
        self.length = length

class Duck:
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail

    def about(self):
        print(f"This duck has a {self.bill.description} and a {self.tail.length} tail.")

duck = Duck(Bill('wide orange'), Tail('long'))

```

Notice how none of the classes have an inheritance relationship with the others. However, the Duck class expects to receive instances of the Bill and Tail classes when it is initialized. You can tell this is a composition relationship because you can accurately describe the program by stating that the Duck _`has a`_ Bill and Tail.

### Aggregation

Aggregation is almost exactly like composition. The difference is that aggregate objects can exist independently. It would be impossible for a bill to be associated with a different duck. But what if there was a Collar or Leash class?

A duck could have a collar or leash, and unlike bill or tail, the collar or leash could exist independently from the duck.

Another way to differentiate between aggregation and composition is to consider the object's lifespan. If the outside object controls when the inside objects are created and destroyed, composition is most suitable. 

If the related object can outlast the composition object, then an aggregate relationship makes more sense.

> Keep in mind that composition is aggregation; aggregation is just a more general form of composition. Any composite relationship is also an aggregate relationship, but the reverse is not true.