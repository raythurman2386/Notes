import React from 'react';

const TodoListItem = ({ todo, onRemovePressed }) => {
	return (
		<div className='todo-item-container'>
			<h3>{todo.text}</h3>
			<div className='button-container'>
				<button className='button-complete'>Complete</button>
				<button
					onClick={() => onRemovePressed(todo.text)}
					className='button-remove'
				>
					Remove
				</button>
			</div>
		</div>
	);
};

export default TodoListItem;
