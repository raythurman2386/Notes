# React
  React is a powerful unopinionated UI library who's main purpose is to be used to build powerful applications. React uses encapsulated pieces of UI called Components that concern themselves with their own individual pieces of the DOM.

  React uses an engine called the Virtual DOM to update any changes that will be made over time to our applications.

# What Problems React solves
  Any application that has a lot of DOM operations in the background will render slowly. 

  If the page has data that changes over time at high rates then there is a requirement for DOM updates to be very fast and reflect in other parts of the UI if they use the same data.

  React solves this without even having the page reload by using a concept called the Virtual DOM.

# Thinking in React
  - Step 1: Break the UI into a Component Hierarchy
    -Identify what will be made into components
    -Components that appear inside another is that components child in the hierarchy.

  - Step 2: Build a static version in React

      Props vs State
        There are two types of model data in React: props and state. It's important to understand the distinction between the two; skim the official docs. https://reactjs.org/docs/interactivity-and-dynamic-uis.html

  - Step 3: Identify the minimal representation of UI state
    -To make your UI interactive you need to be able to trigger changes to your underlying data model.
    -React makes this easy with state
    -REMEMBER DRY!!
      Ask these 3 questions about each component
      1. Is it passed in from a parent via props? If so, it probably isn't state.
      2. Does it remain unchanged over time? If so, it probably isn't state.
      3. Can you compute it based on any other state or props in your component? If so, it isn't state.

  - Step 4: Identify where your state should live

  - Step 5: Add inverse data flow