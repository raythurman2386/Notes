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