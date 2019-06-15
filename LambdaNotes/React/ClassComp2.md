# Create/Read/Update State
  State is mutable
  All changes to the state object must be done through the setState function
  All components are stateless unless there is a state object in them.
  Any time the state updates, `render` is called

# Rules of this.setState
  setState returns an object that will represent our state object.
  setState triggers a call to the render() function

