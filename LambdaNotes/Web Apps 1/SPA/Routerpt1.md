# React Router I
## Client Side Routing
  Client side routing is a JavaScript managed routing option. It offers control over you site URL and content without necessarily having to wait for a server to respond with content.

  Server side routing is how the internet has worked for decades. Every link click and address bar change is a new request to a remote server.
  Server routing is not very efficient.

  > Client side pros
    Faster, no page reloads, more control of the app

  > Client side cons
    Slower initial load time, use to had SEO issues

  > Server side Pros
    Faster initial paint, smaller file sizes to be fetched
    easier on Low bandwidth

  > Server side Cons
    page refreshes, contacting server with every request

## Set up React Router to an app
  React Router is a client side wrapper for React applications

    yarn add react-router-dom
          or
    npm install react-router-dom

  Once Router is installed, it will be used as our base component wrapping our entire app.

    import { BrowserRouter as Router } from 'react-router-dom'

    ReactDOM.render(<Router><App /></Router>, document.getElementById('root'))

  With BrowserRouter comes new Props and State called `history` and `match` these are necessities for the Routes

## The Route component
  > Routes are a way of getting to a destination

    import { Route } from 'react-router-dom'

  The `Route` component is the way we declare what components will be mounted based on what URL's are being requested by the user.

  The Route components takes in a few `props`, the first is the `path` where the ROute component will trigger when someone types in that path in the URL.

  The next important `prop` is the `component` prop. This is the `component` that you want React to mount when the URL matches the requested `path`

    <Route exact path="/" component={Home} />
    <Route path="/contact" component={Contact} />
    <Route path="/about" component={About} />
    <Route path="/users/ component={Users} />
  
  `exact` says that the specified path requested will be the only if the path matches exactly what was requested.

## The Link component
    import { Link } from 'react-router-dom'

  The `Link` component is Reacts way of implementing an `a` tag although it has a few different properties that we can use to control the component.

  instead of the `href` attribute the `Link` component gets to use 
  `to="/"`

## Creating Dynamic Routes
    import React from 'react';

    const avengerData = []; // get the data from the same source above

    function AvengerPage(props) {
      const avenger = avengerData.find(avenger => props.match.params.id === avenger.id);
      return (
        // ...jsx goes here - something like...
        <h1>{avenger.name}</h1>
        // ...etc
      );
    }

  There is an error with the above statement. When you are comparing your props.match id to the avenger id you are comparing a string and an int

  To correct the error you will need to use 
    
    Number(props.match.params.id) === avenger.id
