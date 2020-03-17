import React, { Component } from 'react';
import './App.css';
import Contacts from './Contacts';

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <h2>CRM</h2>
        </div>
        <Contacts />
      </div>
    );
  }
}

export default App;
