# Create/Read/Update State
  State is mutable
  All changes to the state object must be done through the setState function
  All components are stateless unless there is a state object in them.
  Any time the state updates, `render` is called

# Rules of this.setState
  setState returns an object that will represent our state object.
  setState triggers a call to the render() function

# Workings of `setState()`
  `setState` is the only legitimate wat to update state after the initial stat setup.

    class App extends React.Component {
      state = { count: 0 }

      handleIncrement = () => {
        this.setState((prevState) => {
          return { count: this.state.count + 1}
        })
      }

      handleDecrement = () => {
        this.setState((prevState) => {
          return { count: this.state.count - 1}
        })
      }

      render(){
        return(
          <div>
            <div>
              {this.state.count}
            </div>
            <button onClick={this.handleIncrement}>Increment</button>
            <button onClick={this.handleDecrement}>Decrement</button>
          </div>
        )
      }
    }

When working with `setState()` these are the major things you should know:
  update to a component state should be done    using `setState()`
  You can pass an object or a function to `setState()`
  Pass a function when you can to update state multiple times
  Do not depend on this.state immediately after calling `setState()` and make use of the updater function instead.