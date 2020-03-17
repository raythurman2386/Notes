import React, { Component } from 'react';
import { ApolloClient, ApolloProvider, createNetworkInterface, toIdValue } from 'react-apollo';
import { SubscriptionClient, addGraphQLSubscription } from 'subscriptions-transport-ws';
import { BrowserRouter, Link, Route, Switch } from 'react-router-dom';
import './App.css';
import Contacts from './Contacts';
import AddContact from './AddContact';
import ContactSingle from './ContactSingle';

const PORT = 4000;

const networkInterface = createNetworkInterface({
  uri: `http://localhost:${PORT}/graphql`,
});

const wsClient = new SubscriptionClient(`ws://localhost:${PORT}/subscriptions`, {
  reconnect: true
});

const networkInterfaceWithSubscriptions = addGraphQLSubscription(
  networkInterface,
  wsClient
);

const dataIdFromObject = (result) => {
  if (result.__typename) {
    if (result.id !== undefined) {
      return `${result.__typename}:${result.id}`
    }
  }
  return null;
}

const client = new ApolloClient({
  networkInterface: networkInterfaceWithSubscriptions,
  customResolvers: {
    Query: {
      contact: (__, args) => {
        return toIdValue(dataIdFromObject({ __typename: 'Contact', id: args['id'] }))
      },
    },
  },
  dataIdFromObject,
});

class App extends Component {
  render() {
    return (
      <ApolloProvider client={client}>
        <BrowserRouter>
          <div className="App">
            <div className="App-header">
              <Link to="/"><h2>CRM</h2></Link>
            </div>
            <AddContact />
            <Switch>
              <Route exact path="/" component={Contacts}/>
              <Route path="/contact/:contactId" component={ContactSingle}/>
            </Switch>
          </div>
        </BrowserRouter>
      </ApolloProvider>
    );
  }
}

export default App;
