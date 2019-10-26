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
