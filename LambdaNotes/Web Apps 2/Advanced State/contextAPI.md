# Context API
  In a typical React application, data is passed top-down via props, but this can be cumbersom for certain types of props that are required by many components within an application. 

  Context provides a way to share values like these between components without having to explicitly pass a prop through every level of the tree.

  We use the Context API when we have global data that lots of components share, or when we have to pass data through intermediate components.

  This helps us keep our state relatively clean.

  Although this can potentially make components harder to reuse.

  > Provider - The Provider component is used in higher heirarchy of the tree. It accepts a prop called Vlaue. It acts as a root component in the hierarchical tree such that any child in the tree can access the values that are provided by the context provider.

    render() {
      return (
        <Provider value={this.state.contextValue}>{this.props.children</Provider>}
      )
    }

  > Consumer - Consumes the data which is being passed, irregardless of how deeply nested it is located in the component tree. That means, Consumer don't have to be necessarily be the child of Provider.

    render() {
      return (
        <Consumer>
          {contextValue => <Child arbitraryProp={contextValue} />}
        </Consumer>
      )
    }

  In React we have a predefined function to create a Context

    const Context = React.createContext();

## Provide data to the component tree with a context provider
