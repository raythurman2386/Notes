# Class Components
  Declare your `class component` by extending `React.Component`

    class Foo extends React.Component{}

  Second use the `constructor` function to set up some state. Since we are extending we must also call `super()` otherwise we will not have access to `this`

    constructor(){
      super();
      this.state = {}
    }

  Next you will need to render some sort of UI to the DOM. We do this by calling the `life-cycle method render`

    render(){
      return <div>Hello World</div>
    }

  Once all three of those steps are complete our component should look like:

    class Foo extends React.Component{
      constructor(){
        super()
        this.state = {}
      }

      render(){
        return (
          <div>Hello World</div>
        )
      }
    }

  The `state` object that we set up on our `constructor` is a very React-specific way of doing things. It allows us to drive our UI using data.

  ## Share data between components with state and props