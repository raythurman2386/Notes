# Reducer
## Learn to explain what immutability is
  Redux is built on the programming principle of immutability. This means that the Redux store cannot be mutated, which will save us from running into more bugs and weird side effects.

  > Mutable objects are objects whose state is allowed to change over time. 

  > immutable objects are the opposite, their data will not be changed

  ### Predictability
  Mutation hides change, which can create unexpected side effects. This can lead to some nasty bugs. When we enforce immutability we can keep our application architecture and mental model simple. 

  Simply put, it is very easy to predict how the state object will change based on certain actions and events

  Without immutability our state object can be changed or updated in unpredictable ways.

  ### Mutation Tracking
  Immutability makes it really easy to see if anything has changed
  
  If a user adds a task to the todo list, the todolist component will update since it is receiving new props. 

  But what if we want to run an animation on the new todo? We can't just run it on every render because it would run when the user toggles a task to complete or delete a task

  Since Redux state management is immutable, we can track the changes that happen on the state, and only run our animation when a new task is added.

  ### Redux and Immutability
  Redux has a single immutable state tree(referred to as the store) where all state changes are explicitly handled by dispatching actions.

  Dispatched actions are processed by a reducer that accepts the previous state and the action and returns the next state of you application.

  It is easy to predict how the state tree is going to change based on actions that are dispatched. 

  It is also easy to predict which action will be dispatched based on some event or interaction

  Writing immutable code can be tough

  ## Describe Reducer Functions
  A reducer is a function which takes two arguments, the current state and an action, and returns a new updated state object based on both arguments.

  More specifically, consider a function that when passed an int, would return that value + 1, without mutating the original ints value

    const initialState = 0
    const reducer = state => {
      const newState = state + 1
      return newState
    }

    const newStateValue = reducer(initialState)
    console.log(initialState, newStateValue) // 0, 1

  Consider this refactor as an example where we are using an object

    const initialState = { count: 0 }
    const reducer = state => {
      return { count: state.count + 1}
    }

  The reducer function is a pure function without any side efects. This makes a reducer the perfect fit for managing changes in state while maintaining the immutability we want in our components

  Now lets pass down some actions

    const initialState = { count: 0 }
    const reducer = (state, action) => {
      if(action.type === 'increment'){
        return { count: state.count + 1}
      } else if(action.type === 'decrement'){
        return { count: state.count - 1}
      }
    }

    reducer(initialState, { type: 'increment' });
    reducer(initialState, { type: 'decrement' });

  We can also add a payload property to our action objects(sometimes called data) If our reducer needs to have some data passed into it through the action to be able to update the state correctly

    const initialState = { name: 'Donald Duck' }
    const reducer = (state, action) => {
      if(action.type === 'changeName'){
        return { name: action.payload}
      }
    }

    reducer(initialState, { type: 'changeName', payload: 'Mickey Mouse' })

  Lets refactor this to use a switch statement

    const initialState = { count: 0 }
    const reducer = (state, action) => {
      switch(action.type) {
        case 'increment':
          return { count: state.count + 1}
        case 'decrement':
          return { count: state.count - 1}
        default:
          return state
      }
    }

  ## Learn to employ the `useReducer` hook to manage state
  The `useReducer` hook is an alternative to useState, and is preferable when you have complex logic that you have to deal with in a component.

  When we call `useReducer` it will take in a reducer function that we build, as well as a value for the initialState

  Then it will return the current state and a dispatch method in an array

    const [state, dispatch] = useReducer(reducer, initialState)

  The dispatch method is the big addition to our arsenal here.

  It will dispatch any action to our reducer when specific events occur in our application

    import React, { useReducer } from 'react'

    const initialState = { count: 0 }
    // Initial count is established

    // We will use the same reducer we created in the previous section
    function reducer(state, action) {
      switch (action.type) {
        case 'INCREASE':
          return { count: state.count + 1 }
        case 'DECREASE':
          return { count: state.count - 1 }
        default:
          return state
      }
    }

    // Create a functional component
    function Counter() {
      // Use the useReducer hook by destructuring its two properties: state, and dispatch and pass in the reducer and the initialState to the useReducer function
      const [state, dispatch] = useReducer(reducer, initialState)

      // Return JSX that displays the count for the user
      // Note the two button elements which allow the user to increase and decrease the count.  Each of them contains an onClick event that dispatches the desired action object, with its given type.  Each action, when fired, is dispatched to the reducer and the appropriate logic is applied.
      return (
        <>
          {/* Note, we have access to the current state and the dispatch method from the useReducer hook, so we can utilize them to display the count as well as couple the dispatching of the actions from the appropriate buttons.*/}
          <div className="count">Count: {state.count}</div>
          <button onClick={() => dispatch({ type: 'INCREASE' })}>+1</button>
          <button onClick={() => dispatch({ type: 'DECREASE' })}>-1</button>
        </>
      )
    }