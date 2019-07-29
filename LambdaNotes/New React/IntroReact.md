# Anatomy of a React Component

    import React from 'react';
    const Intro =() => {
      return (
        <div>
          <h1>Hi Lambda!</h1>  // JSX
        </div>
      )
    }

    const Intro () => {
      const greeting = "Hi Lambda!";
      return (
        <div>
          <h1>{ greeting }</h1>  // JSX
        </div>
      )
    }

# React Components and State
  In computer programming `the separation of concerns` refers to a design philosophy that each piece of you code should do one and only one thing.

  Functions with a lot of moving parts are hard to debug

  Standard way
    <button class="button"></button>

    let button = document.querySelector('.button');
    button.addEventListener("click", (data)=>{...logic})

  React Way
    <button onClick={() => submitForm(data)} >

# Imperative Programming vs Declarative Programming

    let myArray = [1,2,3,4,5];

  Iterate and Double

    for(let i = 0; i < myArray.length; i++){
      myArray[i] = myArray[i] * 2;
    }

  or:

    const double = (number) => {
      return number * 2;
    }

    myArray.map(double);

  The first approach is an example of imperative code, and this is the kind of approach we're most familiar with.

  The problem with imperative code is it's pretty abstruse and in more complex examples can be harder to understand the code

  The second approach is an example of declarative code. 

  With practice declarative code is easier to parse.

  Most of your time as a developer will be spent reading other's code and trying to understand it instead of always writing new code.

# State in React
  Web apps are basically comprsed of data(state), and things that change that data, or state.

    import React from "react";
    import { render } from "react-dom";
    import "./styles.css";

    const white = "https://image.flaticon.com/icons/png/512/32/32177.png";
    const yellow = "https://i.pinimg.com/originals/92/94/ba/9294badee7b8f3d93fa9bc6c874641b2.png";

    function App(){
      return (
        <div className="App">
          <img src={ white }>
          <img src={ yellow }>
        </div>
      )
    }

  This Displays both lights, not quite the solution that we're looking for to turn the light on and off

    import React, { useState } from 'react';

    const white = "https://image.flaticon.com/icons/png/512/32/32177.png";
    const yellow = "https://i.pinimg.com/originals/92/94/ba/9294badee7b8f3d93fa9bc6c874641b2.png";

    function App(){
      const [ lightOn, setLightOn ] = useState(false);

      return (
        <div className="App">
          <img src={ white }>
          <img src={ yellow }>
        </div>
      )
    }
  
  the `useState` hook above works like:

  `lightOn` is a variable the value of which is whatever we passed in to `useState`. In this case it's value is the boolean primitive `false`. `setLightOn` is a function that will change the value of `lightOn`. We'll also note that I could have named these items whatever we wanted. 

# Conditional Rendering
  Conditional rendering is a fancy name for a very common pattern in React. We don't want to see both lightbulbs at once. We only want to <strong>render</strong> one or the other on the basis of some <strong>condition</strong>. In this case if the `lightOn` boolean is `false` we want to see the white bulb.

    import React, { useState } from 'react';

    const white = "https://image.flaticon.com/icons/png/512/32/32177.png";
    const yellow = "https://i.pinimg.com/originals/92/94/ba/9294badee7b8f3d93fa9bc6c874641b2.png";

    function App(){
      const [ lightOn, setLightOn ] = useState(false);

      return (
        <div onClick={()=>setLightOn(!lightOn)} className="app">
          {lightOn === false ? <img src={white} /> : <img src={yellow} />}
        </div>
      )
    }

# Intro to React Challenge
  Clicker App that keeps track of how many times you click a button

    function App(){
      const [count, setCount] = useState(0);

      return (
        <div className="app">
          <h1>{ count }</h1>
          <button onClick={()=> setCount(count + 1)}>Add</button>
          <button onClick={count === 0 ? count : setCount(count - 1)}>Subtract</button>
          <button onClick={setCount(0)}>Reset</button>
        </div>
      )
    }
***
