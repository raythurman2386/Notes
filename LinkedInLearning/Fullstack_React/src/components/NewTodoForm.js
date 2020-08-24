import React, { useState } from 'react';
import { connect } from 'react-redux';
import { createTodo } from '../actions';

const NewTodoForm = ({ todos, onCreatePressed }) => {
	const [value, setValue] = useState('');

	return (
		<div>
			<input
				type='text'
				value={value}
				placeholder='New Todo'
				onChange={(e) => setValue(e.target.value)}
			/>
			<button
				onClick={() => {
					const isDuplicate = todos.some((todo) => todo.text === value);
					if (!isDuplicate) {
						onCreatePressed(value);
						setValue('');
					}
				}}
			>
				Create Todo
			</button>
		</div>
	);
};

const mapStateToProps = (state) => ({
	todos: state.todos,
});

const mapDispatchToProps = (dispatch) => ({
	onCreatePressed: (text) => dispatch(createTodo(text)),
});

export default connect(mapStateToProps, mapDispatchToProps)(NewTodoForm);
