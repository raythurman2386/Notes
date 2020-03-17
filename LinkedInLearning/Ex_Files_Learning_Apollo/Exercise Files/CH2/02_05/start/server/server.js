import express from 'express';
import bodyParser from 'body-parser';
import { graphqlExpress, graphiqlExpress } from 'apollo-server-express';
import { schema } from './src/schema';

const myGraphQLSchema = schema;
const PORT = 4000;

const server = express();

server.use('/graphql', bodyParser.json(), graphqlExpress({ schema: myGraphQLSchema}));
server.use('/graphiql', bodyParser.json(), graphiqlExpress({ endpointURL: '/graphql'}));

server.listen(PORT);
