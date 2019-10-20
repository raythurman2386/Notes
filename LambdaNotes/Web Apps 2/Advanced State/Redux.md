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
