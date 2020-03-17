import React, { Component } from 'react';
import { ApolloClient, ApolloProvider, createNetworkInterface } from 'react-apollo';
import './App.css';
import Contacts from './Contacts';
import AddContact from './AddContact';

const networkInterface = createNetworkInterface({
  uri: 'http://localhost:4000/graphql',
});

const client = new ApolloClient({
  networkInterface,
});

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
