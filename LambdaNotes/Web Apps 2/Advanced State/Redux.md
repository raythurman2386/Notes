# Redux

Redux is a predictable state management library for JS applications
Redux is a small, light-weight state container for use when building JS apps

#### The Store

Everything that changes withing your app will be represented by a single JS Object known as the store.
The Store contains our state for our App

##### App State is Immutable

When changes are made to our pp state we never write to our store oject. We simple clone the state object, modify the clone, and replace the original state with the new copy

##### Pure Functions change our state

Given the same input, a pure function will return the same output every time. All functions(reducers) in Redux must be pure functions.
Meaning they take in some state, and a description of what changes took place and return a copy of state

## Learn to create the Store and Connect to the app

    import { createStore } from 'redux
    const store = createStore(reducer)

You will need to import Provider from 'react-redux' and surround your app component with it

This will give your entire app access to the store

    <Provider store={store}><App /></Provider>

or

    <Provider store={createStore(reducer)}><App /></Provider>

## Connect React Components to the Redux store

To connect components to the store, we will need to use the `connect` function and `mapStateToProps` to accomplish this

Inside of the component file we will build a helper function to tell the connect function what pieces of state we want to access in each component.

This function is generally called `mapStateToProps` and it will do exactly what it says

    import { connect } from 'react-redux'

    export default connect(mapStateToProps, {})(Component)

That is how we will be required to connect our apps to the store.

    const mapStateToProps = state => {
      return {
        user: state.user,
        name: state.name
      }
    }

Connect is a high order component!

> A HOC is a function that takes in a component, extends it's functionality, and returns a component

## Write Actions and Action Creators to describe state changes

The Redux store is read only, the only way to modify app state when using Redux is by dispatching actions

We can use Action Creators and the react-redux library in order to dispatch those actions

#### Actions

Actions in Redux are packets of information that contain an action type and some data that we want associated with that action

in code, an action is simply an object with up to two properties, a `type` property and an optional `payload` property.

Each action MUST have a `type` property.

> Reducers are the only place we can update our state.

#### Action Creators

An action creator is a function that creates an action.

Or in other words an action creator is a funtion that returns an object that just happens to be an action

Action creators are a middle step between events/interactions and the dispatch process. They make it possible to write reusable functions that can create actions on the fly, rather than hard coding actions into our components

When we want to use action creators in our connected components, we first import the creator, then we must pass the creator into the connect function.

Action creators are passed to the object taht is the second argument in the first connect invocation

## Learn to write Reducers

Reducers calculate the new version of state based on the current state and a given action

When an action is dispatched it flows through all reducers.

This key principle is one of the patterns by which Redux was built.

Reducers will take in two args, the current state, and the action that is sent via the action creator.

The type of action is used to tell the reducer what needs to be done, and the payload is to tell the reducer what needs to be updated

Reducers will never update state directly, but will always return a new object

create a reducer folder inside of src with a file reducer.js

    const initialState = {
      // state goes here
    }

    export const reducer = (state = initialState, action) {
      switch(action.type) {
        default:
          return state;
      }
    }

Once your reducer is created, then you will just need to add a case for each of you action creators

- We will always return a brand new object, Redux state is immutable
- We are using the spread operator to spread in old state
- We tehn update the one piece of state we need to update
