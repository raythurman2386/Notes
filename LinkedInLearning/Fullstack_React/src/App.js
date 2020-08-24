import { hot } from 'react-hot-loader/root';
import React from 'react';
import './App.css';

// Components
import TodoList from './components/TodoList';

const App = () => (
	<div className='App'>
		<TodoList />
	</div>
);

export default hot(App);
