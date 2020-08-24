import React from 'react';
import TodoListItem from './TodoListItem';
import NewTodoForm from './NewTodoForm';

const TodoList = ({ todos = [{ text: 'Hello' }] }) => {
	return (
		<div className='list-wrapper'>
			<NewTodoForm />
			{todos.map((todo) => (
				<TodoListItem todo={todo} />
			))}
		</div>
	);
};

export default TodoList;
