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

Callback Functions
    Functions that are passed into other functions as arguments. And the concept is commonly used throughout JS.

    Functions are like any other type, and they can be passed around as arguments to other functions.


    const elements = ['earth', 'wind', 'fire', 'water'];
    function showFirst(array, callback){
        callback(array[0]);
    }
    showFirst(elements, (firstItem) => {
        alert(firstItem);
    });

    function showLength(array, callback){
        callback(array.length);
    }
    showLength(elements, (length) => {
        alert(length);
    });

    elements.forEach(element => alert(element));

THE BIGGEST DIFFERNCE BETWEEN FOREACH AND MAP, IS THAT MAP RETURNS A NEW ARRAY OF ELEMENTS WHILE IN TURN PASSING EACH ELEMENT BACK TO THE CALLBACK.

    const newArray = elements.map(item => 'Element: ' + item);


ARRAY METHODS
const data = [
  {"city":"seattle", "state":"WA", "population":652405, "land_area":83.9},
  {"city":"new york", "state":"NY", "population":8405837, "land_area":302.6},
  {"city":"boston", "state":"MA", "population":645966, "land_area":48.3},
  {"city":"kansas city", "state":"MO", "population":467007, "land_area":315}
];

.map
    const cityStates = [];
    for(let i = 0; i < data.length; i++){
        let mappedObj = {};
        mappedObj.city = data[i].city;
        mappedObj.state = data[i].state;
        cityStates.push(mappedObj);
        mappedObj = {};
    }
            OR
    const mappedCityStates = data.map(state => {'city': state.city, 'state': state.state});
    const mappedCityStates = data.map((state, index, data) => {'city': state.city, 'state': state.state});

.filter
    const largeStates = [];
    for(let i = 0; i < data.length; i++){
        if(data[i].population >= 650000){
            largeStates.push(data[i]);
        }
    }
            OR
    const filterLargeStates = data.filter(state => state.population >= 650000);

.reduce 
    let statePopulations = 0;
    for(let i = 0; i < data.length; i++){
        statePopulations += data[i].population;
    }

            OR
    const reduceStatePopulations = data.reduce((total, state) => {return total += state.population}, 0);