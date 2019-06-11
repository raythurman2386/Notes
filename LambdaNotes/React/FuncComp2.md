# State and Props in React

  Data in react is passed around by using State and Props.
  The direction in which data flows is top to bottom.

# State 
  State is the data that our components will have access to, and when we pass that state around, we call it props.

# Props
  Props stands for properties. When we give a component some `attribute-looking` data on our JSX, we're essentially telling React to build us out an object that we can consume as a parameter inside of a Functional Component.

  Props are immutable(Read only) meaning we cannot mutate props in any fashion.

    const MyComponentWithProps = props => {
      return <h1>Hello, my name is {props.name}.</h1>
    }

    <MyComponentWithProps name="Fred" />
    <MyComponentWithProps name="Wilma" />
    <MyComponentWithProps name="Barney" />

    DATA FLOWS DOWNWARD IN A REACT APPLICATION, FROM STATE TO PROPS

  To ensure that data can be dynamic we need to pass it into our component as a prop. All React Components have access to the props keyword. To grad any dynamic data that we want rendered to our component we use props.