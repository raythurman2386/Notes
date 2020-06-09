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