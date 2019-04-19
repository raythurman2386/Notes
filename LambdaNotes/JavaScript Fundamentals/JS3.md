THIS Keyword *********************************************************************************************** 
A pronoun to use in place of an object

4 Principles
  --When in the global scope, the value of 'this' will be the window/console Object;
    
    function sayName(name){
      console.log(this);
      return name;
    }
    sayName("D'Artagnan");

  --Implicit Binding - Whenever a function is called by a preceding dot, the object before that dot is this
    
    const myObj = {
      greeting: 'Hello';
      sayHello: function(name){
        console.log(`${this.greeting} my name is ${name}`);
        console.log(this);
      }
    }
    myObj.sayHello('Ryan');

    const sayNameFunc = obj => {
    obj.sayName = function() {
      console.log(`Hello my name is ${this.name}`);
      console.log(this);
      };
    };
    const me = { name: 'Ryan' };
    const you = { name: 'Freddy' };
    sayNameFunc(me);
    sayNameFunc(you);

    // Invoke Methods on our objects
    me.sayName();
    you.sayName();

  --New binding - Whenever a constructor function is used, 'this' refers to the specific instance of the object that is created and returned by the constructor function

      A constructor function is a function that returns an object. It is an object creator.

      function CordialPerson(greeter) {
        this.greeting = 'Hello ';
        this.greeter = greeter;
        this.speak = function() {
          console.log(this.greeting + this.greeter);
          console.log(this);
        };
      }

      const jerry = new CordialPerson('Newman');
      const newman = new CordialPerson('Jerry');

      jerry.speak();
      newman.speak();

  --Explicit Binding - Whenever JS's call or apply method is used, 'this' is explicitly defined.
      jerry.speak.call(newman); newman.speak.apply(jerry);


CONSTRUCTORS ************************************************************************************************
  The constructor function is a way that we can build objects

    function Animal(object){        // Constructors are capitalized for best practices
      this.name = object.name;
      this.age = object.age;
    }

  A constructor function, constructs objects. It can be thought of as a template for the design of the object. The function itself needs to take in an object literal of some sort so that it can map that object literal's properties to a new object that will be returned once instantiated.

    function Person(attributes){
      this.age = attributes.age;
      this.name = attributes.name;
      this.hometown = attributes.homeTown;
      this.speak = function() {
        return `Hello, my name is ${this.name}.`;
      };
    }
  Now that the constructor is in place, we can use it to create a 'new' Person.
    when 'new' is called, the constructor can essentially create a context for a 'this' object

    const fred = new Person({
      age: 35,
      name: 'Fred',
      homeTown: 'Bedrock',
    });
    console.log(fred); console.log(fred.speak());

  This shows how speak was inherited from the Person object and showcases that we are using inheritance and introduces how we can use prototypes in JS

PROTOTYPES **********************************************************************************************
