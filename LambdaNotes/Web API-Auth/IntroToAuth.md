# Introduction to Authentication

Authentication and Authorization are often confused or used interchangeably, but they don't mean the same thing.

Authentication is the process by which our web api verifies the identity of a client that is trying to access a resource. 

Authorization comes after authentication and determines what type of access if any, that user should have

Adding authentication to a Web API requires that an API can:
- register user accounts
- login to prove identity
- logout to invalidate the user's access
- add ability to reset passwords

Proper authentication is difficult

<strong>NEVER STORE PASSWORDS AS PLAIN TEXT</strong>

### Hashing vs Encryption
- Encryption goes two ways. First it utilizes plain text and private keys to generate encrypted passwords and then reverses the process to match to an original password
- Cryptographic hashes only go one way: parameters + input = hash. It is pure; given the same parameters and input it generates the same hash

## Hash passwords before saving to database

When storing a user's password into a database, we must ensure that they are not saved as plain text.

Bcryptjs features include:
- password hashing function
- implements salting both manually and automatically
- accumulative hashing rounds

```
const credentials = req.body;

const hash = bcrypt.hashSync(credentials.password, 14);

credentials.password = hash;

// Move on to save the user.
```

To verify a password

```
const credentials = req.body;

if(!user || !bcrypt.compareSync(credentials.password, user.password)) {
  return res.status(401).json({ error: 'Invalid Credentials!'});
}
```

## Learn to verify passwords using bcrypt

```
server.post('/api/login', (req, res) => {
  let { username, password } = req.body;

  Users.findBy({ username })
    .first()
    .then(user => {
      if(user && bcrypt.compareSync(password, user.password)) {
        res.status(200).json({ message: `Welcome ${user.username}!` })
      } else {
        res.status(401).json({ message: 'Invalid Credentials' })
      }
    })
    .catch(error => {
      res.status(500).json(error)
    })
})
```

## Write middleware to verify credentials

```
function restricted(req, res, next) => {
  const { username, password } = req.headers;

  if(username && password) {
    Users.findBy({ username })
      .first()
      .then(user => {
        if(user && bcrypt.compareSync(password, user.password)) {
          next()
        } else {
          res.status(401).json({ message: 'Invalid Credentials' })
        }
      })
      .catch(error => {
        res.status(500).json({ message: 'Unexpected Error' })
      })
  } else {
    res.status(400).json({ message: 'No Credentials Provided' });
  }
}
```

Example in use

```
server.get('/api/users', restricted, (req, res) => {
  
})
```