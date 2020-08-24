import React from 'react';

const TodoListItem = ({ todo, onRemovePressed, onCompletePressed }) => {
	return (
		<div className='todo-item-container'>
			<h3>{todo.text}</h3>
			<div className='button-container'>
				{todo.isCompleted ? null : (
					<button
						onClick={() => onCompletePressed(todo.text)}
						className='button-complete'
					>
						Complete
					</button>
				)}
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
