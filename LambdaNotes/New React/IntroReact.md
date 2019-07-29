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

***
