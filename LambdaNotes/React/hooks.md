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