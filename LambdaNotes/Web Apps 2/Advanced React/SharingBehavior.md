# Sharing Non-Visual Behavior
## Custom Hooks

  > Stateful logic is logic that is built into a component. It can be a function that handles a click event or a typing event, or maybne a function that sets toggle state, or even a logic that formats data passed to the component before it gets displayed. Usually this kind of logic deals with state in the component. Thus the moniker `stateful logic`

    import React, { useState } from 'react'

    export default const DynamicTitle = () => {
      const [title, setTitle] = useState('Hooks are so fun!)
      const [inputText, setInputText] = useState('')

      const handleChange = e => {
        setInputText(e.target.value) // Stateful logic
      }

      const changeTitle = e => {
        e.preventDefault
        setTitle(inputText) // stateful logic
        setInputText('')
      }

      return (
        <div className="Wrapper">
          <h1 className="Title">{title}</h1>
          <form onSubmit={changeTitle}>
            <div className="Input">
              <input
                className="Input-text"
                id="input"
                name="inputText"
                onChange={handleChanges}
                placeholder="Create new title"
                type="text"
                value={inputText}
              />
              <label htmlFor="input" className="Input-label">
                New title
              </label>
            </div>
          </form>
        </div>
      )
    }

## Learn to apply non-visual behavior(stateful logic) with custom hooks

  `Custom hooks`, so called because you are building the hook yourself, allow you to apply non-visual behavior and stateful logic throughout your components by reusing the same hook over and over again. They follow the same patterns of naming that you've already learned. You can build a reusable custom hook for uses as varied aas handling controlled inputs, managing event listeners, and watching for key presses.

    export const useInput = initialValue => {
      const [value, setValue] = useState(initialValue)
      const handleChanges = updatedValue => {
        setValue(updatedValue)
      }
      return [value, setValue, handleChanges]
    }
  
  In the useInput custom hook above

  - first we're taking in an initialValue as a parameter on this function
  - this is then passed into the `useState` hook which returns an array with our `value` variable and `setValue` function(just the same as what you've used up to this point)
  - Next we have a `handleChanges` function that uses the `setValue` function to update the state to a new value.
  - We then proceed to return an array from our `useInput` custom hook that contains the `value` variable, `setValue` function, and `handleChanges` function

  Lets look at the custom hook in action

        const CustomForm = () => {
          const [username, setUsername, handleUsername] = useInput('')
          const [password, setPassword, handlePassword] = useInput('')
          const [email, setEmail, handleEmail] = useInput('')

          const resetValues = e => {
            e.preventDefault
            setUsername('')
            setPassword('')
            setEmail('')
          }

          return (
            <form onSubmit={resetValues}>
              <input
                className="username-text"
                id="username"
                name="username"
                onChange={e => handleUsername(e.target.value)}
                placeholder="Username"
                type="text"
                value={username}
              />
              <input
                className="password-test"
                id="password"
                name="password"
                onChange={e => handlePassword(e.target.value)}
                placeholder="Password"
                type="password"
                value={password}
              />
              <input
                className="email-text"
                id="email"
                name="email"
                onChange={e => handleEmail(e.target.value)}
                placeholder="Email"
                type="text"
                value={email}
              />
              <button type="submit">Submit</button>
            </form>
          )
        }

  Notice how we are setting our `handleUsername`, `handlePassword`, and `handleEmail` functions to process changes to the input. Remember how we returned a `handleChanges` function from our custom hook? Well, we’ve renamed them here `(again, thanks to array destructuring)` and are using them just the same as before. However, now we have less code for them in our component.

  The final thing you should notice is the `resetValue` function. When we invoke it, we use the `setValues` returned from each `useInput (again, each one is named differently thanks to array destructuring)` and pass in our reset value (in this case, an empty string). Isn’t this an easy way to change your state?

  By building out a custom hook, we can skip writing out all of the stateful logic for our non-visual behavior. This produces nice `DRY` code that is easy to read and use.

## Learn to compose hooks in a custom hook to extend stateful logic

    const useLocalStorage = (key, initialValue) => {
      const [storedValue, setStoredValue] = useState(() => {
        const item = window.localStorage.getItem(key)
        return item ? JSON.parse(item) : initialValue
      })
      const setValue(value) => {
        setStoredValue(value)
        window.localStorage.setItme(key, JSON.stringigy(value))
      }
      return [storedValue, setValue]
    }

- First we pass in a key value, and an initial value. 
  These two parameters are used in the useState hook call used immediately inside our custom hooks

  instead of just passing in an initial value to this useState hook, we are using an anonymous arrow function as a callback to do two things:
    * Check if the window.localstorage has a specific item
    * Return that item from local storage if it exists or the initialValue otherwise

- Then we have a setValue function that takes a value as a parameter sets it to the current storedValue by using the setStoredValue provided by useState, and it sets to localStorage.

As our state is now stored, our custom hook will check here on refresh to see if the state exists.

Now we will combine this with our useInput custom hook

    export const useInput = (key, initialValue) => {
      const [value, setValue] = useLocalStorage(key, initialValue)
      const handleChanges = updatedValue => {
        setValue(updatedValue)
      }
      return [value, setValue, handleChanges]
    }

    const useLocalStorage = (key, initialValue) => {
      const [storedValue, setStoredValue] = useState(() => {
        const item = window.localStorage.getItem(key)
        return item ? JSON.parse(item) : initialValue
      })
      const setValue = value => {
        setStoredValue(value)
        window.localStorage.setItem(key, JSON.stringify(value))
      }
      return [storedValue, setValue]
    }
    
While our useLocalStorage hook has stayed the same our useInput custom hook has some really nice upgrades going on. Instead on implementing useState from React as before we're now using useLocalStorage. 

Furthermore we're also taking in two parameters instead of one, a key and initialValue. 

These are then passed directly into the useLocalStorage hook, and it sets about implementing the logic with them that we described above. This returns to our useInput custom hook with either a value from localStorage or our initialValue, and our useInput custom hook then returns a value, setValue function and a handleChanges function in an array just the same as it did before.

    const [username, setUsername, handleUsername] = useInput("userName", "");
    const [password, setPassword, handlePassword] = useInput("password", "");
    const [email, setEmail, handleEmail] = useInput("email", "");
