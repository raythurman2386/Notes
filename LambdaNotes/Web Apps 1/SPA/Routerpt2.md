# React Router part 2
## Pass data via the render prop
  `Render prop` is a prop on a component that takes in a function that returns a component. 

  This pattern is known as "render props" 

  According to the React docs, a render prop is a function prop that a component uses to know what to render.

    <Route render={ () => <MyComponent someProp={someData} someOtherProp-{moreData} /> } />

  That works to get our data to the component, but this causes us to lose the 
  > history, match, and location props
  that the Router component initially added.

    <Route render={props => <MyComponent {...props} someProp={someData} someOtherProp-{moreData} />} />

  We can pass props as a parameter and use the ES6 spread operator to add those three props back to our render.

## Adding nested routes and sub-nav views
    function ContactPage() {
      return (
        <div className="ContactPage">
          <ContactProfileHeader />
          <ContactProfileTabs />

          // Nested routes
          <Route exact path="/contact/:id/activity" component={ContactProfileActivity} />
          <Route exact path="/contact/:id/appointments" component={ContactProfileAppointments} />
          <Route exact path="/contact/:id/documents" component={ContactProfileDocuments} />
        </div>
      );
    }

  Keep an eye out for where the `exact` keyword is being placed. With nested routes `exact` could cause errors and bugs when traversing your webpage.

## Use the history object for routes
  The `history` prop that React Router passes to components can be used to load different routes in response to events other than a user clicking on a link.

  An example would be navigating to a new page after a promise has resolved and new data is available.

    function Home(props){
      return (
        <div>
          <h1>Home Component</h1>
          <p>Home page</p>
          <button onClick={greet}>Greet</button>
        </div>
      )

      function greet(){
        props.history.push('/greet/Luke')
      }
    }

## Link vs NavLink
  Very similar in nature

  With NavLink comes the class `active` to the anchor tag when the url matches thhe path in the NavLink component.

  If we would like to use something other than `.active` for styling you could pass

    <NavLink to="/" activeClassName="activeNavButton">Home</NavLink>
    <NavLink to="/about" activeClassName="activeNavButton">About</NavLink>
