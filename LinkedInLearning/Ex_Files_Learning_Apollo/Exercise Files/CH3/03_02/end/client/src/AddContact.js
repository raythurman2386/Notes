import React, { Component } from 'react';
import { gql, graphql } from 'react-apollo';

import { contactsListQuery } from './Contacts';

class AddContact extends Component {
  state = {
    firstName: '',
    lastName: ''
  }

  handleSave = ({ mutate }) => {
    const {firstName, lastName } = this.state;
    this.props.mutate({
      variables: {firstName, lastName} 
    })
    .then( res => {
      this.setState({
        firstName: '',
        lastName: ''
      });
    });
  }

  render () {
    return (
      <div>
        <input
          value={this.state.firstName}
          placeholder='First name'
          onChange={(e) => this.setState({firstName: e.target.value})}
        />
        <input
          value={this.state.lastName}
          placeholder='Last name'
          onChange={(e) => this.setState({lastName: e.target.value})}
        />
        <button onClick={this.handleSave}>Save</button>
      </div>
    )
  }

}

const createContact = gql`
  mutation addContact($firstName: String!, $lastName: String!) {
    addContact(firstName: $firstName, lastName: $lastName ) {
      id
      firstName
      lastName
    }
  }
`;

const AddContactsWithMutation = graphql(createContact)(AddContact);

export default AddContactsWithMutation;
