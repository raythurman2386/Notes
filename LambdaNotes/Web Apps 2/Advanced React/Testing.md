# Why Test?

  * Surfaces bugs faster
  * Reduces risk of regressions
  * Allows us to trust the code
  * Makes us think about edge cases
  * Acts as a safety net when making changes
  * Acts as documentation for the code

  Not Testing could result in:

  * Forces to use expensive manual testing
  * Causes bugs and edge cases to be encountered later
  * Makes refactoring code riskier
  * Can make codebases fragile

## Types of testing

  - Unit Testing
  >Tests smaller units of software in isolation. Usually many unit tests in a codebase

  - Integration Testing
  > Several units of a software are tested as a group to ensure they work together correctly

  - End-to-End Testing
  > E2E testing is where the whole application is tested. Simulating real user scenarios closely.

## Learn to use Jest to unit test functions

  Testing Pure Functions are easy to unit test as they always return the same value, given the same input. 

  Testing them is a matter of comparing actual output against expected output for a variety of arguments.

  > Jest comes installed already anytime you are working inside of a Create-React-App!