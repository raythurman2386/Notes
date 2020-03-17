const contacts = [
  {
    id: 1,
    firstName: 'Manny',
    lastName: 'Henri'
  },
  {
    id: 2,
    firstName: 'Jasmine',
    lastName: 'Henri-Rainville'
  },
    {
    id: 3,
    firstName: 'Jeremy',
    lastName: 'Henri-Rainville'
  }
]

export const resolvers = {
  Query: {
    contacts: () => {
      return contacts;   
    },
  },
  Mutation: {
    addContact: (root, args) => {
      const newId = require('crypto').randomBytes(5).toString('hex');
      const newContact = { id: newId, firstName: args.firstName, lastName: args.lastName};
      contacts.push(newContact);
      return newContact;
    }
  }
};
