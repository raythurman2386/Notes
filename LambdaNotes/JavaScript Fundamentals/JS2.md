Closure
    Closure is a big part of the JavaScript language and needs to be discussed.

    The two types of scope in JS is global and local
        Global everything has access too.
        Local is only accessible inside it's current block of code.

        const counter = () => {
            let count = 0;
            return function (){
                count++;
                return count;
            }
        }
        const newCounter = counter();
        console.log(newCounter());

        let val = 7;
        function createAdder(){
            function addNumbers(a, b){
                let ret = a + b;
                return ret;
            }
            return addNumbers;
        }
        let adder = createAdder();
        let sum = adder(val, 8)
        console.log('example of function returning a function: ', sum);

    Closures are functions that refer to independent variables. In other words, the function defined in the closure 'remembers'  the environment in which it was created.

    Free variables are variables that are neither locally declared nor passed as parameter.
        function numberGenerator(){
            // Local "free" variable that ends up within the closure
            var num = 1;
            function checkNumber(){
                console.log(num);
            }
            num++;
            return checkNumber;
        }
        var number = numberGenerator();
        number(); // 2

        function sayHello(){
            var say = function(){ console.log(hello); }

            // Local var that ends up within the closure
            var hello = 'Hello, world!';
            return say;
        }
        var sayHelloClosure = sayHello();
        sayHelloClosure(); // 'Hello, world!'

        // Global Execution Context
        var x = 10;
        function foo() {
            // Execution Context (foo)
            var y = 20; // Free Variable

            function bar(){
                // Execution Context (bar)
                var z = 15; // Free Variable
                var output = x + y + z;
                return output;
            }
            return bar;
        }

        AT ANY POINT IN TIME, THERE CAN ONLY BE ONE EXECUTION CONTEXT RUNNING
        
