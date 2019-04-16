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