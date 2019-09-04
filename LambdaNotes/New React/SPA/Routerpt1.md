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