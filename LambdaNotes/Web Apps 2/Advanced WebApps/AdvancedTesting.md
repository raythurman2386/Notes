# Advanced React Testing

## Snapshot Testing

Snapshot Testing is a useful tool for detecting `regressions` because we get immediate feedback in the form of a failing test.

A snapshot is a JSON representation of a component's output. When the tests run, the current output of the component is compared to the saved snapshot and if anything changed, the test will fail.

When a snapshot test fails, we can choose to update the snapshot if the change to the components's output was intended.

Since a snapshot is simply a JSON object, it is committed to source control along with the rest of the code so it always stays in sync with the components implementation

The steps required to create a snapshot are as follows:

- use a test renderer to create a serializable component tree
- write an assertion to using the .toMatchSnapshot() matcher with the generated tree
- the first time the test runs, the snapshot will be created and the test will pass
- if the components output changes and the change is intentional, simply press u to update the snapshot, if the change was unintentional fix the component

### Advantages of Snapshot Testing

- requires very little code
- helps detect regressions
- committed to source control
- easy to implement

### Drawbacks of Snapshot Tests

- easy to bypass
- too sensitive, breaks the build for minor changes
- waste of time while actively changing components
- only protects against regressions
- adds extra files to the project

Follow Along

    import renderer from 'react-test-renderer'

    describe('<App />', () => {
      it('should match snapshot', () => {
        const tree = renderer.create(<App />).toJSON()

        expect(tree).toMatchSnapshot()
      })
    })

  We import react-test-renderer and use it's .create() method to instantiate the App component. Next we chain a call to the `toJSON()` method to get the JSON representation of the components tree and use expect() in conjunction with the `.toMatchSnapshot()` matcher to assert that the components output is the same as the recorded snapshot.

## Testing Asynchronous code

Most real world applications need to deal with asynchronous operations. Adding tests to async code is challenging as we need to make sure the code has finished executing and the application is stable before running the assertions

When writing these tests we need to notify Jest that the async code has finished executing and it is time to run the assertions

There are a few different ways to do this
  - Invoke a `done()` callback passed to the test as a first argument when the async code is done
  - Return a promise from a test so Jest will wait for it to resolve or reject
  - Pass an async function to `describe()`

Follow Along

Create an async helper inside helpers.js

    export const asyncThing = (callback) => {
      return new Promise((resolve) => {
        setTimeout(() => {
          callback()
          resolve(7)
        }, 1000)
      })
    }    

Create test cases inside the test file

    describe('asyncThing function', () => {
      it('eventually resolves to 7', () => {
        // using jest.useFakeTimers() directly under imports
        const promise = help.asyncThing(Function.prototype)

        jest.runAllTimers() // Runs all the timers so we dont
        // Have to wait

        const resolvedValue = null
        const expected = 7
        help.asyncThing(Function.prototype).then(res => {
          expect(resolvedValue).toBe(expected)
        })
      })
      it('eventually calls the callback', () => {
        // spy
        const spy = jest.fn()
        expect(spy).not.toBeCalled()

        // save promise to a var
        const promise = help.asyncThing(spy)

        jest.runAllTimers()

        promise.then(res => {
          expect(spy).toBeCalled()
        })
      })
    })

## Use Mocks and Spies in unit tests

A function being tested may have inconvenient dependencies on other objects. To isolate the behavior of the function it's often desirable to replace the other objects with mocks that simulate the behavior of the real objects.

Another use of mocks is as "spies", because they let us spy on the behavior of a function that is called by some other code.

Mock functions can keep track of calls to the function, as well as the parameters passed in those calls. We can optionally define an implementation for the mock.

Simpler mocks that implement just enough behavior to have the test execute are sometimes referred to as "stubs"

    // inside utils.js file
    export const executeIfEven = (number, callback) => {
      if(number % 2 === 0) {
        callback(number)
      }
    }

     it('executes the callback with number, if number is even', () => {
      const spy = jest.fn(); // Arrange!
      help.executeIfEven(2, spy); // Act!
      expect(spy).toBeCalledWith(2) // Assert!
    });
    it('does NOT execute the callback, if number is odd', () => {
      const spy = jest.fn();
      help.executeIfEven(1, spy);
      expect(spy).not.toBeCalled()
    });

## Fire events and test async operations

Following the philosophy of testing the UI the same way a user would, we will simulate a click event on a button which triggers an async operation that results in a new piece of DOM being mounted. To this effect we will refactor App.js so it renders a flash message obtained from a fake api

      import React, { useState } from 'react';

      const App = () => {
        const [message, setMessage] = useState('');

        fakeApiCall = () => Promise.resolve('Success!')

        const onClickHandler = () => {
          this.fakeApiCall().then(res => setMessage(res));
        }

        return (
          <div>
            <span>{message}</span>
            <button onClick={onClickHandler}>
              Get message!
            </button>
          </div>
        );
      }

      // Testing file
      import { render, fireEvent } from "@testing-library/react"

      it('renders success text', () => {
        const { getByText, findByText } = render(<App />)

        act(() => {
          fireEvent.click(getByText("Get message!"))
        })
        
        findByText(/success/i)
      })