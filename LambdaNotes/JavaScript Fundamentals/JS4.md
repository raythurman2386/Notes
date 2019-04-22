/**************************************************** JS Classes ********************************************/
The Class keyword is what they call syntactic sugar on top of the Object built into JavaScript and the Objects prototype system.

The Class keyword is not a new way of achieving object oriented inheritance.
Classes in JS are nothing more than special functions

Class Declarations & Class Expressions
  Right now we will just be dealing with Class Declarations

    class Rectangle {
      constructor(height, width){
        this.height = height;
        this.width = width;
      }
    }
  
  Classes will return us Objects
  Declare a new Rectangle and log the result
    
    const newRect = new Rectangle(400, 800);
    console.log(newRect);

/******************************************* Class Inheritance ***************************************/
  Inheritance is where classes really shine. THe extends keyword, and super(); function make it trivial to bind our classes together.

  extends will abstract away any of the class.call syntax that we used in the last project
  super() is used to tell a parent's constructor to be concerned with the child's attributes vis versa and abstracts away the     
    Object.create syntax we used in the last project  

  Here's how Object inheritance works with classes:

    class Animal {
      constructor(name){
        this.name = name;
      }

      speak(){
        console.log(`${this.name} makes a noise.`);
      }
    }
  the Speak method will live on the object's prototype instead of on the object

  Here is a sub-class from this animal class

    class Dog extends Animal {
      constructor(name){
        super(name);
      }

      speak(){
        console.log(`${this.name} barks.`);
      }
    }

/**************************** Converting Constructors to Classes ***************************/

  All methods attached to the class body will be stored on the Objects prototype in a special way. There is a bit more magic here than just Object.create; and Class.call; but now that we know this, we can accept that the class keyword does this gloriously for us.

  The extends keyword is used to extend a parent object. A clue to find out if a class is a sub-class is to look for extends.

  Finally, IF you're going to use extends, super() needs to be called from within the constructor function. This is to pass any new attributes back up to the constructor of the parent object.

  Examples: 

    function Person(attributes) {
      this.age = attributes.age;
      this.name = attributes.name;
      this.homeTown = attributes.homeTown;
    }

    Person.prototype.speak = function () {
      return `Hello, my name is ${this.name}`;
    };

  Becomes:

    class Person {
      constructor(attr){
        this.age = attr.age;
        this.name = attr.name;
        this.homeTown = attr.homeTown;
      }

      speak(){
        return `Hello, my name is ${this.name}`;
      }
    }

  Concepts to go over.

  Speak is now assigned to the object’s prototype. (Pop open the console and show this off after you instanciate an object.)

  This is a single class, meaning it is not extending a parent class. We’ll get to extends in a min.

  Point out how clean the code now looks! Instead of having to reference the objects prototype over and over to create methods on it, you can simply add them to the class body. This is how we use classes today.. point out here that they’ll get plenty of time to use this when they get to React. React uses classes all the time.

  Now, where this comes in handy is when we have children objects that will be sub-classes of their parents. We accomplished this in the previous module with Child

    function Child(childAttrs) {
      Person.call(this, childAttrs); // this is the special sauce
      this.isChild = childAttrs.isChild; // this will be a special attribute to Child
    }

    Child.prototype.checkIfChild = function() {
      if(this.isChild) {
        console.log(`${this.speak} and I am a child object`);
      }
    };
  
  Becomes:

    class Child extends Parent {
      constructor(childAttr){
        super(childAttr);
        this.isChild = childAttr.isChild;
      }

      checkIfChild(){
        if(this.isChild){
          console.log(`${this.speak} and I am a child object.`);
        }
      }
    }

  And Now we can make our Fred and Pebbles objects.

    const fred = new Person({
      age: 35,
      name: 'Fred',
      homeTown: 'Bedrock',
    });

    const pebbles = new Child({
      age: 3,
      name: 'Pebbles',
      homeTown: 'Bedrock',
    });