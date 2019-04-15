Functions 
    functions are the foundation for all web interactions. 

    Basic Function Syntax
        The function keyword
        the name of the function
        an optional list of parameters
        the statements inside of the block of code {}

        function add(a,b){
            return a + b;
        }
        console.log(add(2,4));

    Function Invocation, Arguments, and Parameters
        When we invoke (or call) a function, we often pass in values. These are known as arguments.
        Those arguments are then received into the parameters of the function, a and b in the order they were called.

        Arguments are values that are passed into functions that receive them as parameters.

    Return Statement
        When a return statement is in a block of code, anything written after the return will not execute. Return ends the function.

    Function declaration hosting
        JavaScript utilizes a two pass compiler when executing lines of code. This means anytime we run JS in the browser, there are two passes the browser will take ouver our code.

        The first pass is setting up references to all of our code. 

        The second pass applies the values to the references that were found.

        Function Declarations are defined in the first pass.

        This means that function declarations can be invoked before they are defined
        Such as:

            console.log(add(2,4));

            function add(a,b){
                return a + b;
            }

    Function Expressions
        Function expressions have unique differences when compared agains function declarations
            A variable is used to store the function for later use
            Anonymous functions are used
            Function expressions are not hoisted. They can only be invoked after a definition has been placed in the execution stack

            const add = function(a,b){
                return a + b;
            }
            console.log(add(2,4));

    Arrow Function Expressions
        Arrow functions are a major feature introduced in ES6, these CANNOT be used with the 'this' keyword

            const add = (a,b) => {return a + b};

            console.log(add(2,4));

            const add = (a,b) => a + b;

        The keyword return is implied in an arrow function

        When not to use Arrow functions
            Event handlers
            Object methods
            Prototype Metheds
            Anytime you need to use arguments Object

Var, Let, and Const
    When a variable is declared with var, it can be mistakenly overriden, let and const cannot be overriden.

    But let is mutable meaning we can change the value that let points to 
        for example

        let name = 'Batman';
        let name = 'Robin';  <-- this will not work

        name = 'Robin'; <-- This will work

    A Const variable cannot be overriden or re-assigned

    Var - can be reassigned and overriden
    Let - can be reassigned but not overriden
    const - cannot be reassigned or overriden

    Lambda rule of thumb - Use const until you cannot, then use let

    var is function scoped

    let & const are block scoped

        function scoped means it is only available inside of the function that they are created in.

        Globally scoped are made outside of a function and available to the entire document

        Anytime you see { Curly Brackets } that is a block

Object Literals
    Objects are used all over in JavaScript
    Everything in JS is an object.
    Objects are used almost in every single part of the JS language

    Object Properties
        Objects are used as a way to store data and give the programmer access to that data when needed.
        This ability to store and call data is known as a property
        Object Properties are key:value pairs

            const myPersonalObject = {
                firstName: 'Fred',
                lastName: 'Flintstone',
            };

        dot notation = myPersonalObject.firstName // 'Fred'
        Bracket notation = myPersonalObject["firstName"] // 'Fred'

        to change a property just pass it a new value, such as
        myPersonalObject.firstName = 'Wilma';

        an objects values are MUTABLE, meaning the values can be changed.

        Object Methods
            Object.keys() -> Gives us an array back of the Objects properties/keys

            Object.values() -> Gives us an array of all the objects values

            Object.entries() -> Gives us an array of the objects key/value pairs as a tuple
