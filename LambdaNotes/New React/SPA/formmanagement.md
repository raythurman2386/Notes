# Form Management
## Build a form in React
  Forms are the best way to gather data from your users, or to get your users to interact with your software.

    import React from 'react'

    function App(){
      return (
        <div>
          <form>
            <label>
              Username:
              <input type="text" />
            </label>
          </form>
        </div>
      )
    }

    export default App

## Using onChange to capture input values
  The onChange handler on an input captures the typing event. The event object stores the new value from the input. 

    import React, { useState } from 'react'

    function App(){
      const [inputValue, setInputValue] = useState("")

      const changeHandler = event => {
        setInputValue(event.target.value)
      }

      return (
        <div>
          <form>
            <label>
              Username:
              <input type="text" onChange={changeHandler} />
            </label>
          </form>
        </div>
      )
    }

    export default App

  The changeHandler function can be re used to handle multiple inputs so we can keep our code fairly DRY.

  There are a few gotchas to look out for when using checkboxes.

  The changeHandler above just saves the value of the input to state anytime the input changes.

## Submitting form data

import React, { useState } from 'react'

    function App(){
      const [inputValue, setInputValue] = useState("")

      const changeHandler = event => {
        setInputValue(event.target.value)
      }

      const handleSubmit = (e) => {
        e.preventDefault();
        // Console logs vaule to the console on submit
        console.log(inputValue)
      }

      return (
        <div>
          <form>
            <label>
              Username:
              <input type="text" onChange={changeHandler} />
            </label>
            <button onSubmit={()=> handleSubmit()}>Submit</button>
          </form>
        </div>
      )
    }

    export default App

## Handle multiple submits
  Most of the time when working with forms, you will have more than one input to deal with and handle

    import React, { useState } from "react";
    import "./App.css";

    function App() {
      const [name, setName] = useState("");
      const [password, setPassword] = useState("");

      const handleNameChange = event => {
        setName(event.target.value);
      };

      const handlePasswordChange = event => {
        setPassword(event.target.value);
      };

      const handleSubmit = event => {
        event.preventDefault();
        console.log(name);
        console.log(password);
      };

      return (
        <div className="App">
          {console.log({ name })}
          {console.log({ password })}
          <form onSubmit={event => handleSubmit(event)}>
            <label>
              Username:
              <input type="text" onChange={event => handleNameChange(event)} />
            </label>
            <label>
              Password:
              <input type="text" onChange={event => handlePasswordChange(event)} />
            </label>
            <button>Submit!</button>
          </form>
        </div>
      );
    }

    export default App;

  This gets the job done but the code is not very dry upon a refactor

    function App() {
      const [user, setUser] = useState({
        name: '',
        password: '',
      });

      const handleChange = event => {
        const {name, value} = event.target
        setUser({
          ...user,
          [name]: value
        });
      };

      const handleSubmit = event => {
        event.preventDefault();
        console.log(name);
        console.log(password);
      };

      return (
        <div className="App">
          <form onSubmit={event => handleSubmit(event)}>
            <label>
              Username:
              <input type="text" name="user" onChange={event => handleChange(event)} />
            </label>
            <label>
              Password:
              <input type="text" name="password" onChange={event => handleChange(event)} />
            </label>
            <button>Submit!</button>
          </form>
        </div>
      );
    }

  The above change handler should work correctly for both the user name and the password, and if we were to add in some other inputs it would work for those as well.

  It would also work without destructuring the event.target just as well

  > as long as the input has a name property that matches what it will be added to in state the above handler works perfectly. 

    const handleChange = (e) => {
      setUser({
        ...user, 
        [e.target.name]: e.target.value
      })
    }

## Controlled inputs
  You can control inputs by adding a value attribute. The value attribute forces the text inside the input field to correspond to the string assigned to it.

   function App() {
      const [user, setUser] = useState({
        name: '',
        password: '',
      });

      const handleChange = event => {
        const {name, value} = event.target
        setUser({
          ...user,
          [name]: value
        });
      };

      const handleSubmit = event => {
        event.preventDefault();
        console.log(name);
        console.log(password);
      };

      return (
        <div className="App">
          <form onSubmit={event => handleSubmit(event)}>
            <label>
              Username:
              <input 
                type="text" 
                name="user" 
                value={user.name}
                onChange={event => handleChange(event)} 
              />
            </label>
            <label>
              Password:
              <input 
                type="text" 
                name="password" 
                value={user.password}
                onChange={event => handleChange(event)} 
              />
            </label>
            <button>Submit!</button>
          </form>
        </div>
      );
    }

  Through doing the above and setting the value attribute to what is in state, our inputs are now being "controlled" by state.

  The text in the input will only change if the state changes

  > Why is this important?
    This tries to keep the unidirectional data flow as unidirectional as possible.
  To properly clear the form onSubmit is as easy as:

    const handleSubmit = event => {
        event.preventDefault();
        // Do something with the form
        setUser({ user: '', password: '' })
      };