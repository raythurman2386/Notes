const { GraphQLServer, PubSub } = require('graphql-yoga');

const messages = [];

const typeDefs = `
  type Message {
    id: ID!
    user: String!
    content: String!
  }

  type Query {
    messages: [Message!]
  }

  type Mutation {
    postMessage(user: String!, content: String!): ID!
  }

  type Subscription {
    messages: [Message!]
  }
`;

// keep track of the users
const subscribers = [];
const onMessagesUpdate = (fn) => subscribers.push(fn);

const resolvers = {
	Query: {
		messages: () => messages,
	},
	Mutation: {
		postMessage: (parent, { user, content }) => {
			const id = messages.length;
			messages.push({
				id,
				user,
				content,
			});
			// Alert the system when new message arrives
			subscribers.forEach((fn) => fn());
			return id;
		},
	},
	Subscription: {
		messages: {
			subscribe: (parent, args, { pubsub }) => {
				const channel = Math.random().toString(36).slice(2, 15);
				onMessagesUpdate(() => pubsub.publish(channel, { messages }));
				setTimeout(() => pubsub.publish(channel, { messages }), 0);
				return pubsub.asyncIterator(channel);
			},
		},
	},
};

// PubSub for subscriptions
const pubsub = new PubSub();
const server = new GraphQLServer({ typeDefs, resolvers, context: { pubsub } });
server.start(({ port }) => {
	console.log(`Server started on http://localhost:${port}`);
});
