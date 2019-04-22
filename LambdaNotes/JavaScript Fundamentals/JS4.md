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