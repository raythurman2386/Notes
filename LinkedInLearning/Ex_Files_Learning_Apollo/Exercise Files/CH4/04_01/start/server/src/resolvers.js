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
      const newContact = { id: args.id, firstName: args.firstName, lastName: args.lastName};
      contacts.push(newContact);
      return newContact;
    }
  }
};
