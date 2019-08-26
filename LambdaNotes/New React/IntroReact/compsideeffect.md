# Side Effects in React
> Side effects in web apps are very common. It's important to understand what sside effects are so we can handle them properly in our components.

  A side effect is anything that affects something outside the scope of the function being executed. Fetching data from an API, timers, logging, and manually manipulating the DOM are all examples of side effects. There are two categories of side effects in React components, those that don't require clean-up and those that do. 

  A React component without side effects is called a `pure component`. A component can be considered pure if it renders the same output for the same state and props. Therefore, a side effect is something that can cause a component to return a different output for the same state and props. React offers us tools for managing side effects so we can avoid bugs and inconsistencies in our app. The effect hook `useEffect()` is one of those.

## The Effect Hook
  The effect hook tells React that a component needs to run, or execute some side effect. This hook takes in two parameters. The first is a callback function where we can run the side effect. Let's take a look at an effect hook that is handling a console.log.

    useEffect(() => { console.log("Hello from the effect hook!");});

  Used inside the component, puts the effect function inside the component's function scope. This gives it access to state, props, and local variables. So we could also do:

    useEffect(() => { console.log(props.someProp, stateValueOne )})

  Here are some basic examples of other common side effects:

    // API Calls
    const [user, setUser] = useState();
    const [error, setError] = useState();

    useEffect(() => {
      fetchUserData(userId)
        .then(res => setUser(res.data.user))
        .catch(err => setError(err.response.message))
    })

    // Manipulating the DOM
    const [count, setCount] = useState();
    useEffect(() => {
      document.title = `Count is: ${count}`;
    })

    useEffect(() => {
      console.log("The component has mounted.")
    }, []);

## Sync side effects with state and props with effect hook
> There are many times when we may only want a side effect to run when certain data changes. Learning how to sync the effect hook with changes in our state or props is essential to handling side effects in the most efficient manner.

### An empty dependancy array will cause the useEffect to only run on mount. Once parameters are put it, the useEffect will run anytime one of those items change.