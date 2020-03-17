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
  }
};
