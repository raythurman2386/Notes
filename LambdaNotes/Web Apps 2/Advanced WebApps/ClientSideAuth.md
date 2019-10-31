# Client Side Authentication

> JWT or JSON Web Tokens are generally used in the process for client side authentication.

These tokens are issued by the server and are cryptic strings which can be stored in the client using local storage or session storage.

The server can readily tell it issued the token and nobody else, as well as read the token and be able to tell who you are and what permissions you have.

A common pattern is for a login endpoint to exist, which takes a payload of `username` and `password`. 

If the credentials are known, the server responds with a fresh JWT.

From then on it's the applications responsibility to add an `Authorization: <token>` header to every request, in order to be allowed access to protected resources that require auth.

    import axios from 'axios'

    export const axiosWithAuth = () => {
      const token = localStorage.getItem('token');

      return axios.create({
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `${token}
        }
      });
    }

  Now the token will be returned to us by the server after the user properly authenticates.

  When you login, you want to save to token that's returned to `localStorage` so that the above `axiosWithAuth` module can grab it for the other calls that require the Authorization header to be on it

    const login = () => {
      axios.post('endpoint/here', userCredentials)
        .then(res => {
          localStorage.setItem('token', res.data.token);
          props.history.push('/dashboard');
        })
    }

  Now that we have the token, we can do an AJAX request to an endpoint using the `axiosWithAuth` module

    import { axiosWithAuth } from '../....'

    axiosWithAuth().get('endpoint/path/here').then(data => do something with the data)

## Implement protected routes

As we build our apps, we will most likely need some protected routes - routes that we only want to render if the user has logged in and been authenticated.

The way this normally works is we make a login request, sending the server the user's username and password.

The server will check those credentials, and if it can authenticate the user it will return a token.

Once we have the token, we can add two layers of protection to our app. 

One with protected routes, the other by sending an authentication header with our API calls.

    <Route path='/public' component={Public} />
    <Route path='/login' component={Login} />
    <PrivateRoute path='/private' component={Private} />

    const PrivateRoute = ({ component: Component, ...rest}) => (
      <Route 
        {...rest} 
        render={props =>
          localStorage.getItem('token') ? (
            <Component {...props} />
          ) : (
            <Redirect to='/login' />
          )
        }
      />
    )

  Now lets look at the login page

    import React, { useState } from 'react';
    import { axiosWithAuth } from '../path/to/module';

    const Login = (props) => {
    const [credentials, setCredentials] = useState({});

    const login = e => {
      e.preventDefault();
      axiosWithAuth().post('login/endpoint', credentials)
        .then(res => {
          localStorage.setItem('token', res.data.token);
          this.props.history.push('/');
        })

      const handleChange = e => {
        setCredentials: {
          ...credentials,
          [e.target.name]: e.target.value,
        }
      }

      return (
        ....
      )
    }