# JSON Web Tokens

## Explain 3 parts of the JWT
We can use JSON web tokens to add authentication to a web api. 

JWT are an industry standard for transferring data between two parties

JWT's are cryptographically signed, typically using a secret with the HMACSHA-256 algorithm

A JWT is a string that has three parts separated by a period
Those are:

- The Header
- The Payload
- The Signature

The header contains the algorithm with the token type Typically the header will look like:

```
{
  "alg": "HS256",
  "typ": "JWT" 
}
```

The alg key specifies which algorith was used to create the token

***

The Payload inclcudes permissions for the user, information or any other data we'd like to store in the token, which is most likely a user ID

```
{
  "sub": "1234567890", // subject, usually the user id
  "name": "John Doe", // Custom propery
  "iat": 1514234235 // Date the token was issued
}
```

***

To create a signature, we must create a string by base64 encoding, the header and payload together, and then signing it with a secret

## Learn to send a JWT

To produce a JWT and verify the token 

`npm install jsonwebtoken`

- add JWT to the project and require it into auth-router.js
- change the /login endpoint to produce and send the token

```
const jst = require('jsonwebtoken');

router.post('/login', (req, res) => {
  let { username, password } = req.body;

  Users.findBy({ username })
    .first()
    .then(user => {
      if ( user && bcrypt.compare(password, user.password)) {
        const token = generateToken(user)

        res.status(200).json({
          message: `Welcome ${user.username}!`,
          token,
        });
      } else {
        res.status(401).json({ message: `Invalid Credentials` })
      }
    })
    .catch(err => res.status(500).json(err))
})

const generateToken = (user) => {
  const payload = {
    subject: user.id,
    username: user.username,
    // Other data
  }

  const options = {
    expiresIn: '1d',
  }

  return jwt.sign(payload, secrets.jwtSecret, options);
}
```

Ensure that your secret is safely stored in a .env file

module.exports = {
  jstSecret: process.env.JWT_SECRET || 'something secret'
}