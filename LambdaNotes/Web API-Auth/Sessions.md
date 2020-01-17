# Sessions and Cookies

## Use in memory sessions to persist auth

Sessions are commonly used to allow a server to store info about a client

Sessions provide a way to persevere data across requests

When using sessions, each client will have a unique session stored on the server

Basic workflow using cookies and sessions

- Client sends credentials
- Server verify credentials
- Server creates a session
- Server produces and sends cookie
- Client stores cookie
- Client sends cookie on each request
- Server verifies that cookie is valid
- Server provides access to resource

Cookies are not accessible from JS or anywhere because they are cryptographically signed and secure

- client-sessions
- express-session

Common ways to store session data

- Memory
- Memory cache (like Redis)
- Database

Cookies

- Automatically included on requests
- Unique t oeach domain + device pair
- Cannot be sent to different domain
- Sent in the cookie header
- Has body that can have extra info
- Max size around 4kb

### Storing session data in memory

- Wiped when the server restarts
- Causes memory leaks as more and more memory is used
- Good for development

### Storing session data in Memory Cache(preferred way in production)

- stored as key value pair
- server still uses a cookie
- memory cache uses session id to find the data

Advantages

- Quick lookups
- Decoupled from the server
- A single memory cache can serve many applications
- automatically remove old data

Drawbacks

- Another server to set up and manage
- extra complexity
- hard to reset the chache without losing all session data

### Storing session data in database

- Similar to memory store
- cookie still holds session id
- server uses session id to find the data
- retrieveing data is slower than the memory cache
- causes chatter between server and database
- need to manage remove old sessions manually

```
const session = require('express-session')

server.use(
  session({
    secret: 'keep it secret, keep it safe',
    cookie: {
      maxAge: 1 * 24 * 60 * 60 * 1000,
      secure: true // only sets cookies over https
    },
    httpOnly: true,
    resave: false,
    saveUninitialized: false,
  })
)
```

The resave option forces the session to be saved back to the session store, even if it wasn't modified during the request

saveUninitialized forces a session that is "uninitialized" to be saved to the store.

Choosing false is useful for implementing login session and 
`complying with laws that require permission before setting a cookie`

```
app.get('/', (req, res) => {
  req.session.name = 'Frodo';
  res.send('got it')
})

app.get('/greet', (req, res) => {
  const name = req.session.name;
  res.send(`Hello ${req.session.name}`)
})
```

The server sends back a session id with every response and the client sends back taht session id on every request

express-session uses in-memory storage by default

## Implement logout

Sessions remain active til they reach the expiration time configured when they were created

```
server.get('/api/logout', (req, res) => {
  if (req.session) {
    req.session.destroy(err => {
      if (err) {
        res.send(error)
      } else {
        res.send(logged out)
      }
    })
  }
})
```

## Restrict resources to only authenticated users

```
function protected(req, res, next) {
  if (req.session && req.session.userId) {
    next();
  } else {
    res.status(401).json(message)
  }
}
```

That middleware verifies that we have a session and that the userId is set.

```
server.get('/api/users', protected, (req, res) => {
  db('users)
    .then(users => res.json(users))
    .catch(err => res.json(err))
})
```