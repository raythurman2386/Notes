# Classes in React
  Main differences between functional(dumb) components and class(smart) components is that class components have access to state and the Component Lifecycle.

  These methods(known as life cycle hooks) give us control into how our components work, and if we'd like to use them, we have to build out a class component that `extends` the `React.Component` parent class.

    class FooComponent extends React.Component {}

  One of the integral parts of creating components as classes is that you have the ability to set up a data object that your component might need to be concerned with.

  This is done by using `state` as we call it and setting that object up on our constructor method.

  [ ] First: declare your `class component` by extending the `React.Component` parent class. `class FooComponent extends React.Component {}`

  [ ] Second: Use the `constructor` function to set up some state. Since we are calling `extends` we also need to call `super()` otherwise we won't have access to `this`

  [ ] Third: We need to render some sort of UI to the DOM. We do this by calling the life-cycle method called `render`

    class FooComponent extends React.Component {
      constructor(){
        Super();
        this.state = {};
      }
      render() {
        return <div>Hello, I am Foo Component</div>
      }
    }

# Share data between components
  state is the heart of any React Application

  State is the data that we have when we need it

  Stored on the constructor

  Its just an object that we can reference on the this keyword

  As long as the component is mounted you will have access to state

  state is mutable

  Can be changed by the `setState` method