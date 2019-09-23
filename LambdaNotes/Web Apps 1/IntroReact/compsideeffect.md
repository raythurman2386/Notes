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

> Using a dependency array as the second argument in the effect hook, we can tell it with which state or props the effect should be synced. This is a handy guide to use as you begin the build the mental model for this principle:

… the question is “with which state and props does this effect synchronize with”

    useEffect(fn); // all state and props
    useEffect(fn, []); // no state or props
    useEffect(fn, [these, states, props]);

## Fetch data from an API with the effect hook

Now that we know how to sync effects with certain data, and we know how to avoid infinite loops, let's take a deeper look at fetching data wthin an effect hook. There are a couple possible situations we want to look at with fetching data in a component. First is writing an effect that is not synced with any state or props sor that it only fetches data once as the component mounts. The other is writing an effect that makes an API call that could fire again during the life of the component.

    function App(){
      const [dogPic, setDogPic] = useState('');

      useEffect(() => {
        axios
          .get(//some url would go here)

          // Set the data to state
          .then(res => setDogPic(res.data.message))

          // Always use error handling
          .catch(err => console.log(err))

          // Empty Array means it will only fire once as the component mounts
      }, [])

      return (
        <div className="App">
          <h1>We Love Puppers</h1>
          <img src={dogPic} alt="a random dog" />
        </div>
      )
    }

    function App() {
      const [data, setData] = useState({ hits: [] });
      const [query, setQuery] = useState("react");

      useEffect(() => {
        const fetchData = () => {
          axios
            .get("https://hn.algolia.com/api/v1/search?query=" + query)
            .then(res => setData(result.data));
        };

        fetchData();
      }, [query]);

      return (
        <>
          <input value={query} onChange={e => setQuery(e.target.value)} />
          <ul>
            {data.hits.map(item => (
              <li key={item.objectID}>
                <a href={item.url}>{item.title}</a>
              </li>
            ))}
          </ul>
        </>
      );
    }

## Learn to clean up side effects in the effect hook

    const App = () => {
      const [position, setPosition] = useState({ x: 0, y: 0 });

      useEffect(() => {
        // Add an event listener
        const setFromEvent = e => setPosition({ x: e.clientX, y: e.clientY });
        window.addEventListener("mousemove", setFromEvent);
      }, []);

      return (
        <div>
          {position.x}:{position.y}
        </div>
      );
    };

Now we will add a function to the useEffect to clean up the event listener

    const App = () => {
      const [position, setPosition] = useState({ x: 0, y: 0 });

      useEffect(() => {
        const setFromEvent = e => setPosition({ x: e.clientX, y: e.clientY });
        window.addEventListener("mousemove", setFromEvent);

        // the function returned here will remove, or "clean up", the event listener
        return () => {
          window.removeEventListener("mousemove", setFromEvent);
        };
      }, []);

      return (
        <div>
          {position.x}:{position.y}
        </div>
      );
    };
