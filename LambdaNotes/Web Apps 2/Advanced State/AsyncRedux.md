# Async Redux
## Finite State Machines
  A state machine is a mathematical model of computation
  A machine can have a finite number of states, but it is only in one state at a given time.
  There are different types of state machines, but for building UI's (and understanding Redux) we'll concentrate on the type that has an initial state and the next state is calculated based on input and the current state.

  A State Machine has:
  - Initial State(store)
  - Current State(store)
  - inputs or actions(action creators) that trigger transitions(reducers) to the next state

  Redux is not a finite state machine, but the thinking in states helps our understanding of how redux works 

## Redux Middleware
  Middleware is a common tool used in programming.
  You will see middleware used heavily when you start learning about NodeJS.

  Middleware will intercept every action <strong>Before</strong> it flows through to the Reducers

  Middleware can:
  - stop actions
  - forward an action untouched
  - dispatch a different action
  - dispatch multiple actions

  > Possible local storage solution
  > https://github.com/elgerlambert/redux-localstorage

## Redux-Thunk
  In Redux, Reducers are synchronous by default. If we need to perform async operations, they need to happen before the actions flow through the reducers stack.

  We can use middleware to handle async requests

  Redux Thunk is a middleware created by Dan Abramov, that provides the ability to handle async operations inside our Action Creators

  Redux Thunk is a separate node package called redux-thunk.

  Since the Redux action -> reducer flow is synchronous, we will use thunk to make the flow asynchronous so we can make API calls from our action creators.

  A `thunk` is another word for a function. But it's not just any old function. It is a special (and uncommon) name for a function that's returned by another

    function not_a_thunk() {
      // this one is a 'thunk' because it defers work for later
      return function() {
        console.log('do stuff now')
      }
    }

  When an action creator is called, redux-thunk will intercept and look at what is returned. 

  If the thing returned is an action, it will forward the action through to the reducer.

  But if the thing returned is a function, aka a `thunk` then it will invoke that function and pass in the dispatch function as an argument to it.

    const logInUser = (creds) => (dispatch) => {
      return axios.post('./login', creds).then(res => {
        const loggedInAction = { type: USER_LOGGED_IN, payload: res.data.user}
        dispatch(loggedInAction)
      })
    }