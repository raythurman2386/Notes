import React, { Component } from 'react';
import { ApolloClient, ApolloProvider, createNetworkInterface } from 'react-apollo';
import { SubscriptionClient, addGraphQLSubscriptions } from 'subscriptions-transport-ws'; 
import { BrowserRouter, Link, Route, Switch } from 'react-router-dom';
import './App.css';
import Contacts from './Contacts';
import AddContact from './AddContact';
import ContactSingle from './ContactSingle';

const networkInterface = createNetworkInterface({
  uri: `http://localhost:${PORT}/graphql`,
});

const wsClient = new SubscriptionClient(`ws://localhost:${PORT}/subscriptions`, {
  reconnect: true
});

const networkInterfaceWithSubscriptions = addGraphQLSubscriptions(
  networkInterface,
  wsClient
);
class App extends Component {
  render() {
    return (
      <ApolloProvider client={client}>
        <div className="App">
          <div className="App-header">
            <h2>CRM</h2>
          </div>
          <AddContact />
          <Contacts />
        </div>
      </ApolloProvider>
    );
  }
}

export default App;
