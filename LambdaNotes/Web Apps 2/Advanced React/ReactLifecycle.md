# React Lifecycle Methods

## componentWillMount

  Your component is going to appear on the screen shortly. 

  With componentWillMount there is no component to play with yet. So you can't do anything involving the DOM    

  ### Most common use case
  * App configuration in your root component

  #### Can call setState
  * Yes, but don't
  
## componentDidMount

  Here is where you load in your data

  > You can't guarantee the AJAX request won't resolve before the component mounts. If it did, that would mean that you'd be trying to setState on an unmounted component, which not only won't work, but React will yell at you for doing. Using componentDidMount for AJAX will guarantee that there's a component to update

  ### Most common use case
  * Start AJAX calls to load in data for your component

  #### Can call setState
  * Yes

## componentWillReceiveProps

  When a parent component is passing down props to a child componentWillReceiveProps is called with the next props as the argument

  Now we have access to both the next props and our current props

  Here's what we should do:
  * check which props will change
  * if the props will change in a significant way, act on it

  ### Most common use case
  * Act on particular prop changes to trigger state transitions

  #### Can call setState
  * Yes

## shouldComponentUpdate

  We have new props. Typical React says that when a component receives new props, or new state, it should update.

  But our component is a little bit anxious and is going to ask permission first.

  So now we get a shouldComponentUpdate, called with nextProps as the first argument and nextState the second

  shouldComponentUpdate should always return a boolean

  ### Most common use case
  * Controlling exactly when your component will re-render

  #### Can call setState
  * No

## componentWillUpdate

  Functionally the same as componentWillReceiveProps, except you are not allowed to call this.setState

  If you were using shouldComponentUpdate and needed to do something when props change, componentWillUpdate makes sense.

  But it's probably not going to give you a whole lot of utility

  ### Most common use case
  * Used instead of componentWillReceiveProps on a component that also has shouldComponentUpdate

  ##### Can call setState
  * No

## componentDidUpdate

  Here we can accomplish the same stuff that we did in componentDidMount

  ### Most common use case
  * Updating the DOM in response to prop or state changes

  #### Can call setState
  * Yes

## componentWillUnmount

  Here is where you component is dying. You can cancel any outgoing network requests, or remove all event listeners associated with the component.

  Basically accomplish clean up for the component in question

  ### Most common use case
  * Clean up leftover debris from your component

  #### Can call setState
  * No