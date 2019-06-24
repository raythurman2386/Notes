# React Hooks
  useState is the first hook that we will look into

      import React, { useState } from 'react';

      function Example() {
        // Declare a new state variable, which we'll call "count"
        const [count, setCount] = useState(0);

        return (
          <div>
            <p>You clicked {count} times</p>
            <button onClick={ () => setCount( count + 1 ) }>
              Click Me
            </button>
          </div>
        )
      }

  Hooks don't replace the knowledge of core React concepts. Instead hooks provide a more direct API to the React concepts you already know: props, state, context, refs, and lifecycle.

  Hooks solve a weide variety of seemingly unconnected problems in React that we've encountered over five years of writing and maintaining tens of thousands of components.

  React doesn't offer a way to "attach" reusable behavior to a component(for example, connecting it to a store). 

  With hooks you can extract stateful logic from a component so it can be tested independently and reused.

  Hooks allow you to reuse stateful logic without changing your component hierarchy.

# Hooks At a Glance
  Hooks are backwards-compatible. 
  The only argument to useState is the initial state. In the example at the top it is 0 because our counter starts from zero. 
    Note that unlike this.state, the state here doesn't have to be an object, although it can be if you want. The initial state argument is only used during the first render.

# Declaring Multiple state variables

    function ExampleWithManyStates() {
      const [age, setAge] = useState(42);
      const [fruit, setFruit] = useState('banana');
      const [todos, setTodos] = useState([{ text: 'Learn Hooks' }]);
    }

  These names aren't a part of the useState API. Instead, React assumes that if you call useState many times, you do it in the same order during every render.

# What is a Hook
  Hooks are functions that let you 'hook' into React state and lifecycle features from function components. 
  Hooks don't work insideclasses -- they let you use React without classes. (We don't recommend rewriting your existing components overnight but you can start using Hooks in the new ones)

  React provides a few built-in Hooks like useState. You can also create your own Hooks to reuse stateful behavior between different components. s